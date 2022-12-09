# Your colleague has recently started ice-skating, and after an injury,
# has become obsessed with padding his clothes in order to prevent future injuries.
# His padding obsession has become so severe, that all the documents you write together must also be padded.
# For every sentence, each word must be padded with enough spaces on each side, such that each word has the
# same amount of characters in itself/either side, as the longest word in the sentence.
# 'let's pad this sentence'
# '  let's    pad    this  sentence'
"""
   loop through sentence
   check if the word is less than longest word
   if yes, find the difference in the length of words
   pad word with the difference and save in a new list
   """


def sentence_padding(sentence):
    sentence = sentence.split()

    largest_word_length = 0
    for word in sentence:
        if len(word) > largest_word_length:
            largest_word_length = len(word)

    new_word_list = []

    for word in sentence:
        if len(word) < largest_word_length:
            if (largest_word_length - len(word)) % 2 == 0:
                no_of_spaces_to_left = (largest_word_length - len(word))/ 2
                no_of_spaces_to_right = (largest_word_length - len(word)) / 2
            else:
                no_of_spaces_to_left = (largest_word_length - len(word)) // 2 + 1
                no_of_spaces_to_right = (largest_word_length - len(word)) // 2


            word = " " * int(no_of_spaces_to_left) + word + " " * int(no_of_spaces_to_right)

            new_word_list.append(word)
        else:
            new_word_list.append(word)

    return "".join(new_word_list)


if __name__ == '__main__':
    print(sentence_padding("let's pad this sentence"))

