"""
Basic Program that allows a user to input a list
Then will have the list displayed to them with commas between each
William Alber 9/30/2019
"""
listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words): ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)

for i in range(len(listToPrint)):
    if i == (len(listToPrint) - 1):
        print(", and " + listToPrint[i], end="")
    elif i == 0:
        print(listToPrint[i], end="")
    else:
        print(", " + listToPrint[i], end="")
