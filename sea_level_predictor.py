 # Reference: https://openwritings.net/pg/python/python-use-scipystatslinregress-get-linear-least-squares-regression-equation

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df.columns = ['year', 'csiro', 'lower-bound', 'upper-bound', 'noaa']

    # Scatter plot
    df.plot.scatter(x='year',
                  y='csiro',
                  color='sandybrown',
                  label='Original data')

    # Create first line of best fit
    line_a = linregress(df['year'], df['csiro'])
    x = np.arange(df['year'].min(), 2051)
    plt.plot(x, (line_a.intercept + line_a.slope * x),
           color='red',
           label='Line of best fit',
           linestyle='--',
           linewidth=2)

    # Plot second line of best fit
    sub_df = df[df['year'] >= 2000]
    line_b = linregress(sub_df['year'], sub_df['csiro'])
    x1 = np.arange(2000, 2051)
    plt.plot(x1, (line_b.intercept + line_b.slope * x1),
           color='blue',
           label='Line of best fit from year 2000',
           linestyle='dashdot',
           linewidth=2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
