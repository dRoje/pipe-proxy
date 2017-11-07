import unittest
from pipeproxy.lib.proxyListener.proxyListenerMessageHandler import ProxyListenerMessageHandler
from pipeproxy.lib.proxyMessages.replyMessage import *
from pipeproxy.lib.proxyMessages.requestMessage import *
from test_pipeproxy.testObject import TestObject


class ProxyListenerMessageHandlerTest(unittest.TestCase):
    def test_handleCorrectReceivedMessage(self):
        testObject = TestObject()
        testObject.setParameter(1)
        proxyListenerMessageHandler = ProxyListenerMessageHandler(testObject)

        assert proxyListenerMessageHandler.handleReceivedMessage(RequestMessage('getParameter')) == ReplyMessage(1)

    def test_handleIncorrectReceivedMessage(self):
        testObject = TestObject()
        testObject.setParameter(1)
        proxyListenerMessageHandler = ProxyListenerMessageHandler(testObject)

        assert isinstance(proxyListenerMessageHandler.handleReceivedMessage(RequestMessage('something')),
                          ErrorReplyMessage)
