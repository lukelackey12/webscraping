'''You will scrape the first 10 pages of quotes and perform the following analysis tasks:

Author Statistics:
Count the number of quotes by each author.
Find the author with the most and least quotes.

Quote Analysis:
Determine the average length of quotes.
Identify the longest and shortest quotes.

Tag Analysis:
If there are tags associated with each quote, analyze the distribution of tags.
What is the most popular tag?
How many total tags were used across all quotes?

Visualization:
Create a visualization using plotly to represent the top 10 authors and their corresponding number of quotes with the highest number first
Create a visualization using plotly to represent the top 10 tags based on popularity'''


import plotly.graph_objects as go
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from collections import defaultdict

# Function to calculate average length of quotes
def average_quote_length(quotes):
    total_length = sum(len(quote) for quote in quotes)
    return total_length / len(quotes)

base_url = 'http://quotes.toscrape.com/page/{}/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

# Data structures to store results
author_quotes_count = defaultdict(int)
all_quotes = []
all_tags = []

# Scraping and data analysis
for page_num in range(1, 11):
    url = base_url.format(page_num)
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    table_rows = soup.find_all(class_='quote')

    for row in table_rows:

        # Author statistics
        author = row.find(class_='author').text.strip()
        author_quotes_count[author] += 1

        # Quote analysis
        quote_text = row.find(class_='text').text.strip()
        all_quotes.append(quote_text)

        # Tag analysis
        tags = row.find_all(class_='tag')
        for tag in tags:
            tag_text = tag.text.strip()
            all_tags.append(tag_text)

# Author Statistics
print()
print("Author Statistics:")

most_quotes_author = max(author_quotes_count, key=author_quotes_count.get)
least_quotes_author = min(author_quotes_count, key=author_quotes_count.get)
print("Author with the most quotes:", most_quotes_author)
print("Author with the least quotes:", least_quotes_author)

# Quote Analysis
print("\nQuote Analysis:")
average_length = average_quote_length(all_quotes)
longest_quote = max(all_quotes, key=len)
shortest_quote = min(all_quotes, key=len)
print("Average quote length:", average_length)
print("Longest quote:", longest_quote)
print("Shortest quote:", shortest_quote)

# Tag Analysis
print("\nTag Analysis:")
tag_distribution = defaultdict(int)
for tag in all_tags:
    tag_distribution[tag] += 1

most_popular_tag = max(tag_distribution, key=tag_distribution.get)
total_tags_used = len(all_tags)
print("Most popular tag:", most_popular_tag)
print("Total tags used across all quotes:", total_tags_used)

# Sort authors by quote count in descending order
sorted_authors = sorted(author_quotes_count.items(), key=lambda x: x[1], reverse=True)
top_10_authors = sorted_authors[:10]

# Extract author names and quote counts
top_10_author_names = [author[0] for author in top_10_authors]
top_10_author_quote_counts = [author[1] for author in top_10_authors]

# Plot top 10 authors and their quote counts
fig1 = go.Figure([go.Bar(x=top_10_author_names, y=top_10_author_quote_counts)])
fig1.update_layout(title='Top 10 Authors by Number of Quotes', xaxis_title='Authors', yaxis_title='Number of Quotes')

# Tag Analysis
tag_distribution = defaultdict(int)
for tag in all_tags:
    tag_distribution[tag] += 1

# Sort tags by count in descending order
sorted_tags = sorted(tag_distribution.items(), key=lambda x: x[1], reverse=True)
top_10_tags = sorted_tags[:10]

# Extract tag names and counts
top_10_tag_names = [tag[0] for tag in top_10_tags]
top_10_tag_counts = [tag[1] for tag in top_10_tags]

# Plot top 10 tags based on popularity
fig2 = go.Figure(data=[go.Pie(labels=top_10_tag_names, values=top_10_tag_counts, textinfo='value')])
fig2.update_layout(title='Top 10 Tags by Popularity')

# Show plots
fig1.show()
fig2.show()