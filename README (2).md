
# 📰 News Sentiment Dashboard

An AI-powered Streamlit app for visualizing and analyzing sentiment in news articles.  
Upload structured article data (in JSON format), automatically analyze sentiment, and explore insights through an interactive UI.

---

## 🚀 Features

- 📄 Upload & parse article data from JSON
- 🔍 Automatic sentiment analysis using TextBlob
- 📊 Visual sentiment distribution with interactive charts
- 📆 Filter by date range, sentiment type, and news source
- 🔗 Clickable article titles with publication info
- 🧠 Easy to extend with keyword search, topic detection, or summarization

---

## 🛠 Requirements

Install the following Python packages:
```bash
pip install streamlit pandas textblob altair
```

---

## 📂 How to Use

1. Place your JSON file (e.g., `Raw Data v4.json`) in the same folder.
2. Run the app using:

```bash
streamlit run news_sentiment_dashboard.py
```

3. Use the sidebar to filter results and explore articles.

---

## 📁 File Structure

```
├── news_sentiment_dashboard.py   # Main Streamlit app
├── Raw Data v4.json              # News article input data (JSON)
├── README.md                     # Project documentation
```

---

## 📌 Notes

- Make sure your JSON contains keys: `title`, `Full_Article`, `link`, `source_name`, and `published_datetime_utc`.
- The sentiment is computed based on article text using TextBlob's polarity scores.

---

## 📬 Future Enhancements

- Add article summarization (T5, BART)
- Use advanced sentiment models (BERT, FinBERT)
- Export filtered data to CSV/Excel
- Word cloud visualization for keywords

---

## 👨‍💻 Author

Developed by an AI Engineer using real-world news data and NLP.

