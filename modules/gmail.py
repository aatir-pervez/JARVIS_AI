import os
import base64
from email.mime.text import MIMEText
from core.speak import speak

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def read_emails():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)

        results = service.users().messages().list(userId="me", maxResults=5).execute()
        messages = results.get("messages", [])

        if not messages:
            speak("No new emails found")
            return

        speak("Reading your latest emails")

        for msg in messages:
            message = service.users().messages().get(userId="me", id=msg["id"]).execute()

            snippet = message.get("snippet", "")
            print("Email:", snippet)
            speak(snippet)

    except Exception as e:
        print("Gmail error:", e)
        speak("Error reading emails")