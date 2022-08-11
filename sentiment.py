import string


negative_words = ["bad", "ugly", "terrible", "awful", "stupid", "mad", "angry", "sad"]
counter = 0

def sentiment_analysis(sentence: str) -> str:
    if calPercentage(sentence) <= 5:
        return "POSITIVE"
    elif calPercentage(sentence) < 20:
        return "NEUTRAL"
    else:
        return "NEGATIVE"

def negative_words_count(sentence: str) -> int:
    global counter
    split_sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split(" ")

    for neg_word in negative_words:
        for word in split_sentence:
            if neg_word == word:
                counter = counter + 1
    return counter
    
def calPercentage(sentence: str) -> int:
    split_sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split(" ")

    word_counter = sum(len(word) >= 3 for word in split_sentence)

    return negative_words_count(sentence) / word_counter * 100

if __name__ == '__main__':
    print(sentiment_analysis("I'm going shopping and I'm super excited. The terrible thing is that the boots I wanted are no longer in sale, which makes me a bit angry, because I now have to pay full price."))
