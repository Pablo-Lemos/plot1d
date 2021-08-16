if __name__ == '__main__':
    import plotter

    points_file = 'csv_files/h0_review.csv'
    plotter.plotter(points_file,
                    xlabel=r'$ H_0 \ [\mathrm{km \ s^{-1} \ Mpc^{-1}]}$',
                    save=True,
                    out_folder='plots',
                    plot_name='h0_review',
                    xmargin=0.12)