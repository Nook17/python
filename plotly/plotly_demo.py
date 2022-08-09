#!/usr/bin/env python3
from plotly.offline import plot
import plotly.graph_objs as graphs


def main():
    x = [1, 2, 3, 4, 5]
    y = [3, 6, 2, 8, 1]
    plot_html = generate_scatter_plot(x, y)
    generate_html(plot_html)


def generate_scatter_plot(x_axis, y_axis):
    figure = graphs.Figure()
    scatter = graphs.Scatter(x=x_axis, y=y_axis)
    figure.add_trace(scatter)
    return plot(figure, output_type='div')


def generate_html(plot_html):
    html_content = "<html><head><title>Graphs</title></head><body>{}</body></html>".format(plot_html)
    try:
        with open('plot_demo.html', 'w') as plot_file:
            plot_file.write(html_content)
    except (IOError, OSError) as file_io_error:
        print("can't open file !!! {}".format(file_io_error))


if __name__ == '__main__':
    main()
