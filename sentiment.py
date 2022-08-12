import string

negative_words = ["bad", "ugly", "terrible", "awful", "stupid", "mad", "angry", "sad"]
counter = 0

def sentiment_analysis(sentence: str) -> str:
    global counter
    split_sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split(" ")

    for neg_word in negative_words:
        for word in split_sentence:
            if neg_word == word:
                counter = counter + 1

    word_counter = sum(len(word) >= 3 for word in split_sentence)

    neg_word_percentage = counter / word_counter * 100

    if neg_word_percentage <= 5:
        return "POSITIVE"
    elif neg_word_percentage < 20:
        return "NEUTRAL"
    else:
        return "NEGATIVE"

if __name__ == '__main__':
    print(sentiment_analysis(2))