# clause_detector.py

# def detect_clauses(text):
#     clauses = {
#         "Confidentiality": ["confidential", "non-disclosure"],
#         "Termination": ["terminate", "termination", "end of agreement"],
#         "Governing Law": ["governing law", "jurisdiction", "laws of"],
#         "Non-Compete": ["non-compete", "competition", "compete"],
#         "Dispute Resolution": ["dispute", "arbitration", "mediation"]
#     }

#     found_clauses = {}

#     for clause_name, keywords in clauses.items():
#         found = False
#         for keyword in keywords:
#             if keyword.lower() in text.lower():
#                 found = True
#                 break
#         found_clauses[clause_name] = found

#     return found_clauses


# if __name__ == "__main__":
#     with open("sample_contract.txt", "r") as file:
#         document_text = file.read()

#     detected = detect_clauses(document_text)

#     print("Clause Detection Result:\n")
#     for clause, present in detected.items():
#         if present:
#             print(f"{clause}: Present")
#         else:
#             print(f"{clause}: Missing")






# clause_detector.py

# We are using a pre-trained AI model to detect important clauses in legal documents.
# This model is good at understanding the meaning of text (not just matching keywords).
# import streamlit as st
# from transformers import pipeline

# # These are the types of clauses we want to check in the document
# CLAUSE_LABELS = [
#     "Confidentiality",
#     "Termination",
#     "Governing Law",
#     "Non-Compete",
#     "Dispute Resolution",
#     "IP Ownership",            
#     "Jurisdiction",            
#     "Data Protection",         
#     "Force Majeure",           
#     "Liability Limitation"     
# ]

# # Load the AI model for zero-shot classification
# # It means: the model can match sentences to labels even if it wasn't trained on those labels
# @st.cache_resource
# def load_classifier():
#     return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# classifier = load_classifier()

# # This function will return which clauses are present or missing
# def detect_clauses(text):
#     # Check for empty or whitespace-only text
#     if not text or not text.strip():
#         return {}  # Return empty result safely

#     result = classifier(
#         text,
#         candidate_labels=CLAUSE_LABELS,
#         multi_label=True
#     )

#     clause_results = {}
#     for label, score in zip(result["labels"], result["scores"]):
#         clause_results[label] = score >= 0.5  # You can adjust threshold

#     return clause_results


# # If you run this file directly, it will read from sample_contract.txt and print the results
# if __name__ == "__main__":
#     with open("sample_contract.txt", "r", encoding="utf-8") as f:
#         text = f.read()

#     clauses = detect_clauses(text)

#     print("Clause Detection Result:\n")
#     for clause, found in clauses.items():
#         print(f"{clause}: {'Present' if found else 'Missing'}")





from transformers import pipeline

# These are the types of clauses we want to check in the document
CLAUSE_LABELS = [
    "Confidentiality",
    "Termination",
    "Governing Law",
    "Non-Compete",
    "Dispute Resolution",
    "IP Ownership",            
    "Jurisdiction",            
    "Data Protection",         
    "Force Majeure",           
    "Liability Limitation"     
]

# Load the AI model for zero-shot classification
classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-1")

# This function will return which clauses are present or missing
def detect_clauses(text):
    # Check for empty or whitespace-only text
    if not text or not text.strip():
        return {}  # Return empty result safely

    result = classifier(
        text,
        candidate_labels=CLAUSE_LABELS,
        multi_label=True
    )

    clause_results = {}
    for label, score in zip(result["labels"], result["scores"]):
        clause_results[label] = score >= 0.5  # Threshold can be tuned

    return clause_results
