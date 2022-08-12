negative_word_list = ["bad", "ugly", "terrible", "awful", "stupid", "mad", "angry", "sad"]


def sentiment_analysis(text_excerpt):
    # replace all punctuations with space and convert to list of words
    text_excerpt = text_excerpt.replace(" ", " ").replace(",", " ").replace(".", " ").replace("!", " ").lower().split()

    new_text_excerpt = [word for word in text_excerpt if len(word) >= 3]  # get rid of all words < 3,store in new list

    neg_word_count = [word for word in new_text_excerpt if word in negative_word_list]  # store all occurs of neg words

    try:
        sentiment_percentage = (len(neg_word_count) / len(new_text_excerpt)) * 100
    except ZeroDivisionError:
        return "ALL WORDS ARE LESS THAN 3"

    if sentiment_percentage <= 5:
        return "POSITIVE"
    elif sentiment_percentage >= 20:
        return "NEGATIVE"
    else:
        return "NEUTRAL"


if __name__ == '__main__':
    print(sentiment_analysis("The world is a terrible place to live in. Terrible!"))
