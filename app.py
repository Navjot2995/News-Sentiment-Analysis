# Generate the Streamlit app code for News Sentiment Dashboard
streamlit_code = """
import streamlit as st
import pandas as pd
from textblob import TextBlob
import altair as alt

# Load the JSON data
@st.cache_data
def load_data():
    df = pd.read_json("Raw Data v4.json")
    df = df[df['Full_Article'].notnull()].copy()
    df['Sentiment_Score'] = df['Full_Article'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['Sentiment_Label'] = df['Sentiment_Score'].apply(
        lambda x: 'Positive' if x > 0.1 else ('Negative' if x < -0.1 else 'Neutral'))
    df['published_datetime_utc'] = pd.to_datetime(df['published_datetime_utc'])
    return df

df = load_data()

st.title("📰 News Sentiment Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
sentiment_filter = st.sidebar.multiselect("Sentiment", options=df['Sentiment_Label'].unique(), default=df['Sentiment_Label'].unique())
source_filter = st.sidebar.multiselect("Source", options=df['source_name'].unique(), default=df['source_name'].unique())
date_range = st.sidebar.date_input("Published Date Range", [df['published_datetime_utc'].min().date(), df['published_datetime_utc'].max().date()])

# Filtered data
filtered_df = df[
    (df['Sentiment_Label'].isin(sentiment_filter)) &
    (df['source_name'].isin(source_filter)) &
    (df['published_datetime_utc'].dt.date >= date_range[0]) &
    (df['published_datetime_utc'].dt.date <= date_range[1])
]

# Display sentiment breakdown
st.subheader("📊 Sentiment Distribution")
chart_data = filtered_df['Sentiment_Label'].value_counts().reset_index()
chart_data.columns = ['Sentiment', 'Count']
chart = alt.Chart(chart_data).mark_bar().encode(x='Sentiment', y='Count', color='Sentiment')
st.altair_chart(chart, use_container_width=True)

# Display articles
st.subheader("🗞️ Articles")
for _, row in filtered_df.iterrows():
    st.markdown(f"### [{row['title']}]({row['link']})")
    st.markdown(f"**Published:** {row['published_datetime_utc'].date()} | **Source:** {row['source_name']}")
    st.markdown(f"**Sentiment:** `{row['Sentiment_Label']}` | **Score:** `{row['Sentiment_Score']:.2f}`")
    st.markdown("---")
"""

# Save the code to a .py file
streamlit_file_path = "/mnt/data/news_sentiment_dashboard.py"
with open(streamlit_file_path, "w") as f:
    f.write(streamlit_code)

streamlit_file_path
