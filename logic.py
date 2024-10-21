import spacy

llm = spacy.load("en_core_web_lg")

def cemantix(secret_word, given_word, guessed_words=None):
    if guessed_words is None:
        guessed_words = []

    token_secret_word = llm(secret_word)
    token_given_word = llm(given_word)
    similarity = token_given_word.similarity(token_secret_word)

    guessed_words.append((given_word, similarity))

    return guessed_words, similarity


