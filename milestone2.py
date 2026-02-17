import pandas as pd                     #data handling
from textblob import TextBlob        # For finding sentiment (positive/negative/neutral)
import matplotlib.pyplot as plt      # For plotting graphs

# Function to get sentiment and polarity score from a text
def get_sentiment(text):
    # Convert text to string and get polarity score from TextBlob
    polarity = TextBlob(str(text)).sentiment.polarity
    
    # Decide sentiment based on polarity value
    if polarity > 0:
        return "positive", polarity
    elif polarity < 0:
        return "negative", polarity
    else:
        return "neutral", polarity

# Main program starts here
if __name__ == "__main__":
    # Read the cleaned feedback CSV file
    df = pd.read_csv("Milestone1_cleaned_feedback.csv")
    
    # Apply sentiment function to each feedback and create two new columns
    df[["sentiment", "confidence_score"]] = df["clean_feedback"].apply(
        lambda x: pd.Series(get_sentiment(x))
    )
    
    # Save the new results to a new CSV file
    df.to_csv("Milestone2_Sentiment_Results_new.csv", index=False)
    print("Milestone 2 completed successfully!")
    
    # Count how many reviews are positive, negative, and neutral
    sentiment_counts = df['sentiment'].value_counts()

    # Create a bar chart
    plt.figure(figsize=(8, 5))
    colors = ['green', 'red', 'gray']
    sentiment_counts.plot(kind='bar', color=colors)
    
    # Add title and labels
    plt.title('How Customers Feel - Sentiment Summary', fontsize=14)
    plt.xlabel('Sentiment', fontsize=12)
    plt.ylabel('Number of Reviews', fontsize=12)
    plt.xticks(rotation=0)

    # Add count values on top of each bar
    for i, count in enumerate(sentiment_counts):
        plt.text(i, count + 20, str(count), ha='center', fontsize=11)

    # Save the chart as an image file
    plt.savefig('sentiment_bar_chart.png', dpi=100, bbox_inches='tight')
    
    # Show the chart on screen
    plt.show()
    print("Bar chart saved as: sentiment_bar_chart.png")
    
    # Print first 5 rows of feedback with sentiment and score
    print(df[["clean_feedback", "sentiment", "confidence_score"]].head())