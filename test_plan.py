import sys

from testplan import test_plan
from testplan.testing.multitest import MultiTest, testsuite, testcase

from Sentiment import get_sentiment

@testsuite()
class BasicSuite(object):

    @testcase()
    def for_sentiment(self, env, result):
        result.equal(get_sentiment("testFile.txt"), "NEUTRAL", description='passing assertion')


@test_plan(name='Get_Sentiment')
def main(plan):
    test = MultiTest(name='GetSentimentTest', suites=[BasicSuite()])
    plan.add(test)

if __name__ == '__main__':
    sys.exit(not main())
