import multiprocessing
from pipeproxy.proxyMessages.requestMessage import RequestMessage, NullRequestMessage
from pipeproxy.proxyListener.proxyListenerMessageReceiver import ProxyListenerMessageReceiver
import unittest


class ProxyListenerMessageReceiverTest(unittest.TestCase):
    def sendMessageToPipe(self, conn, message, *args):
        # type: (multiprocessing.Connection, str) -> None
        request = RequestMessage(message, args)
        conn.send(request)

    def test_receiveMessageWithoutArgs(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        self.sendMessageToPipe(childConnection, "someMessage")
        messageReceiver = ProxyListenerMessageReceiver(parentConnection)
        receivedMessage = messageReceiver.receive()

        assert isinstance(receivedMessage, RequestMessage)
        assert receivedMessage == RequestMessage("someMessage")

    def test_receiveMessageWithArgs(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        self.sendMessageToPipe(childConnection, "someMessage", 1, 2)
        messageReceiver = ProxyListenerMessageReceiver(parentConnection)
        receivedMessage = messageReceiver.receive()

        assert isinstance(receivedMessage, RequestMessage)
        assert receivedMessage == RequestMessage("someMessage", args=tuple([1, 2]))

    def test_receiveNoMessage(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        messageReceiver = ProxyListenerMessageReceiver(parentConnection)
        receivedMessage = messageReceiver.receive()

        assert isinstance(receivedMessage, NullRequestMessage)

