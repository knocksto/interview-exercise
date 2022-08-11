
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
    print(total_text)
    text_list = re.split('[ !.,]', text.lower())
    text_dict = dict(Counter(text_list))
    new_text_dict = {}
    score = 0
    expression_dectector = ""
    text_with_scores = {}
    
    for key, value in text_dict.items():
        if len(key) >= 3:
            new_text_dict[key] = value

    for key, value in new_text_dict.items():
        if key in wordList:
            score = (value / total_text) * 100
            print(score)
            print(value)
            if value >= 1 and score > 1:
                return Expression.NEGATIVE.name
            elif value and score >= 0.6:
                  return Expression.POSITIVE.name
            elif value and score <= 0.6:
                return Expression.NEUTRAL.name
    
    print(score)
    return -1


print(sentiment_analyzer("The world is a terrible place to live in. Terrible!", ["sad","terrible","angry","mad","bad","ugly","awful","stupid"]))