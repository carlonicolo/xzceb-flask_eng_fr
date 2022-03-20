"""Module that connect to IBM Language Translator to provide text translation
languages translation available in this module:
1- English to French
2- French to English
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(englishtext):
    """function that take english text and translate it into french text
    Args:
        englishText (_type_): _description_
    Returns:
        str: frenchText
    """
    try:

        frenchtranslation = language_translator.translate(
            text=englishtext,
            model_id='en-fr'
        ).get_result()
        
        return frenchtranslation.get("translations")[0].get("translation")
    except ApiException as ex:
        return ex.message

def french_to_english(frenchtext):
    """function that take french text and translate it into english text
    Args:
        frenchText
    Returns:
        str: englishText
    """
    try:
        englishtranslation = language_translator.translate(
            text=frenchtext,
            model_id='fr-en'
        ).get_result()
        
        return englishtranslation.get("translations")[0].get("translation")
    except ApiException as ex:
        return ex.message
