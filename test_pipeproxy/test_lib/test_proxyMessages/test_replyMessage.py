import unittest
from pipeproxy.lib.proxyMessages.replyMessage import *


class ReplyMessageTest(unittest.TestCase):
    def test_hasContent(self):
        reply = ReplyMessage(None)
        assert reply.hasContent() is False

        reply = ReplyMessage(1)
        assert reply.hasContent() is True

    def test_getContent(self):
        reply = ReplyMessage(1)
        assert reply.getContent() == 1


class NullReplyMessageTest(unittest.TestCase):
    def test_hasContent(self):
        reply = NullReplyMessage()
        assert reply.hasContent() is False

    def test_getContent(self):
        reply = NullReplyMessage()
        assert reply.getContent() is None






