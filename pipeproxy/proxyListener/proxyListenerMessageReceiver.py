import multiprocessing
from pipeproxy.proxyMessages.requestMessage import RequestMessage, NullRequestMessage


class ProxyListenerMessageReceiver:
    def __init__(self, pipeConnection):
        # type: (multiprocessing.Connection) -> None
        self.conn = pipeConnection

    def receive(self):
        # type: () -> RequestMessage
        if self.conn.poll(0.2):
            message = self.conn.recv()
            assert isinstance(message, RequestMessage)
            return message
        return NullRequestMessage()




