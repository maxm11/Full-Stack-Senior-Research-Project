from watson-developer-cloud import ToneAnalyzerV3


def tone(text):
    tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='83ad76ab-4e48-48d9-b46f-0936f861d916',
    password='t7xG8mDnwZ8l'
    )

    tone = tone_analyzer(text, content_type='text/plain')

    print(tone)