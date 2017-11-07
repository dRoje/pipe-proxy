import multiprocessing
from pipeproxy.lib.proxyMessages.replyMessage import ReplyMessage


class ProxyListenerMessageSender:
    def __init__(self, pipeConnection):
        # type: (multiprocessing.Connection) -> None
        self.conn = pipeConnection

    def send(self, message):
        # type: (ReplyMessage) -> None
        self.conn.send(message)

