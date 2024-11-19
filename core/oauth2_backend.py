import base64
from core.settings import *
import google.auth # type: ignore
from google.auth.transport.requests import Request # type: ignore
from django.core.mail.backends.smtp import EmailBackend
from google.oauth2.credentials import Credentials # type: ignore

class OAuth2EmailBackend(EmailBackend):
    def _get_oauth2_access_token(self):
        # Rebuild credentials from settings
        creds = Credentials(
            None,
            refresh_token=EMAIL_REFRESH_TOKEN, # type: ignore
            client_id=EMAIL_CLIENT_ID,
            client_secret=EMAIL_CLIENT_SECRET,
            token_uri="https://oauth2.googleapis.com/token",
        )
        creds.refresh(Request())
        return creds.token

    def _send(self, email_message):
        # Get the access token
        access_token = self._get_oauth2_access_token()

        # Add access token to the authentication process
        auth_string = f"user={EMAIL_HOST_USER}\1auth=Bearer {access_token}\1\1"
        self.connection.docmd('AUTH', 'XOAUTH2 ' + base64.b64encode(auth_string.encode()).decode())

        super()._send(email_message)
