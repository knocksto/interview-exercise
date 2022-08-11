import sys

# from pywin.mfc.object import Object
from testplan import test_plan
from testplan.testing.multitest import MultiTest, testcase, testsuite
from sentiment import sentiment_analyzer


@testsuite
class SentimentTest(object):
    text = "The world is a ugly place to live in terrible. ugly! terrible"
    worldList = ["ugly"]

    @testcase
    def test_negative(self, env, result):
        result.equal(sentiment_analyzer("The world is a ugly place to live in ulgly. ugly! terrible", ["ugly"]), "NEGATIVE", description='Passing assertion')
        result.equal(sentiment_analyzer("The world is a ugly place to live in terrible. terrible", ["ugly"]), "POSITIVE", description='Failing assertion')


@test_plan(name='Sentiment')
def main(plan):
    test = MultiTest(name='SentimentTest', suites=[SentimentTest()])
    plan.add(test)


if __name__ == '__main__':
    sys.exit(not main)
