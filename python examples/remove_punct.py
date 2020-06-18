def remove_punctuation(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in punctuations:
        if char not in punctuations:
            no_punct = no_punct + char

    return no_punct
