# # summarizer.py
# import streamlit as st
# from transformers import pipeline

# @st.cache_resource
# def load_summarizer():
#     return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# summarizer = load_summarizer()

# def summarize_text(text):
#     # Limit the input size to avoid model errors
#     max_words = 1024
#     words = text.split()
#     if len(words) > max_words:
#         text = " ".join(words[:max_words])

#     # Generate summary
#     summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

#     # Clean the result (basic formatting)
#     summary = summary.strip().replace("\n", " ").replace(" .", ".").replace(" ,", ",")
#     return summary


# if __name__ == "__main__":
#     with open("sample_contract.txt", "r") as file:
#         content = file.read()

#     result = summarize_text(content)
#     print("\nSummary of Document:\n")
#     print(result)

    #this code is running correctly and generating summary of the document


import spacy
from heapq import nlargest

# Load English model from spaCy
nlp = spacy.load("en_core_web_sm")

def summarize_text(text, max_sentences=5):
    doc = nlp(text)
    sentence_scores = {}
    
    # Calculate word frequency
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in nlp.Defaults.stop_words and word.is_alpha:
            word_frequencies[word.text.lower()] = word_frequencies.get(word.text.lower(), 0) + 1

    max_freq = max(word_frequencies.values(), default=1)
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / max_freq

    # Score each sentence
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word.text.lower()]

    # Pick top N scored sentences
    summary_sentences = nlargest(max_sentences, sentence_scores, key=sentence_scores.get)
    final_summary = " ".join([sent.text.strip() for sent in summary_sentences])

    return final_summary


