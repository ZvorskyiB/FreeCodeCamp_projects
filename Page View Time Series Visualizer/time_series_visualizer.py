import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('Page View Time Series Visualizer\\fcc-forum-pageviews.csv')
df['date']=pd.to_datetime(df['date'])

# Clean data
df = df[(df['value']>=df['value'].quantile(0.025))&(df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig=plt.figure(figsize=(13, 4))
    plt.plot(df['date'], df['value'], color='red', linewidth=1.2)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.set_index('date',inplace=True)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()


    df_bar = df_bar.groupby(['year', 'month']).mean().reset_index()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
    df_bar = df_bar.sort_values('month')


    fig, ax = plt.subplots(figsize=(10, 6))
    # Draw bar plot
    df_bar.pivot(index='year', columns='month', values='value').plot(kind='bar', ax=ax)  # Use ax to plot on the created figure

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months') 




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Draw box plots (using Seaborn)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views") 




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig