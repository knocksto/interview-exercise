
from enum import Enum
import enum
import math
from typing import List

import pytest
# from textblob import TextBlob
import re
from collections import Counter

class Expression(enum.Enum):
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"
    NEUTRAL = "NEUTRAL"

def sentiment_analyzer(text:str, wordList:List[str]):
    
    total_text = len(text)
    text_list = re.split('[ !.,]', text)
    text_dict = dict(Counter(text_list))
    new_text_dict = {}
    score = 0
    text_with_scores = {}
    
    for key, value in text_dict.items():
        if len(key) > 3:
            new_text_dict[key] = value

    for key, value in new_text_dict.items():
        if key in wordList:
            if value == 1:
                score = (value / total_text) * 100
                print(value)
                return Expression.POSITIVE.name
            if value > 1:
                text_with_scores[key] = value

    for key, value in text_with_scores.items():
        if value == 2:
            return Expression.NEUTRAL.name
        else:
            return Expression.NEGATIVE.name

    return -1
    
    # print(new_text_dict)
    # blob = TextBlob(text)
    # print(list(blob.sentiment)[0])
    # print(text_with_scores)


print(sentiment_analyzer("The world is a terrible place to live in terrible.", ["ugly","terrible"]))