import win32com.client
import pandas as pd

outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
inbox = outlook.GetDefaultFolder(6)  # "6" refers to the index of the inbox folder

# Get all emails in the inbox
emails = inbox.Items

# Restrict to emails with subject line containing "Screen"
restricted_emails = emails.Restrict("@SQL=urn:schemas:httpmail:subject LIKE '%SEDIT%'")

# Create a DataFrame of email properties

for email in restricted_emails:
    print(email.Subject)
    print(email.SentOn)

print(message.__dir__())