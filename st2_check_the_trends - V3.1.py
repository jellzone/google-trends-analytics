import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_csv('trends_data.csv')

# Convert the 'date' column to a datetime object
data['date'] = pd.to_datetime(data['date'])

# List of columns (keywords)
columns = data.columns[1:]

def plot_trends(keywords):
    """
    Plots the trends for the selected keywords.
    
    Parameters:
    - keywords: a list of strings, each being a column (keyword) in the dataframe.
    """
    
    # Melt the dataframe to a long format for plotting
    melted_data = pd.melt(data, id_vars='date', value_vars=keywords)
    
    # Create the line plot
    fig = px.line(melted_data, x='date', y='value', color='variable')
    fig.show()

# Example usage
plot_trends(columns)
