import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
  fig , ax = plt.subplots(figsize = (13 , 6))

  plt.scatter(x,y)
  # Create first line of best fit
  res = linregress(x,y)
  print(res.slope , res.intercept)
  xfit = np.array([i for i in range(1880,2051)])
  yfit = xfit * res[0] + res[1]

  ax.plot(xfit , yfit)
  # Create second line of best fit
  ndf = df[df['Year'] >= 2000]
  nx = ndf['Year']
  ny = ndf['CSIRO Adjusted Sea Level']
  res1 = linregress(nx,ny)
  print(res1.slope , res1.intercept)
  nxfit = np.array([i for i in range(2000,2051)])
  nyfit = nxfit * res1[0] + res1[1]

  ax.plot(nxfit , nyfit)

  # Add labels and title
  ax.set_xlabel("Year")
  ax.set_ylabel("Sea Level (inches)")
  ax.set_title("Rise in Sea Level")
      
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()