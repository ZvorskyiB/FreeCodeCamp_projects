import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('Page View Time Series Visualizer\\fcc-forum-pageviews.csv', sep=',')
df['date']=pd.to_datetime(df['date'])

# Clean data
df = df[(df['value']>=df['value'].quantile(0.025))&(df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax =plt.subplots(figsize=(12,6))
    ax.plot(df['date'], df['value'], color='r', linewidth=0.9)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.index=df_bar['date']
    df_bar['year']=df_bar.index.year
    df_bar['month']=df_bar.index.month_name()

    # Draw bar plot
    fig, ax= plt.subplots(figsize=(12,6))
    df_bar=df_bar.groupby(['year', 'month'], as_index=False).mean()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
    df_bar = df_bar.sort_values('month')
    df_bar.pivot_table(index='year', columns='month', values='value').plot(ax=ax, kind='bar')
    ax.legend(title='Months')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['year']=df_box['date'].dt.year
    df_box['month']=df_box['date'].dt.strftime('%b') 

    # Draw box plots (using Seaborn)
    fig, axs=plt.subplots(1,2, figsize=(15,6))
    sns.boxplot(data=df_box, y='value', x='year', ax=axs[0], color='r')
    sns.boxplot(data=df_box, y='value', x='month', ax=axs[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig 