import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column

df["overweight"] = (df["weight"]/pow(df["height"]/100, 2)).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x <=1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x <=1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars= ["active", "alco", "cholesterol", "gluc", "overweight", "smoke"], id_vars="cardio")



    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    
    

    # Draw the catplot with 'sns.catplot()'



    df_cat = pd.melt(df, value_vars= ["active", "alco", "cholesterol", "gluc", "overweight", "smoke"], id_vars="cardio")

    #grouping
    fig = sns.catplot(data=df_cat, kind="count", x="variable", hue="value",col="cardio").set_axis_labels('variable' , 'total').fig

    #save figure
    fig.savefig('catplot.png')

    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)]= True


    # Set up the matplotlib figure
    fig = df_heat.plot(figsize=(8,8)).figure
  

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, mask=mask, vmin=-0.1, vmax=.7, square=True, annot=True, linewidths=0.5, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
