import imaplib
import email
from email.header import decode_header
import os
import getpass

IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "chkavyaa123@gmail.com"
SUBJECT_KEYWORD = "Invoice"
FOLDER_NAME = "attachments"


def download_attachments(mail):
    for part in mail.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        if filename:
            print(filename)
            filename = decode_header(filename)[0][0]
            print(f"Decoded filename: {filename}")
            if isinstance(filename, bytes):
                filename = filename.decode()
            if not filename.lower().endswith(".pdf"):
                continue
            print(f"Valid PDF attachment found: {filename}")
            filename = "".join(c if c.isalnum() or c in (' ', '.', '_') else "_" for c in filename)
            print(f"Cleaned filename: {filename}")
            filepath = os.path.join(FOLDER_NAME, filename)
            os.makedirs(FOLDER_NAME, exist_ok=True)

            if not os.path.isfile(filepath):
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                print(f"Downloaded: {filepath}")

def main():
    password = getpass.getpass(f"Enter app password for {EMAIL_ACCOUNT}: ")
    try:
        imap = imaplib.IMAP4_SSL(IMAP_SERVER)
        imap.login(EMAIL_ACCOUNT, password)
        print("Login successful.")
        imap.select("inbox")
        status, messages = imap.search(None, f'SUBJECT "{SUBJECT_KEYWORD}"')
        if status != "OK":
            print("No messages found.")
            return
        for num in messages[0].split():
            status, data = imap.fetch(num, "(RFC822)")
            if status != "OK":
                print(f"Failed to fetch email ID {num.decode()}")
                continue

            raw_email = data[0][1]
            mail = email.message_from_bytes(raw_email)
            print(f"Processing email with subject: {mail['Subject']}")
            download_attachments(mail)

        imap.close()
        imap.logout()

    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
