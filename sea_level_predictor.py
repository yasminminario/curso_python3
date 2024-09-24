import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='purple')


    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = range(df['Year'].min(), 2051)
    line_of_best_fit = intercept + slope * pd.Series(years)
    plt.plot(years, line_of_best_fit, color='red', label='First Line of Best Fit')
    
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000 = range(2000, 2051)
    line_of_best_fit_2000 = intercept_2000 + slope_2000 * pd.Series(years_2000)
    plt.plot(years_2000, line_of_best_fit_2000, color='green', label='Second Line of Best Fit (Since 2000)')
    
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()