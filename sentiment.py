
from enum import Enum
import pytest
import enum
from typing import List
import re
from collections import Counter

class Expression(enum.Enum):
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"
    NEUTRAL = "NEUTRAL"


def sentiment_analyzer(text:str):
    wordList = ["sad","terrible","angry","mad","bad","ugly","awful","stupid"]
    total_text = len(text)
    print(total_text)
    text_list = re.split('[ !.,]', text.lower())
    text_dict = dict(Counter(text_list))
    new_text_dict = {}
    score = 0
    total = 0
    word_in_list_size = 0
    
    for key, value in text_dict.items():
        if len(key) >= 3:
            new_text_dict[key] = value

    for key,value in new_text_dict.items():
        word_in_list_size += value

    for key, value in new_text_dict.items():
        if key in wordList:
            total += value

    score = (total / word_in_list_size) * 100
    print(score)
    print(total)
    
    if score >= 20: # >=20% -> NEGATIVE
        return Expression.NEGATIVE.name
    if score <= 5: # <=5% -> POSITIVE
        return Expression.POSITIVE.name
    if score > 5 and score < 20: # 5-20% -> NEUTRAL
        return Expression.NEUTRAL.name
    
    return -1


print(sentiment_analyzer(""))