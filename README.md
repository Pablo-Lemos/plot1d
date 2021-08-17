# plot1d

This is a very simple plotting script, to read a CSV file, and produce a plot comparing the 1D posterior distributions. See `plot_h0_review.py` for an example.

Alternatively, the code can be installed with: 

``` 
git clone https://github.com/Pablo-Lemos/plot1d
cd plot1d
python setup.py install
```

And then a plot can be generated from a CSV file using 

```
from plot1d import plotter
plotter.plotter('path/to/csv/file.csv')
```

## Format of CSV file

The CSV file should have no header, and the different entries can have the following format: 

- Rows with a single column are interpreted as dashed horizontal lines
- Rows with three columns are read as "name, mean, sigma"
- Rows with four columns are read as "name, mean, sigma_lower, sigma_higher"
- Do not use rows with a different number of columns. 

## Credit

If you use this script, please credit this repository! 

For any questions, feel free to email me 

pablo.lemos.18@ucl.ac.uk
