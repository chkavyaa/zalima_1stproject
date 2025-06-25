                                              
 # AUTOMATED INVOICE PROCESSING SYSTEM
  
# 1. Introduction
   
The Automated Invoice processing System automates the retrieval of invoice documents from email and extracts key invoice information such as invoice number, date, amount, and vendor name. The extracted data is exported into structured CSV files for further use in financial processes.




# 2. Objectives
   
- Automatically retrieve invoice attachments from emails

-  Extract text content from invoice PDFs

- Identify and parse invoice metadata

- Store extracted data in structured CSV

- Offer GUI and HTML viewing options



  
# 3. System Architecture


   
The system is built using modular Python scripts. Below are the components:


- Email Module (`imap.py`, `email_read.py`) – Fetches email attachments
  

- Extractor Module (`extract_text.py`) – Extracts raw text from PDFs
  

- Parser Module (`invoicenumber.py`) – Extracts structured fields using regex
  

- Export Module (`data_excel.py`) – Saves parsed data into CSV
  

- Interface (`tinker.py`, `here.html`) – GUI/HTML for user interaction
  

- Main Pipeline (`final.py`) – Runs the complete pipeline



  
# 4. Technology Stack

   
- Python 3.x
  

- pandas
  

- PyPDF2 / pdfplumber / fitz (PyMuPDF)
  

- imaplib / email
  

- tkinter (GUI)
  

- re, os, logging

  
# 5. How to Use

•	Install dependencies with `pip install -r requirements.txt`


•	Configure your email credentials in `imap.py`


•	Run `final.py` to execute the end-to-end process


•	View the output in `extracted_data.csv`


•	Optionally, run `tinker.py` for GUI or open `here.html` in a browser

 
 


# 6. Sample Output

    

A sample output CSV contains:


Invoice Number, Date, Vendor, Amount


INV-2025-001, 2025-06-21, Acme Supplies, $1,200.00



# 7.Future Enhancements
   
- Integrate OCR for scanned PDFs
  

- Use NLP for intelligent field extraction
  

- REST API or web dashboard
  

- Filter emails by subject/date/vendor

  
# 8. Conclusion

   
This system simplifies and accelerates the processing of invoice documents by eliminating manual entry.
The Invoice PDF Extraction System effectively automates the labor-intensive process of collecting, extracting, and organizing invoice data from emails and PDF attachments. By leveraging email integration, PDF parsing, and structured data export, it reduces human effort, minimizes errors, and accelerates financial workflows.
