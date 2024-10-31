import customtkinter
import threading
import pandas as pd
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

    # Entry field for vector size
    size_label = customtkinter.CTkLabel(frame, text="Enter vector size:", font=("Courier New", 16))
    size_label.pack(pady=10)

    vector_size_entry = customtkinter.CTkEntry(frame, width=200, font=("Courier New", 16))
    vector_size_entry.pack(pady=10)

    single_tests_button_text = 'Execute Quicksort tests once'
    run_single_test_button = customtkinter.CTkButton(
        frame, command=lambda: start_loading_animation(frame, title_label, vector_size_entry.get()),
        text=single_tests_button_text, font=("Courier New", 16, "bold"),
        width=50, height=50,
        fg_color="#663399", hover_color="#4B0082"
    )
    run_single_test_button.pack(padx=20, pady=10)

    many_tests_button_text = 'Generate excel with 100 tests'
    run_many_tests_button = customtkinter.CTkButton(
        frame, command=lambda: start_loading_animation(frame, title_label, vector_size_entry.get()),
        text=many_tests_button_text, font=("Courier New", 16, "bold"),
        width=50, height=50,
        fg_color="#663399", hover_color="#4B0082"
    )
    run_many_tests_button.pack(padx=20, pady=10)

    def start_loading_animation(new_frame, new_title_label, vector_size):
        # Display loading label
        loading_label = customtkinter.CTkLabel(
            new_frame, text="Loading...", font=("Courier New", 16, "italic"),
        )
        loading_label.pack(pady=(10, 20), side="top")

        # Start update_graph in a separate thread
        threading.Thread(target=lambda: update_graph(new_title_label, new_frame, loading_label, vector_size)).start()

    def update_graph(new_title_label, new_frame, loading_label, vector_size):
        app.update()  # Refresh the UI to show the loading label

        # Execute Quicksort tests with the specified vector size
        new_results = run_quicksort_tests(int(vector_size))

        compSwap = pd.DataFrame({
            'Comparacoes totais': new_results[0]['comparisonsTotal'],
            'Trocas totais': new_results[0]['swapsTotal'],
            'Algoritmos': ['Quicksort', 'Cutoff Quicksort', 'Median of Three Quicksort']
        })

        execTimes = pd.DataFrame({
            'Tempos': new_results[1],
            'Algoritmos': ['Quicksort', 'Cutoff Quicksort', 'Median of Three Quicksort']
        })

        compSwap.to_csv('Comparations_and_Swaps.csv', index=False)
        execTimes.to_csv('Execution_Times.csv', index=False)

        # Remove loading label once tests complete
        loading_label.destroy()

        new_x_axis_comparisons = new_results[0]['comparisonsTotal']
        new_x_axis_swaps = new_results[0]['swapsTotal']
        new_x_axis_elements = ['Quicksort', 'Cutoff Quicksort', 'Median of Three Quicksort']

        # Não destrua a caixa de entrada
        for widget in new_frame.winfo_children():
            if (widget != new_title_label
                    and widget != run_single_test_button
                    and widget != run_many_tests_button
                    and widget != vector_size_entry
                    and widget != size_label):
                widget.destroy()

        # Generate comparisons quantity bar graph
        comparisons_title = 'Total comparisons'
        comparisons_graph_frame = customtkinter.CTkFrame(new_frame)
        comparisons_graph_frame.pack(padx=20, side="left")
        create_bar_graph(new_x_axis_comparisons, comparisons_title, new_x_axis_elements, comparisons_graph_frame)

        # Display execution time information
        execution_time_frame = customtkinter.CTkFrame(new_frame)
        execution_time_frame.pack(side="left", expand=True, fill="both")

        time_title_label = customtkinter.CTkLabel(
            execution_time_frame,
            text="CPU execution times (s)",
            font=("Courier New", 18, "bold"))

        time_title_label.pack(pady=10)

        for i, algorithm in enumerate(new_x_axis_elements):
            time_text = f"{algorithm}: {new_results[1][i]:.4f} s"
            time_label = customtkinter.CTkLabel(execution_time_frame, text=time_text, font=("Courier New", 14))
            time_label.pack(anchor="w", padx=10)

        # Generate swaps quantity bar graph
        swaps_title = 'Total swaps'
        swaps_graph_frame = customtkinter.CTkFrame(new_frame)
        swaps_graph_frame.pack(padx=20, side="right")
        create_bar_graph(new_x_axis_swaps, swaps_title, new_x_axis_elements, swaps_graph_frame)

    app.mainloop()
