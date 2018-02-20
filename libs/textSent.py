from google.cloud import language_v1
from google.cloud.language import enums
from google.cloud.language import types
from sys import maxunicode
import six

def __main__(text):
    """Detects entity sentiment in the provided text."""
    client = language_v1.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = {
        'type' : enums.Document.Type.PLAIN_TEXT,
        'content': text.encode('utf-8')
    }

    features = {
        "extractSyntax": False,
        "extractEntities": False,
        "extractDocumentSentiment": True,
        "extractEntitySentiment": False,
        "classifyText": False
    }

    # Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    response = client.annotate_text(document, features, encoding)

    return response