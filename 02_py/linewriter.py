file_name = "fin_text.txt"
def writeTextToFile(plus_text):
    with open(file_name, "w") as fin_text:
        STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
        add_text = STATICKY_TEXT + str(plus_text)
        fin_text.write(add_text)
    return file_name