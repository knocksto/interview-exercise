import sys

from testplan import test_plan
from testplan.testing.multitest import testsuite, testcase, MultiTest

from main import sentiment_analysis


@testsuite
class SentimentAnalysisSuite(object):

    @testcase
    def negative_sent_analysis(self, env, result):
        result.equal(sentiment_analysis("The world is a terrible place to live in. Terrible!"), "NEGATIVE",
                     description='Passing')
        result.ne(sentiment_analysis("The world is a terrible place to live in. Terrible!"), "POSITIVE",
                  description='Passing')
        result.ne(sentiment_analysis("The world is a terrible place to live in. Terrible!"), "NEUTRAL",
                  description='Passing')

    @testcase
    def test_positive_sentiment(self, env, result):
        result.equal(sentiment_analysis(
            "Today I saw a bunch of beautiful butterflies and they all looked so happy! All except for one that "
            "looked a bit sad and lonely."),
            "POSITIVE", description='Passing')

    @testcase
    def test_neutral_sentiment(self, env, result):
        result.equal(sentiment_analysis(
            "I'm going shopping and I'm super excited. The terrible thing is that the boots I wanted are no longer in "
            "sale, which makes me a bit angry, because I now have to pay full price."),
            "NEUTRAL", description='Passing')
        result.ne(sentiment_analysis(
            "I'm going shopping and I'm super excited. The terrible thing is that the boots I wanted are no longer in "
            "sale, which makes me a bit angry, because I now have to pay full price."),
            "POSITIVE", description='Passing')

    @testcase
    def test_no_spaced_text_excerpt(self, env, result):
        """ this is to test for the scenario where there's no space between two words separated by a comma.
             """
        result.equal(sentiment_analysis("I am mad,sad but smiling"), "NEGATIVE", description='Passing')

    @testcase
    def test_no_three_words(self, env, result):
        result.equal(sentiment_analysis("He no go go!"), "ALL WORDS ARE LESS THAN 3", description='Passing')

    @testcase
    def test_text_excerpt_is_empty_string(self, env, result):
        result.equal(sentiment_analysis(""), "ALL WORDS ARE LESS THAN 3", description='Passing')


@test_plan(name='Sentiment_Analysis')
def main(plan):
    test = MultiTest(name='Sentiment_Analysis_Test', suites=[SentimentAnalysisSuite()])

    plan.add(test)


if __name__ == '__main__':
    sys.exit(not main())
