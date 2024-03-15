from transformers import pipeline


sentiment_model = pipeline("text-classification")

results = sentiment_model(["I am really happy today!", "I had the worst day ever."])
print(f"First sentence: {results}")  