import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('Sea Level Predictor\\epa-sea-level.csv', sep=',')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    model_1=linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_1=range(df['Year'].min(), 2051)
    plt.plot(x_1, model_1.slope*x_1+model_1.intercept, color='y')

    # Create second line of best fit
    model_2=linregress(df[df['Year']>=2000]['Year'], df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    x_2=range(2000, 2051)
    plt.plot(x_2, model_2.slope*x_2+model_2.intercept, color='r')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()