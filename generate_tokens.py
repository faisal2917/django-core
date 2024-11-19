from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# Replace with your credentials from the Google Cloud Console
client_id = '1033878212692-f3p3ed15ulee17j78emhhuend9rbra08.apps.googleusercontent.com'
client_secret = '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'

# OAuth2 scope for Gmail
SCOPES = ['https://mail.google.com/']

def main():
    flow = InstalledAppFlow.from_client_config({
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token"
        }
    }, SCOPES)

    creds = flow.run_local_server(port=0)

    # Save the credentials for reuse
    with open("token.pkl", "wb") as token_file:
        pickle.dump(creds, token_file)

    print("Access Token:", creds.token)
    print("Refresh Token:", creds.refresh_token)

if __name__ == '__main__':
    main()
