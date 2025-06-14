# import streamlit as st
# import fitz  # PyMuPDF
# from clause_detector import detect_clauses
# from summarizer import summarize_text
# from risk_evaluator import evaluate_risk
# from pdf_writer import create_pdf

# st.title("LexAI - Legal Document Reviewer")

# # Uploading file
# uploaded_file = st.file_uploader("Upload your document (.txt or .pdf)", type=["txt", "pdf"])

# # This will hold the extracted text
# text = ""

# if uploaded_file:
#     # Check if it's a PDF file
#     if uploaded_file.type == "application/pdf":
#         with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf:
#             for page in pdf:
#                 text += page.get_text()
#     else:
#         # If it's a plain text file
#         text = uploaded_file.read().decode("utf-8")

#     # Show document content
#     st.subheader("Document Preview")
#     st.text_area("Text Content", text, height=200)

#     if not text.strip():
#         st.error("The uploaded file has no readable content.")
#         st.stop()

#     # Summarize the document
#     st.subheader("Summary")
#     summary = summarize_text(text)
#     st.write(summary)

#     # Detect clauses
# st.subheader("Detected Clauses")

# clauses = detect_clauses(text)

# if clauses:
#     for clause, found in clauses.items():
#         if found:
#             st.success(f"✅ {clause} clause is Present")
#         else:
#             st.error(f"❌ {clause} clause is Missing")

#     # Evaluate risk and show score
#     st.subheader("Risk Evaluation")
#     result = evaluate_risk(text)
#     st.write(f"Document Score: {result['score']} / 100")

#     if result["missing_clauses"]:
#         st.write("Missing Clauses:")
#         for clause in result["missing_clauses"]:
#             st.write(f"- {clause}")
#     else:
#         st.write("All important clauses are present.")

#      # Generate PDF report
#     st.subheader("Generate PDF Report")
#     if st.button("Create PDF Report"):
#         pdf_buffer = create_pdf(summary, clauses, result["score"], result["missing_clauses"])
#         st.download_button(
#             label="Download PDF Report",
#             data=pdf_buffer,
#             file_name="LexAI_Report.pdf",
#             mime="application/pdf"
#         )

# this code is running correctly and generating the report of the document





# import streamlit as st
# import fitz  # PyMuPDF
# from clause_detector import detect_clauses
# from summarizer import summarize_text
# from risk_evaluator import evaluate_risk
# from pdf_writer import create_pdf

# st.title("LexAI - Legal Document Reviewer")

# # Uploading file
# uploaded_file = st.file_uploader("Upload your document (.txt or .pdf)", type=["txt", "pdf"])

# text = ""

# if uploaded_file:
#     # Extract text
#     if uploaded_file.type == "application/pdf":
#         with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf:
#             for page in pdf:
#                 text += page.get_text()
#     else:
#         text = uploaded_file.read().decode("utf-8")

#     if not text.strip():
#         st.error("The uploaded file has no readable content.")
#         st.stop()

#     # Show document content
#     st.subheader("Document Preview")
#     st.text_area("Text Content", text, height=200)

#     # Summarize the document
#     st.subheader("Summary")
#     summary = summarize_text(text)
#     st.write(summary)

#     # Detect clauses
#     st.subheader("Detected Clauses")
#     clauses = detect_clauses(text)

#     if clauses:
#         for clause, found in clauses.items():
#             if found:
#                 st.success(f"✅ {clause} clause is Present")
#             else:
#                 st.error(f"❌ {clause} clause is Missing")
#     else:
#         st.warning("No clauses were detected in the document.")

#     # Evaluate risk and show score
#     st.subheader("Risk Evaluation")
#     result = evaluate_risk(text)
#     st.write(f"Document Score: {result['score']} / 100")

#     if result["missing_clauses"]:
#         st.write("Missing Clauses:")
#         for clause in result["missing_clauses"]:
#             st.write(f"- {clause}")
#     else:
#         st.write("All important clauses are present.")

#     # Generate PDF report
#     st.subheader("Generate PDF Report")
#     if st.button("Create PDF Report"):
#         pdf_buffer = create_pdf(summary, clauses, result["score"], result["missing_clauses"])
#         st.download_button(
#             label="Download PDF Report",
#             data=pdf_buffer,
#             file_name="LexAI_Report.pdf",
#             mime="application/pdf"
#         )
# else:
#     st.info("Please upload a `.txt` or `.pdf` file to begin analysis.")
# # This is the main application file that integrates all components
# # and provides a user interface for document analysis.


# from flask import Flask, render_template, request, send_file
# import fitz  # PyMuPDF
# from io import BytesIO
# from clause_detector import detect_clauses
# from summarizer import summarize_text
# from risk_evaluator import evaluate_risk
# from pdf_writer import create_pdf

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     text = ""
#     summary = ""
#     clauses = {}
#     result = {}
#     filename = None
    
#     if request.method == "POST":
#         file = request.files["document"]
#         filename = file.filename
#         if filename.endswith(".pdf"):
#             with fitz.open(stream=file.read(), filetype="pdf") as pdf:
#                 for page in pdf:
#                     text += page.get_text()
#         elif filename.endswith(".txt"):
#             text = file.read().decode("utf-8")
#         else:
#             return render_template("index.html", error="Unsupported file type.")

#         if not text.strip():
#             return render_template("index.html", error="No readable content found.")

#         summary = summarize_text(text)
#         clauses = detect_clauses(text)
#         result = evaluate_risk(text)

#         return render_template("index.html", 
#                                text=text,
#                                summary=summary,
#                                clauses=clauses,
#                                result=result,
#                                filename=filename)

#     return render_template("index.html")


# @app.route("/download_report", methods=["POST"])
# def download_report():
#     summary = request.form["summary"]
#     score = request.form["score"]
#     missing_clauses = request.form.getlist("missing_clauses")
#     clauses = {clause: ("✅ Present" if request.form.get(clause) == "true" else "❌ Missing")
#                for clause in request.form.getlist("all_clauses")}

#     pdf_bytes = create_pdf(summary, clauses, int(score), missing_clauses)
#     return send_file(pdf_bytes, download_name="LexAI_Report.pdf", as_attachment=True)

# if __name__ == "__main__":
#     app.run(debug=True)







from flask import Flask, render_template, request, send_file
import fitz  # PyMuPDF
from io import BytesIO
from clause_detector import detect_clauses
from summarizer import summarize_text
from risk_evaluator import evaluate_risk
from pdf_writer import create_pdf

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    summary = ""
    clauses = {}
    result = {}
    filename = None

    if request.method == "POST":
        file = request.files["document"]
        filename = file.filename

        # Handle PDF files
        if filename.endswith(".pdf"):
            pdf_data = file.read()
            with fitz.open(stream=pdf_data, filetype="pdf") as pdf_file:
                for page in pdf_file:
                    text += page.get_text()

        # Handle plain text files
        elif filename.endswith(".txt"):
            text = file.read().decode("utf-8")

        else:
            return render_template("index.html", error="Unsupported file type. Please upload a .txt or .pdf file.")

        # Check if the extracted text is empty
        if not text.strip():
            return render_template("index.html", error="No readable content found in the uploaded document.")

        # Run all main processing steps
        summary = summarize_text(text)
        clauses = detect_clauses(text)
        result = evaluate_risk(text)

        # Send everything to frontend
        return render_template("index.html",
                               text=text,
                               summary=summary,
                               clauses=clauses,
                               result=result,
                               filename=filename)

    # Default page load (GET request)
    return render_template("index.html")


@app.route("/download_report", methods=["POST"])
def download_report():
    summary = request.form["summary"]
    score = request.form["score"]
    missing_clauses = request.form.getlist("missing_clauses")

    # Collect clause status values from form
    all_clauses = request.form.getlist("all_clauses")
    clauses = {}

    for clause in all_clauses:
        status = request.form.get(clause)
        if status == "true":
            clauses[clause] = "Present"
        else:
            clauses[clause] = "Missing"

    # Create PDF and send as download
    pdf_bytes = create_pdf(summary, clauses, int(score), missing_clauses)
    return send_file(pdf_bytes, download_name="LexAI_Report.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)

