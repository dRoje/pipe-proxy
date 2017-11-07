import multiprocessing
import unittest
from pipeproxy.lib.proxyMessages.replyMessage import ReplyMessage
from pipeproxy.lib.proxyListener.proxyListenerMessageSender import ProxyListenerMessageSender


class ProxyListenerMessageSenderTest(unittest.TestCase):
    def receiveMessageFromPipe(self, conn):
        # type: (multiprocessing.Connection) -> ReplyMessage
        reply = conn.recv()
        return reply

    def test_send(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        messageSender = ProxyListenerMessageSender(parentConnection)
        messageSender.send(ReplyMessage(1))
        assert self.receiveMessageFromPipe(childConnection) == ReplyMessage(1)
