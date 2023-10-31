d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocab(word):
    try:
        return d[word]
    except KeyError:
        return "No data exists.."

word = input("Enter word: ")
print(vocab(word))