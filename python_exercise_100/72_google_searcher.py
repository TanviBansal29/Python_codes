import webbrowser

query = input("Enter your query: ")
webbrowser.open("https://google.com/search?q=%s" % query)