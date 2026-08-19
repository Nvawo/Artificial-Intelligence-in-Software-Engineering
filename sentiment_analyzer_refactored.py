#!/usr/bin/python3
"""
Sentiment Analysis Tool (Refactored)
Analyzes sentiment via API with environment auth & enhanced exception handling.
"""
import os
import requests
import sys

def analyze_sentiment(text):
    """
    Analyzes sentiment of text using Text Processing API.
    """
    url = "https://api.text-processing.com/api/sentiment/"

    # Securely retrieve API key from environment variables
    api_key = os.getenv("TEXT_PROCESSING_API_KEY")
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    payload = {"text": text}

    try:
        response = requests.post(url, data=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        label = data.get('label', 'neutral')

        if label == 'pos':
            return 'positive'
        elif label == 'neg':
            return 'negative'
        else:
            return 'neutral'

    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: Request timed out. Details: {e}", file=sys.stderr)
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: Could not connect to API server. Details: {e}", file=sys.stderr)
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}", file=sys.stderr)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        return None
    except (KeyError, ValueError) as e:
        print(f"Invalid response format: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./sentiment_analyzer.py <text>")
        sys.exit(1)

    sentence = " ".join(sys.argv[1:])
    result = analyze_sentiment(sentence)

    if result:
        print(result)
    else:
        sys.exit(1)
