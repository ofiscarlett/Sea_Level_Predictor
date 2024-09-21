import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df= pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label="Sea Level Data")


    # Create first line of best fit
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended_all = pd.Series(range(1880, 2051))
    sea_levels_all = intercept_all + slope_all * years_extended_all
    plt.plot(years_extended_all, sea_levels_all, 'r', label='Best Fit Line (All Data)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = intercept_recent + slope_recent * years_extended_recent
    plt.plot(years_extended_recent, sea_levels_recent, 'green', label='Best Fit Line (2000 Onwards)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()