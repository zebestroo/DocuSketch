import pandas as pd
import json as js
import matplotlib.pyplot as plt
from seaborn import heatmap


def draw_plot(data: tuple, axes: tuple, filename: str):
    plt.xlabel(axes[0], color='red')
    plt.ylabel(axes[1], color='red')
    plt.grid()

    plt.plot(data[0], data[1], marker='o', markersize='2', linestyle='None')
    #plt.show()

    plt.savefig(f'plots/{filename}.png')
    plt.close()
    return f'plots/{filename}.png'
    

def draw_plots(data_file):
    paths = []
    with open(data_file) as file:
        data = pd.DataFrame(js.load(file), columns=
            [
                'gt_corners', 
                'rb_corners',
                'mean',
                'max',
                'min',
                'floor_mean',
                'floor_max',
                'floor_min',
                'ceiling_mean',
                'ceiling_max',
                'ceiling_min',
            ]
        )

        heatmap(data.corr(), annot=True, fmt='.2f')
        plt.savefig('plots/correlation_heatmap.png')
        paths.append('plots/correlation_heatmap.png')
        plt.close()

        paths.append(draw_plot((data.gt_corners, data.rb_corners), ('gt_corners', 'rb_corners'), 'plot_0'))
        paths.append(draw_plot((data.floor_max, data.ceiling_max), ('floor_max', 'ceiling_max'), 'plot_1'))
        paths.append(draw_plot((data.floor_min, data.ceiling_min), ('floor_min', 'ceiling_min'), 'plot_2'))
        paths.append(draw_plot((data.floor_mean, data.ceiling_mean), ('floor_mean', 'ceiling_mean'), 'plot_3'))

    return paths


print(draw_plots('data.json'))



