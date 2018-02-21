from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
from sys import maxunicode
import six

class TextSent():
    def textSent(self, text):
        
        credentials = service_account.Credentials.from_service_account_file('../creds/SRPConcAI-d1fac92d729b.json')
        """Detects entity sentiment in the provided text."""

        # Instantiates a client
        client = language.LanguageServiceClient(credentials=credentials)

        # The text to analyze
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        return sentiment.score, sentiment.magnitude