from collections import Counter
import json

def count_characters(text):
    return dict(Counter(text))

# Example usage
if __name__ == "__main__":
    sample_text = "Hello, World!"
    result = count_characters(sample_text)
    print(json.dumps(result, indent=2))