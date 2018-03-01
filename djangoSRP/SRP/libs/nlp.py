from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
from google.protobuf.json_format import MessageToJson
from json import loads
from sys import maxunicode
from pathlib import WindowsPath
import six

def text_sentiment(text):
        creds_path = WindowsPath('c:\\Users\\maxmr\\Documents\\SRP\\djangoSRP\\SRP\\libs\\creds.json')
        credentials = service_account.Credentials.from_service_account_file(creds_path)
        """Detects entity sentiment in the provided text."""

        # Instantiates a client
        client = language.LanguageServiceClient(credentials=credentials)

        # The text to analyze
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Analyze the text
        analysis = client.analyze_sentiment(document=document)
        
        # Convert Result to JSON
        data = MessageToJson(analysis)
        data = loads(data)
        sentiment = analysis.document_sentiment
        sentences = data['sentences']

        return sentiment.score, sentiment.magnitude, sentences

def entity_sentiment_text(text):
    """Detects entity sentiment in the provided text."""
    credentials = service_account.Credentials.from_service_account_file('../../../creds/SRPConcAI-d1fac92d729b.json')
    client = language.LanguageServiceClient(credentials=credentials)

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    # Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    result = client.analyze_entity_sentiment(document, encoding)

    for entity in result.entities:
        print('Mentions: ')
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
            print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
            print(u'  Content : {}'.format(mention.text.content))
            print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
            print(u'  Sentiment : {}'.format(mention.sentiment.score))
            print(u'  Type : {}'.format(mention.type))
        print(u'Salience: {}'.format(entity.salience))
        print(u'Sentiment: {}\n'.format(entity.sentiment))

def syntax_text(text):
    """Detects syntax in the text."""
    credentials = service_account.Credentials.from_service_account_file('../../../creds/SRPConcAI-d1fac92d729b.json')
    client = language.LanguageServiceClient(credentials=credentials)

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    tokens = client.analyze_syntax(document).tokens

    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    for token in tokens:
        print(u'{}: {}'.format(pos_tag[token.part_of_speech.tag],
                               token.text.content))
