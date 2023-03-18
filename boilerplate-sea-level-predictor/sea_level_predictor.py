import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x= df['Year']
    y= df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots(figsize= (6,6))
    ax = plt.scatter(x,y)

    # Create first line of best fit
    #create slope line
    slope, intercept, r_value, p_value, stderr = linregress (x,y)

    #set new x, y for a line plot
    x_pred = pd.Series([i for i in range (1880,2051)])
    y_pred = slope*x_pred + intercept

    #create line plot
    plt.plot(x_pred, y_pred, 'r')

    #using linregress
    res = linregress (x,y)

    # Create second line of best fit
    #set new range of data from 2000 to the future
    df_forecast = df.loc[df['Year'] >= 2000]

    #set new x and y for new plot
    x_forecast = df_forecast['Year']
    y_forecast = df_forecast['CSIRO Adjusted Sea Level']
    #calculate new slope 
    slope, intercept, r_value, p_value, stderr = linregress(x_forecast, y_forecast)

    #set x, y to creat a new line graph
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = slope*x_pred2 + intercept

    #create line graph with different color
    plt.plot(x_pred2, y_pred2, 'green')

    # Add labels and title
    #add all plot in 1 figure
    fig, ax = plt.subplots(figsize=(6,6))
    ax = plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    #line plot (1880 - 2050)
    plt.plot(x_pred, y_pred, 'r')

    #line plot (2000 - 2050)
    plt.plot(x_pred2, y_pred2, 'green')

    #add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year', fontsize = 12)
    plt.ylabel('Sea Level (inches)', fontsize= 12)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
