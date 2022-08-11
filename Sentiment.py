import re


# fileName = input("Please enter the text file:")

# Get words from the text file and remove words with less than 3 letters
def get_sentiment(file_name):
    negative_words = ["bad", "ugly", "terrible", "awful", "stupid", "mad", "angry", "sad"]
    file_negative_words = []

    final_words = []
    test_file = open(file_name, 'r')
    file_content = test_file.read()
    split_words = re.split(r'[.,!\s+]\s*', file_content)
    for word in split_words:
        if len(word) >= 3:
            final_words.append(word)
    total_word_count = len(final_words)
    print(final_words)
    print(total_word_count)

    for word in final_words:
        if word in negative_words:
            file_negative_words.append(word)

    negative_word_count = len(file_negative_words)
    sentiment_percentage = int((negative_word_count / total_word_count) * 100)

    if sentiment_percentage < 5:
        print("POSITIVE")
        # return "POSITIVE"
    elif sentiment_percentage > 20:
        print("NEGATIVE")
        # return "NEGATIVE"
    else:
        print("NEUTRAL")
        # return "NEUTRAL"

    print(file_negative_words)
    print(negative_word_count)
    print(sentiment_percentage)


if __name__ == '__main__':
    get_sentiment("testFile.txt")
