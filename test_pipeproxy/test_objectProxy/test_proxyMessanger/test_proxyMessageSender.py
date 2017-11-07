import multiprocessing
from pipeproxy.proxyMessages.replyMessage import *
from pipeproxy.proxyMessages.requestMessage import *
import time
from pipeproxy.objectProxy.proxyMessanger.proxyMessageSender import ProxyMessageSender
import unittest


class ProxyMessageSenderTest(unittest.TestCase):
    def sendMessageToPipe(self, conn, message):
        # type: (multiprocessing.Connection, str) -> None
        time.sleep(0.1)
        reply = ReplyMessage(message)
        conn.send(reply)

    def receiveMessageFromPipe(self, conn):
        # type: (multiprocessing.Connection) -> RequestMessage
        request = conn.recv()
        return request

    def test_noResponseTimeout(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        messageSender = ProxyMessageSender(parentConnection)

        assert messageSender.sendMessage(RequestMessage("request")) == NullReplyMessage()

    def test_sendingMessage(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        messageSender = ProxyMessageSender(parentConnection)
        messageSender.sendMessage(RequestMessage("request"))

        assert self.receiveMessageFromPipe(childConnection) == RequestMessage("request")

    def method(self):
        pass

    def test_passingUnpickleableParameter(self):
        from threading import Timer
        parentConnection, childConnection = multiprocessing.Pipe()
        messageSender = ProxyMessageSender(parentConnection)
        unpickleableAttribute = Timer(1, self.method)

        with self.assertRaises(TypeError):
            messageSender.sendMessage(RequestMessage("request", args=unpickleableAttribute))

    def test_sendAndReceiveMessage(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        messageSender = ProxyMessageSender(parentConnection)

        p = multiprocessing.Process(target=self.sendMessageToPipe, args=[childConnection, 'reply'])
        p.start()

        assert messageSender.sendMessage(RequestMessage("request")) == ReplyMessage("reply")



