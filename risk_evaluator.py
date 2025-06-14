# risk_evaluator.py

from clause_detector import detect_clauses
from clause_detector import CLAUSE_LABELS

def evaluate_risk(text):
    detected_clauses = detect_clauses(text)

    total_clauses = len(detected_clauses)
    present_clauses = sum(detected_clauses.values())
    missing_clauses = [clause for clause, present in detected_clauses.items() if not present]

    total_clauses = len(CLAUSE_LABELS)
    if total_clauses == 0:
        score = 0
    else:
        score = int((present_clauses / total_clauses) * 100)
    return {
        "score": score,
        "missing_clauses": missing_clauses,
        "detected_clauses": detected_clauses
    }


if __name__ == "__main__":
    with open("sample_contract.txt", "r") as file:
        text = file.read()

    result = evaluate_risk(text)

    print(f"Document Score: {result['score']}/100\n")
    print("Missing Clauses:")
    for clause in result['missing_clauses']:
        print(f"- {clause}")
