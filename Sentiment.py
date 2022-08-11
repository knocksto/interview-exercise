import re

# fileName = input("Please enter the text file:")

# Get words from the text file and remove words with less than 3 letters
def getSentiment(fileName):
    negative_words = ["bad", "ugly", "terrible", "awful", "stupid", "mad", "angry", "sad"]

    finalWords = []
    test_file = open(fileName, 'r')
    file_content = test_file.read()
    splitWords = re.split(r'[.,!\s+]\s*', file_content)
    for word in splitWords:
        if len(word) >= 3:
            finalWords.append(word)
    print(finalWords)


if __name__ == '__main__':
    getSentiment("testFile.txt")

