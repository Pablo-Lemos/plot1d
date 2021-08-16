import matplotlib.pyplot as plt
import color_utilities as cu
import os
import csv
import matplotlib.gridspec as gridspec

def read_csv(points_file):
    points = []
    with open(points_file, 'r') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        for row in reader:
            points.append(row)

    return points

def plotter(points_file, xlabel = None, out_folder = None, plot_name = None, save = False, xmargin = 0.05):

    if not plot_name:
        plot_name = 'plot'

    if not out_folder:
        out_folder = './'
    else:
        if not os.path.exists(out_folder):
            os.mkdir(out_folder)

    points = read_csv(points_file)
    ny = 0
    xmin = 1e300
    xmax = -1e300

    for point in points:
        if len(point) == 3:
            ny += 1
            lower = float(point[1]) - float(point[2])
            higher = float(point[1]) + float(point[2])
        elif len(point) == 4:
            ny += 1
            lower = float(point[1]) - float(point[2])
            higher = float(point[1]) + float(point[3])
        if lower < xmin:
            xmin = lower
        if higher > xmax:
            xmax = higher

    # color palette:
    colors = [cu.nice_colors(i) for i in range(ny)]

    # latex rendering:
    plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
    plt.rc('text', usetex=True)

    # plot size in cm. Has to match to draft to make sure font sizes are consistent
    x_size = 8.99
    y_size = 17
    main_fontsize = 10.0

    # start the plot:
    # Start plot
    fig = plt.gcf()
    fig.set_size_inches(x_size / 2.54, y_size / 2.54)
    gs = gridspec.GridSpec(1, 1)
    ax = plt.subplot(gs[0, 0])

    ax.set_xlim(xmin - xmargin*xmin, xmax + xmargin*xmax)
    ax.set_ylim(-0.5, ny - 0.5)

    # the ticks:
    # ax.set_xticklabels( ax.get_xmajorticklabels(), horizontalalignment='center', fontsize=0.9*main_fontsize);
    ax.set_yticklabels([])
    ax.set_yticks([])

    # label on the axis:
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=main_fontsize);

    points = read_csv(points_file)
    lines = 0

    for ii, point in enumerate(points):
        i = ny - ii - 1 + lines
        if len(point) == 3:
            ax.errorbar(float(point[1]), i, xerr=float(point[2]), fmt='.', color=colors[i])
            plt.text(float(point[1]), i+0.1, point[0], fontsize=main_fontsize)
        elif len(point) == 4:
            ax.errorbar(float(point[1]), i, xerr=([[float(point[2])], [float(point[3])]]), fmt='.', color=colors[i])
            plt.text(float(point[1]), i+0.1, point[0], fontsize=main_fontsize)
        elif len(point) == 1:
            ax.axhline(i+0.5, color='k', ls='--')
            lines += 1
        else:
            raise ValueError("Incorrect format of CSV file")


    # update dimensions:
    bottom = 0.12
    top = 0.99
    left = 0.15
    right = 0.99
    wspace = 0.
    hspace = 0.
    gs.update(bottom=bottom, top=top, left=left, right=right,
              wspace=wspace, hspace=hspace)

    if save:
        # save:
        plt.savefig(os.path.join(out_folder, plot_name + '.pdf'))
    else:
        plt.show()



if __name__ == '__main__':
    plotter('./example.csv')
