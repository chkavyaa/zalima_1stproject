# Step 1: Install pymupdf if not done yet
# pip install pymupdf

import fitz  # This is pymupdf

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        doc.close()
        return full_text
    except Exception as e:
        return f"Error: {e}"

# Example usage
pdf_path = r"C:\Users\chkav\OneDrive\test case\attachments\24TLME0040008069.pdf"  # Replace with your actual PDF file path
text = extract_text_from_pdf(pdf_path)
print(text)
