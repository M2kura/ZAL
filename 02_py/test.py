import linewriter

linewriter.writeTextToFile(float(input("Write your text: ")))
with open("fin_text.txt", "r") as check:
    point = check.readline()
print(point)