"""
negativity_filter.py
---------------------
Detects and flags negative sentences in input text using Azure AI Language (Text Analytics).

If Azure keys are not provided or invalid, uses mock logic.
"""

import os
import json
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


# Load Azure config
def load_config():
    try:
        with open("azure_config.json", "r") as f:
            config = json.load(f)
        return config["endpoint"], config["key"]
    except (FileNotFoundError, KeyError):
        print(" Azure config not found or incomplete. Falling back to mock mode.")
        return None, None


# Azure sentiment analysis
def analyze_sentiment_azure(sentences, endpoint, key):
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    response = client.analyze_sentiment(documents=sentences)
    results = []
    for sentence, analysis in zip(sentences, response):
        if not analysis.is_error and analysis.sentiment == "negative":
            results.append((sentence, analysis.confidence_scores.negative))
    return results


# Fallback mock analyzer
def analyze_sentiment_mock(sentences):
    negative_triggers = ["bad", "terrible", "worst", "never", "awful", "hate", "your fault"]
    results = []
    for sentence in sentences:
        if any(word in sentence.lower() for word in negative_triggers):
            results.append((sentence, 0.95))  # fake confidence
    return results


def main():
    # Load input
    with open("example_input.txt", "r") as f:
        text = f.read()

    sentences = [s.strip() for s in text.split(".") if s.strip()]
    
    # Load Azure config
    endpoint, key = load_config()

    # Choose analyzer
    if endpoint and key:
        flagged = analyze_sentiment_azure(sentences, endpoint, key)
    else:
        flagged = analyze_sentiment_mock(sentences)

    # Write results
    with open("cleaned_output.txt", "w") as out:
        for sentence in sentences:
            if any(sentence == flagged_s for flagged_s, _ in flagged):
                out.write("[REDACTED - NEGATIVE SENTENCE]\n")
            else:
                out.write(sentence + ".\n")

    print(f"\n✅ Done! {len(flagged)} negative sentence(s) flagged.")
    print("Filtered output written to: cleaned_output.txt")


if __name__ == "__main__":
    main()

