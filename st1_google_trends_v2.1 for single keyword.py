import pandas as pd
from pytrends.request import TrendReq
from tqdm import tqdm
import time

# Read the CSV file and get the list of keywords
keywords_df = pd.read_csv('keywords.csv')
keywords_list = keywords_df['keywords'].tolist()

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Set search parameters
timeframe = 'today 5-y'  # Search data from the past 5 years
geo = 'US'  # Set to US

# Get and aggregate data
all_data = pd.DataFrame()
all_related_topics = pd.DataFrame()
all_related_queries = pd.DataFrame()
all_suggestions = pd.DataFrame()

for keyword in tqdm(keywords_list):
    # existing code inside the loop
    pytrends.build_payload([keyword], timeframe=timeframe, geo=geo)
    
    # Get interest over time data
    data = pytrends.interest_over_time()
    if not data.empty:
        data = data.drop(labels=['isPartial'], axis='columns')
        all_data = pd.concat([all_data, data], axis=1)

    # Get related topics data
    related_topics = pytrends.related_topics()
    all_related_topics = pd.concat([all_related_topics, pd.DataFrame(related_topics)], axis=0)

    # Get related queries data
    related_queries = pytrends.related_queries()
    all_related_queries = pd.concat([all_related_queries, pd.DataFrame(related_queries)], axis=0)

    # Get suggestions data
    suggestions = pytrends.suggestions(keyword)
    all_suggestions = pd.concat([all_suggestions, pd.DataFrame(suggestions)], axis=0)

    # Delay to prevent rate limit
    time.sleep(15)  # delay for 60 seconds

# Save aggregated data to CSV files
all_data.to_csv('trends_data.csv', index=True)
all_related_topics.to_csv('related_topics_data.csv', index=True)
all_related_queries.to_csv('related_queries_data.csv', index=True)
all_suggestions.to_csv('suggestions_data.csv', index=True)

print("Google Trends data has been saved to CSV files.")
