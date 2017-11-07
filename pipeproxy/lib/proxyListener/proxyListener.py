import multiprocessing
from pipeproxy.lib.proxyMessages.replyMessage import *
from pipeproxy.lib.proxyMessages.requestMessage import *
from proxyListenerMessageHandler import ProxyListenerMessageHandler
from proxyListenerMessageReceiver import ProxyListenerMessageReceiver
from proxyListenerMessageSender import ProxyListenerMessageSender


class ProxyListener:
    def __init__(self, pipeConnection, obj):
        # type: (multiprocessing.Connection, object) -> None
        self.messageReceiver = ProxyListenerMessageReceiver(pipeConnection)
        self.messageSender = ProxyListenerMessageSender(pipeConnection)
        self.functionHandler = ProxyListenerMessageHandler(obj)

    def listen(self):
        """Receive message request, handle and reply. NullRequestMessage means no message was received"""
        message = self.messageReceiver.receive()
        assert isinstance(message, RequestMessage)
        if not isinstance(message, NullRequestMessage):
            reply = self.functionHandler.handleReceivedMessage(message)
            assert isinstance(reply, ReplyMessage)
            self.messageSender.send(reply)
