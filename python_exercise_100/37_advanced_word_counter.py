def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text =  text.replace(",", " ")
    text_list = text.split(" ")
    return len(text_list)

print(count_words(r"C:\Users\tbansal\Downloads\words2.txt"))