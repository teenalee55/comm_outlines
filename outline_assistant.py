
import streamlit as st
import fitz  # PyMuPDF
import os

# Define evaluation criteria
criteria = {
    "Attention Getter": "Does the introduction include a compelling attention getter?",
    "Reason to Listen": "Is there a clear reason for the audience to listen?",
    "Thesis Statement": "Is the thesis statement clearly stated and specific?",
    "Credibility": "Does the speaker establish credibility?",
    "Preview of Points": "Are three main points previewed in the introduction?",
    "Transitions": "Are transitions between sections logical and smooth?",
    "Development": "Are main points well-developed with supporting material?",
    "Conclusion Review": "Does the conclusion review the main points?",
    "Thoughtful Closing": "Is there a thought-provoking closing that refers back to the introduction?",
    "Citation Format": "Are references cited in APA/MLA format and listed alphabetically?",
    "Time Awareness": "Does the outline reflect awareness of the 4–6 minute time limit?",
    "Skill Demonstration": "Does the topic demonstrate a useful skill for the audience?",
    "Outline Format Compliance": "Does the outline follow the formal sentence outline format?"
}

# Evaluation function
def evaluate_outline(text):
    feedback = {}
    for key, description in criteria.items():
        feedback[description] = "✅ Present" if key.lower() in text.lower() else "⚠️ Missing or unclear"
    return feedback

# Streamlit app
st.title("Speech Outline Evaluation Assistant")
st.write("Upload your speech outline (PDF) to receive automated feedback based on the assignment requirements.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_outline.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract text from PDF
    doc = fitz.open("temp_outline.pdf")
    text = "
".join(page.get_text() for page in doc)
    doc.close()
    os.remove("temp_outline.pdf")

    # Evaluate the outline
    feedback = evaluate_outline(text)

    # Display feedback
    st.subheader("Evaluation Feedback")
    for desc, result in feedback.items():
        st.write(f"**{desc}**: {result}")

    # Suggestions
    st.subheader("Suggestions for Improvement")
    for desc, result in feedback.items():
        if "⚠️" in result:
            st.write(f"- Consider improving: {desc}")
else:
    st.info("Please upload a PDF file to begin evaluation.")
