import sys

from testplan import test_plan
from testplan.testing.multitest import MultiTest, testcase, testsuite
from sentiment import sentiment_analyzer


@testsuite
class SentimentTest(object):
    text = "The world is a ugly place to live in terrible. ugly! terrible"
    @testcase
    def test_sentiment(self, env, result):
        result.equal(sentiment_analyzer(self.text), "NEGATIVE", description='Passing assertion')
        result.equal(sentiment_analyzer(self.text), "POSITIVE", description='Failing assertion')


@test_plan(name='Sentiment')
def main(plan):
    test = MultiTest(name='SentimentTest', suites=[SentimentTest()])
    plan.add(test)


if __name__ == '__main__':
    sys.exit(not main)
