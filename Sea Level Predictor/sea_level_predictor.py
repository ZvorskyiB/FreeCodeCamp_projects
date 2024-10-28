import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('Sea Level Predictor\\epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    result_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_all = pd.Series(range(1880, 2051))
    y_pred_all = result_all.slope * x_pred_all + result_all.intercept
    plt.plot(x_pred_all, y_pred_all, color='blue', label='1880-2050 trend')


    # Create second line of best fit
    result_recent = linregress(df[df['Year']>=2000]['Year'], df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = result_recent.slope * x_pred_recent + result_recent.intercept
    plt.plot(x_pred_recent, y_pred_recent, color='red', label='2000-2050 trend')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()