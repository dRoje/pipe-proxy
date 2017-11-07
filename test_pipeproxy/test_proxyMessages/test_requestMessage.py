from pipeproxy.proxyMessages.requestMessage import *
import unittest


class ReplyMessageTest(unittest.TestCase):
    def test_getFunction(self):
        request = RequestMessage('someFunction', [1, 2])
        assert request.getFunction() == 'someFunction'

    def test_getArgs(self):
        request = RequestMessage('someFunction', [1, 2])
        assert request.getArgs() == [1, 2]


class NullReplyMessageTest(unittest.TestCase):
    def test_getFunction(self):
        request = NullRequestMessage()
        assert request.getFunction() == ''

    def test_getArgs(self):
        request = NullRequestMessage()
        assert request.getArgs() == ()




