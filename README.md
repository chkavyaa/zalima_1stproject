                                              
  AUTOMATED INVOICE PROCESSING SYSTEM
  

This project automates the extraction of invoice information from PDF documents and email attachments. It collects, processes, and organizes invoice data into structured formats such as CSV for streamlined financial operations or audits.

FEATURES


- 📥 Fetch invoices from email (IMAP)
- 🔍 Extract and parse text from PDF invoices
- 🔎 Identify key fields (Invoice Number, Date, Vendor, Amount)
- 📤 Export structured data to CSV
- 🧾 Optional GUI and HTML view for results


  

 INSTALL REQUIRED LIBRARIES:



pip install -r requirements.txt

Make sure to include packages such as:
pandas

imaplib2 or imapclient

pdfplumber or PyMuPDF

tkinter (preinstalled with Python)

re (regular expressions)




Sample Output

Example structure of extracted_data.csv:

Invoice Number, Date, Vendor, Amount
INV-2345, 2025-06-20, Tech Supplies Inc., $1,250.00

🔐 Email Access Setup:

Ensure your email provider allows IMAP access and that credentials are securely stored (update imap.py or .env if used).
