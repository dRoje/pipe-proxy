import multiprocessing
import time
import unittest
from pipeproxy.lib.proxyMessages.replyMessage import *
from pipeproxy.lib.proxyMessages.requestMessage import RequestMessage
from pipeproxy.lib.objectProxy.objectProxy import ObjectProxy
from pipeproxy.lib.objectProxy.proxyMessanger.proxyMessageSender import ProxyMessageSender


class ObjectProxyTest(unittest.TestCase):
    def sendMessageToPipe(self, conn, message):
        # type: (multiprocessing.Connection, str) -> None
        time.sleep(0.1)
        reply = ReplyMessage(message)
        conn.send(reply)

    def receiveMessageFromPipe(self, conn):
        # type: (multiprocessing.Connection) -> RequestMessage
        request = conn.recv()
        return request

    def test_noReplyTimeout(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        objectProxy = ObjectProxy(ProxyMessageSender(parentConnection))

        assert objectProxy.sendMessage('someFunction', ()) == NullReplyMessage()

    def test_sendMessageNoArgs(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        objectProxy = ObjectProxy(ProxyMessageSender(parentConnection))
        objectProxy.sendMessage('someFunction', ())

        assert self.receiveMessageFromPipe(childConnection) == RequestMessage("someFunction")

    def test_sendMessageWithArgs(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        objectProxy = ObjectProxy(ProxyMessageSender(parentConnection))
        objectProxy.sendMessage('someFunction', tuple([1, 2]))

        assert self.receiveMessageFromPipe(childConnection) == RequestMessage("someFunction", tuple([1, 2]))

    def test_sendAndReceiveMessage(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        objectProxy = ObjectProxy(ProxyMessageSender(parentConnection))

        p = multiprocessing.Process(target=self.sendMessageToPipe, args=[childConnection, 'reply'])
        p.start()

        assert objectProxy.sendMessage('someFunction', ()) == ReplyMessage("reply")

    def methodForTesting(self):
        print "I am a test method"

    def test_addMethod(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        objectProxy = ObjectProxy(ProxyMessageSender(parentConnection))
        objectProxy.addMethod(self.methodForTesting, "testMe")
        objectProxy.testMe()








