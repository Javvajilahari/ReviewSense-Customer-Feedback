📊 ReviewSense – Extracting Insights from Customer Feedback
🚀 Project Overview

ReviewSense is a complete end-to-end customer feedback analytics pipeline designed to convert raw customer reviews into actionable business insights.

The system follows a structured four-stage workflow:

Data Cleaning & Preparation

Sentiment Analysis

Keyword Extraction

Interactive Dashboard Visualization

The final outcome is a dynamic Business Intelligence Dashboard built using Streamlit.

🧩 Project Architecture

Raw Customer Feedback
→ Text Cleaning & Standardization
→ Sentiment Classification
→ Keyword Frequency Analysis
→ Interactive Dashboard
→ Actionable Business Insights

📌 Milestone 1 – Data Cleaning & Preprocessing
🎯 Objective

Prepare raw customer feedback for analysis by removing noise and standardizing text.

⚙️ Processing Steps

Removed special characters and punctuation

Converted text to lowercase

Eliminated extra spaces

Removed unnecessary words (stopwords)

Created a structured clean_feedback column

📂 Input

Raw customer feedback dataset (CSV / Excel)

📤 Output

Milestone1_Cleaned_Feedback.csv

🛠 Technologies Used

Python

pandas

Regular Expressions (re)

📌 Milestone 2 – Sentiment Analysis
🎯 Objective

Classify customer feedback into sentiment categories and quantify customer satisfaction.

⚙️ Processing Steps

Applied TextBlob polarity scoring

Classified feedback as:

Positive

Negative

Neutral

Generated confidence scores (-1 to +1)

Created sentiment distribution visualization

📂 Input

Milestone1_Cleaned_Feedback.csv

📤 Outputs

Milestone2_Sentiment_Results_new.csv

sentiment_bar_chart.png

📊 Output Columns

clean_feedback

sentiment

confidence_score

🛠 Technologies Used

Python

pandas

TextBlob

matplotlib

📌 Milestone 3 – Keyword Extraction
🎯 Objective

Identify frequently occurring keywords to uncover common themes and customer concerns.

⚙️ Processing Steps

Refined cleaned text

Removed non-alphabetic characters

Tokenized words

Counted frequency using Counter

Sorted keywords by descending frequency

📂 Input

Milestone2_Sentiment_Results_new.csv

📤 Output

Milestone3_Keyword_Insights.csv

📊 Output Columns

keyword

frequency

🛠 Technologies Used

Python

pandas

collections.Counter

re (regular expressions)

📌 Milestone 4 – Interactive Dashboard
🎯 Objective

Convert analytical results into an interactive dashboard for dynamic exploration and reporting.

⚙️ Dashboard Features
🔍 Interactive Filters

Sentiment (Positive / Negative / Neutral)

Product selection

Date range filtering

📊 KPI Metrics

Total Reviews

Positive %

Negative %

Neutral %

📈 Visualizations

Sentiment distribution bar chart

Product-wise sentiment summary table

Product sentiment heatmap

Monthly sentiment trend graph

Top keyword frequency chart

Word cloud visualization

Confidence score histogram

📥 Export Options

Download filtered reviews (CSV)

Download keyword list (CSV)

📂 Inputs

Milestone2_Sentiment_Results_new.csv

Milestone3_Keyword_Insights.csv

📤 Outputs

Interactive Streamlit Dashboard

ReviewSense_Filtered_Reviews.csv

ReviewSense_Keywords.csv

🛠 Technology Stack

Python

pandas

TextBlob

matplotlib

seaborn

WordCloud

Streamlit

🏁 Conclusion

ReviewSense demonstrates a complete real-world data analytics pipeline — from raw text ingestion to interactive business intelligence visualization.

The project highlights how unstructured customer feedback can be transformed into structured, measurable, and actionable insights suitable for real business applications.
