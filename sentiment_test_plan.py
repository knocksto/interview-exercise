import sys
import sentiment

from testplan import test_plan
from testplan.testing.multitest import MultiTest, testsuite, testcase


@testsuite
class SentimentTestSuite(object):

    @testcase
    def sentiment_analyis(self, env, result):
        result.equal(sentiment.sentiment_analysis("The world is a terrible place to live in. Terrible!"), "NEGATIVE", description='Passing assertion')
        
    @testcase
    def sentiment_return_type(self, env, result):
        result.true(isinstance(sentiment.sentiment_analysis("The boy is going to school"), str), description='check return type is String')

    @testcase
    def sentiment_analysis_with_no_param(self, env, result):
        with result.raises(TypeError):
            sentiment.sentiment_analysis()

@test_plan(name='Sentiment')
def main(plan):
    test = MultiTest(name='SentimentTest', suites=[SentimentTestSuite()])
    plan.add(test)

if __name__ == '__main__':
    sys.exit(not main())