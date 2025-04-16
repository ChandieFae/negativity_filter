"""
tests.py
---------
Test suite for negativity_filter.py
Validates that keyword-based sentence filtering works as expected.
"""

from negativity_filter import extract_negativity

def test_extract_negativity_matches_expected_keywords():
    # Input sentences
    sentences = [
        "The worst company",
        "The service was terrible",
        "I'll never use them again",
        "That was the worst experience of my life",
        "Total rip off",
        "shouldnt be in business"
    ]

    # Define keywords used in the main script
    negative_keywords = [
        "terrible service",
        "worst experience",
        "bad",
        "worst staff",
        "rip off",
        "lawsuit",
        "not worth it",
        "your fault",
        "they are stupid",
        "useless"
    ]

    # Expected matches
    expected = [
        "That was the worst experience of my life",
        "They ripped us off"
    ]

    # Run the test
    flagged = extract_negativity(sentences, negative_keywords)

    assert flagged == expected, f" Expected {expected}, but got {flagged}"
    print("✅ test_extract_negativity_matches_expected_keywords passed.")


if __name__ == "__main__":
    test_extract_negativity_matches_expected_keywords()


