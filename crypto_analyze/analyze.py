from transformers import pipeline
from deep_translator import GoogleTranslator
from extract import extraction
import re

sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def translate_to_english(text):
    return GoogleTranslator(source='auto', target='en').translate(text)

def extract_cryptos(tweet, crypto_list):
    found_cryptos = []
    for crypto in crypto_list:
        if re.search(r'\b' + re.escape(crypto) + r'\b', tweet, re.IGNORECASE):
            found_cryptos.append(crypto)
    return found_cryptos

def map_label_to_score(label, confidence):
    """Convertir le label du modèle en un score entre -1 et 1"""
    if label == "LABEL_0":
        return -confidence 
    elif label == "LABEL_1":
        return 0
    elif label == "LABEL_2":
        return confidence
    return 0

def analyze_crypto_sentiment( crypto_list):
    tweets = extraction()
     
    data = []  # Liste pour stocker les résultats sous forme de dictionnaire
    
    for tweet in tweets:
        translated_tweet = translate_to_english(tweet["Texte"])
        cryptos = extract_cryptos(translated_tweet, crypto_list)

        for crypto in cryptos:
            pattern = r"([^.,;!?]*\b" + re.escape(crypto) + r"\b[^.,;!?]*)"
            match = re.search(pattern, translated_tweet, re.IGNORECASE)

            if match:
                sub_sentence = match.group(0)
                sentiment_result = sentiment_pipeline(sub_sentence)[0]

                # DEBUG : Afficher le résultat du modèle
                print(f"🔍 Crypto: {crypto} | Texte analysé: {sub_sentence} | Résultat: {sentiment_result}")

                data.append({"Crypto": crypto, "Score": sentiment_result["score"]})



    return data