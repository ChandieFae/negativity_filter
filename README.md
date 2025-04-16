# negativity_filter
This tool is designed to **detect and flag negative or accusatory content** in reviews, feedback, or other user-generated text.
# negativity_filter 🧹

A lightweight Python tool to **scan and redact negative or accusatory content** from written text using a **customizable keyword list** — no external APIs required.

---

## 🔍 What It Does

- Reads raw text input (e.g. reviews, feedback, or comments)
- Breaks it into sentences
- Flags sentences containing **predefined negative phrases**
- Outputs a redacted version of the original text with negative content removed

---

## ⚙️ How It Works

This project does **not** use a machine learning model.  
It uses **precise, keyword-based filtering** so you stay in control of what’s considered “negative.”

The keywords can be fully customized in `negativity_filter.py`.

---

## 📁 Project Structure

negativity_filter/ ├── negativity_filter.py # Core logic ├── example_input.txt # Example text to test filtering ├── cleaned_output.txt # Result after filtering ├── tests.py # Unit tests for filtering logic ├── requirements.txt # Dependencies (empty if no Azure) ├── azure_config.json # Placeholder (not needed unless using Azure) └── .gitignore # Ignores sensitive files

---

## 🚀 How to Use

1. Clone the repo:
```bash
git clone https://github.com/ChandieFae/negativity_filter.git
cd negativity_filter

python negativity_filter.py
Check cleaned_output.txt for the result.

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

python tests.py

🌱 Future Possibilities
Category-based tagging (anger, blame, etc.)

Azure AI or ML model integration (optional)

Rewrite/redraft suggestions instead of redactions

🧠 Author’s Note
This project is about clarity, intentional language, and content hygiene.
No AI black boxes — just real filters, made by real humans, for real use.

