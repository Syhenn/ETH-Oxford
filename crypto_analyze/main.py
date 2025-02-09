from crypto_data import get_top_cryptos
from analyze import analyze_crypto_sentiment
from database import excecute
if __name__ == "__main__":
    crypto_list = get_top_cryptos()
    print("Liste des cryptos analysées :", crypto_list)

    tweet = "J’adore Bitcoin, c’est une révolution ! Par contre, Ethereum devient trop cher… "
    sentiment_scores = analyze_crypto_sentiment( crypto_list)

    print("Résultats d'analyse des sentiments :", sentiment_scores)
    excecute(sentiment_scores)
