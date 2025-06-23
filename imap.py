import imaplib

# Configuration (Gmail example)
IMAP_SERVER = "imap.gmail.com"
EMAIL_USER = "chkavyaa123@gmail.com"
EMAIL_PASS = "yntj nmpy msrd yzdz"  # Use an App Password if 2FA is enabled

try:
    # Connect to the server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)

    # Login
    mail.login(EMAIL_USER, EMAIL_PASS)

    # Select the inbox
    mail.select("inbox")

    print("✅ Connected to email server and inbox selected.")

    # Example: check how many emails are there
    status, messages = mail.search(None, "ALL")
    print(f"Total emails: {len(messages[0].split())}")

    # Always logout when done
    mail.logout()

except imaplib.IMAP4.error as e:
    print(f"❌ IMAP connection failed: {e}")
