import os
import re
import pdfplumber

# Extract text from PDF
def get_pdf_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text()
            return text
    except Exception as e:
        print(f"[ERROR] Could not read PDF: {e}")
        return ""

# Extract data using regex
def extract_invoice_data(text):
    invoice_no = re.search(r'Invoice\s*Number\s*[:\-]?\s*(\w+)', text, re.I)
    date = re.search(r'Date\s*[:\-]?\s*(\d{2}/\d{2}/\d{4})', text)
    amount = re.search(r'Total\s*[:\-]?\s*\$?([\d,]+\.\d{2})', text)
    vendor = re.search(r'From\s*[:\-]?\s*(.+)', text)

    return {
        'Invoice Number': invoice_no.group(1) if invoice_no else 'Not Found',
        'Date': date.group(1) if date else 'Not Found',
        'Amount': amount.group(1).replace(',', '') if amount else 'Not Found',
        'Vendor': vendor.group(1).strip() if vendor else 'Not Found'
    }

# Main logic
def main():
    folder = "attachments"

    if not os.path.exists(folder):
        print(f"[ERROR] Folder '{folder}' not found. Please create it and add PDF files.")
        return

    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder, filename)
            print(f"\nProcessing: {filename}")
            text = get_pdf_text(file_path)
            if not text:
                print("[WARNING] No text extracted.")
                continue

            data = extract_invoice_data(text)
            print("[INFO] Extracted Data:")
            for k, v in data.items():
                print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
