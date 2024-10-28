import customtkinter
import threading

from create_bar_graph import create_bar_graph
from quicksort_tests import run_quicksort_tests

def create_application():
    app = customtkinter.CTk()

    app.attributes("-fullscreen", True)

    frame = customtkinter.CTkFrame(app)
    frame.pack(fill="both", padx=40, pady=40)

    title = 'Total operations from each Quicksort algorithm'
    title_label = customtkinter.CTkLabel(frame, text=title, font=("Courier New", 24, "bold"))
    title_label.pack(padx=20, pady=20)

    button_text = 'Execute Quicksort tests'
    run_button = customtkinter.CTkButton(
        frame, command=lambda: start_loading_animation(frame, title_label),
        text=button_text, font=("Courier New", 16, "bold"),
        width=50, height=50,
        fg_color="#663399", hover_color="#4B0082"
    )
    run_button.pack(padx=20, pady=(20, 40))

    def start_loading_animation(new_frame, new_title_label):
        # Display loading label
        loading_label = customtkinter.CTkLabel(
            new_frame, text="Loading...", font=("Courier New", 16, "italic"),
        )
        loading_label.pack(pady=(10, 20), side="top")

        # Start update_graph in a separate thread
        threading.Thread(target=lambda: update_graph(new_title_label, new_frame, loading_label)).start()

    def update_graph(new_title_label, new_frame, loading_label):
        app.update()  # Refresh the UI to show the loading label

        # Execute Quicksort tests
        new_results = run_quicksort_tests()

        # Remove loading label once tests complete
        loading_label.destroy()

        new_x_axis_comparisons = new_results[0]['comparisonsTotal']
        new_x_axis_swaps = new_results[0]['swapsTotal']
        new_x_axis_elements = ['Quicksort', 'Cutoff Quicksort', 'Median of Three Quicksort']

        for widget in new_frame.winfo_children():
            if widget != new_title_label and widget != run_button:
                widget.destroy()

        # Generate comparisons quantity bar graph
        comparisons_title = 'Total comparisons'
        comparisons_graph_frame = customtkinter.CTkFrame(new_frame)
        comparisons_graph_frame.pack(padx=20, side="left")
        create_bar_graph(new_x_axis_comparisons, comparisons_title, new_x_axis_elements, comparisons_graph_frame)

        # Display execution time information
        execution_time_frame = customtkinter.CTkFrame(new_frame)
        execution_time_frame.pack(pady=20, side="left", expand=True, fill="both")

        time_title_label = customtkinter.CTkLabel(
            execution_time_frame,
            text="CPU execution times (s)",
            font=("Courier New", 18, "bold"))

        time_title_label.pack(pady=10)

        for i, algorithm in enumerate(new_x_axis_elements):
            time_text = f"{algorithm}: {new_results[1][i]:.4f} s"
            time_label = customtkinter.CTkLabel(execution_time_frame, text=time_text, font=("Courier New", 14))
            time_label.pack(anchor="w")

        # Generate swaps quantity bar graph
        swaps_title = 'Total swaps'
        swaps_graph_frame = customtkinter.CTkFrame(new_frame)
        swaps_graph_frame.pack(padx=20, side="right")
        create_bar_graph(new_x_axis_swaps, swaps_title, new_x_axis_elements, swaps_graph_frame)

    # Start the application with loading animation and automatic execution of Quicksort tests
    app.after(500, lambda: start_loading_animation(frame, title_label))

    app.mainloop()