import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date' , parse_dates= True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (12,4))

    ax = sns.lineplot(data=df, x='date', y='value')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot
    #copy and modify data for monthly bar plot
    df_bar = df.copy()

    #create month and year collumn based on df_bar index
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year

    #show average daily page views for each month grouped by year
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()

    #unstack month collumn
    df_bar = df_bar.unstack()

    #change month collumn name
    df_bar.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    fig = df_bar.plot(kind= 'bar', figsize = (15,8)).figure

    plt.title('')
    plt.xlabel('Years', fontsize = 15)
    plt.ylabel('Average Page Views', fontsize = 15)
    plt.legend(loc ='upper left', title='Months', fontsize = 12)  

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box.sort_values(by=['year','date'],ascending=[False,True],inplace=True)

    # Draw box plots (using Seaborn)
    #draw box plot using seaborn
    #draw first figure (year)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    sns.boxplot(ax=ax1, x='year', y= 'value', data = df_box)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    #draw second figure (Month)
    sns.boxplot(ax=ax2, x='month', y= 'value', data = df_box)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
