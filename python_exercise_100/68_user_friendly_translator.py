d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocab(word):
    try:
        return d[word]
    except KeyError:
        return "We couldn't find the word..."

word = input("Enter the word: ").lower()

print(vocab(word))