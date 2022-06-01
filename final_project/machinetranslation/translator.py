import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('VppD33oxV0IcoCnsj7NAN01VYCJeZrYujSoJ967yjFTJ')
language_translator = LanguageTranslatorV3(
    version='2022-05-30',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/c9456c2c-d9e4-42b8-9e91-d95414c422ff')

def english_to_french(english_text):
    french_text = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    english_text = language_translator.translate(text=french_text, model_id="fr-en").get_result()
    return english_text.get('translations')[0].get('translation')
    
