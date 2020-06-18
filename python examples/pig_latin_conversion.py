def pig_latin(text):
    ls = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        ls.append("{}{}ay".format(word[1:], word[0]))
        # Turn the list back into a phrase
    return " ".join(ls)


print(pig_latin("hello how are you"))
