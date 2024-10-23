import matplotlib.pyplot as plot

def create_bar_graph(x_axis, title: str, x_axis_elements: list[str]):
    entities_quantity = range(len(x_axis))

    plot.bar(entities_quantity, x_axis)
    plot.title(title)
    plot.xticks(entities_quantity, x_axis_elements)

    for i, comparisonsQuantity in enumerate(x_axis):
        plot.text(i, comparisonsQuantity, str(comparisonsQuantity), ha='center')

    plot.show()