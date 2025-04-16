"""
negativity_filter.py
---------------------
Scans input text and filters out sentences containing defined negative keywords or phrases.
This version does not use sentiment models — it is fully keyword-driven.
"""

def load_input_file(filename):
    """Load raw text from a file."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def write_output_file(sentences, flagged, output_file):
    """Write cleaned version of text with redacted flagged sentences."""
    with open(output_file, "w", encoding="utf-8") as f:
        for sentence in sentences:
            if sentence in flagged:
                f.write("[REDACTED - NEGATIVE CONTENT]\n")
            else:
                f.write(sentence + ".\n")


def extract_negativity(sentences, keyword_list):
    """Return sentences that contain any of the defined negative keywords or phrases."""
    flagged = []
    for sentence in sentences:
        lower = sentence.lower()
        if any(keyword in lower for keyword in keyword_list):
            flagged.append(sentence)
    return flagged


def main():
    # 🔹 Your keyword list — customize as needed
    negative_keywords = [
        "terrible service",
        "worst experience",
        "never coming back",
        "completely unacceptable",
        "rude staff",
        "they ignored",
        "not worth it",
        "your fault",
        "they didn't listen",
        "unhelpful"
    ]

    # 🔹 Load input
    text = load_input_file("example_input.txt")

    # 🔹 Break into sentences
    sentences = [s.strip() for s in text.split(".") if s.strip()]

    # 🔹 Filter by keywords
    flagged = extract_negativity(sentences, negative_keywords)

    # 🔹 Write filtered version
    write_output_file(sentences, flagged, "cleaned_output.txt")

    # 🔹 Summary
    print(f"✅ Done. {len(flagged)} sentence(s) flagged.")
    if flagged:
        print("\nFlagged content:")
        for s in flagged:
            print(f"- {s}")


if __name__ == "__main__":
    main()


