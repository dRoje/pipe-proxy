from pipeproxy.proxyMessages.requestMessage import *
from pipeproxy.proxyMessages.replyMessage import *
from pipeproxy.proxyListener.proxyListenerMessageHandler import ProxyListenerMessageHandler
import unittest
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
