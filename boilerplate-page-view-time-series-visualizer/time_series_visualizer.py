import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv' , parse_dates = ['date'] , index_col = ['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig , ax = plt.subplots(figsize = (15 , 5) )
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    x = df['value']
    y = df.index
    plt.plot(y , x , color = 'red' , label = '2x' , markersize = 5)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['months'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year' , 'months'] , as_index = False).mean()
  

    # Draw bar plot
  
    db = df_bar.pivot_table(index = 'year' , columns = 'months' , values = 'value')

    fig = db.plot.bar(legend = True , figsize = (12,6) , ylabel = 'Average Page Views', xlabel = "Years").figure
    
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'])




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num') 
    fig , ax = plt.subplots(1,2,figsize=(15,5))
    ax[0] = sns.boxplot(x = df_box.year , y = df_box['value']  , ax = ax[0])
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')

    ax[1] = sns.boxplot(x = df_box.month  , y = df_box['value']  ,ax = ax[1])
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
