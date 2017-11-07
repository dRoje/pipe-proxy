import multiprocessing
import time
import unittest
from pipeproxy.lib.proxyMessages.replyMessage import *
from pipeproxy.lib.proxyMessages.requestMessage import *
from pipeproxy.lib.proxyListener.proxyListener import ProxyListener
from test_pipeproxy.testObject import TestObject


class ProxyListenerTest(unittest.TestCase):
    def sendMessageToPipe(self, conn, message, *args):
        # type: (multiprocessing.Connection, str) -> None
        time.sleep(0.1)
        request = RequestMessage(message, args)
        conn.send(request)

    def receiveMessageFromPipe(self, conn):
        # type: (multiprocessing.Connection) -> ReplyMessage
        reply = conn.recv()
        return reply

    def test_listenWithReturnValue(self):
        testObject = TestObject()
        testObject.setParameter(1)

        parentConnection, childConnection = multiprocessing.Pipe()
        proxyListener = ProxyListener(parentConnection, testObject)

        p = multiprocessing.Process(target=self.sendMessageToPipe, args=[childConnection, 'getParameter'])
        p.start()

        time.sleep(0.2)
        proxyListener.listen()

        reply = self.receiveMessageFromPipe(childConnection)

        assert isinstance(reply, ReplyMessage)
        assert reply == ReplyMessage(1)

    def test_listenWithEmptyReturnValue(self):
        testObject = TestObject()
        parentConnection, childConnection = multiprocessing.Pipe()
        proxyListener = ProxyListener(parentConnection, testObject)

        p = multiprocessing.Process(target=self.sendMessageToPipe, args=[childConnection, 'setParameter', 1])
        p.start()

        time.sleep(0.2)
        proxyListener.listen()

        reply = self.receiveMessageFromPipe(childConnection)

        assert reply == NullReplyMessage()

    def test_listenWithNoReply(self):
        testObject = TestObject()
        parentConnection, childConnection = multiprocessing.Pipe()
        proxyListener = ProxyListener(parentConnection, testObject)

        proxyListener.listen()

        assert 1
