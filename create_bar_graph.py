import matplotlib.pyplot as plot

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_bar_graph(x_axis, title: str, x_axis_elements: list[str], frame):
    plot.close()
    figure, ax = plot.subplots(figsize=(6, 5))

    entities_quantity = range(len(x_axis))
    ax.bar(entities_quantity, x_axis, 0.2, color="#663399")

    ax.set_title(title, font="Courier New", fontsize=16, fontweight="bold")
    ax.set_xticks(entities_quantity)
    ax.set_xticklabels(x_axis_elements)

    for i, comparisonsQuantity in enumerate(x_axis):
        ax.text(i, comparisonsQuantity, str(comparisonsQuantity), ha='center', va='bottom')

    canvas = FigureCanvasTkAgg(figure, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=20, pady=20, anchor="w")