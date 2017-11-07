import multiprocessing
import pickle
from pipeproxy.proxyMessages.replyMessage import *
from pipeproxy.proxyMessages.requestMessage import *
import time


class ProxyMessageSender:
    def __init__(self, pipeConnection):
        # type: (multiprocessing.Connection) -> None
        self.conn = pipeConnection

    def sendMessage(self, request):
        # type: (RequestMessage) -> ReplyMessage
        """Sends a request message threw the pipe and immediately expects a response with a 2s timeout"""
        self._tryToPickle(request)  # object being sent threw pipe connection must be pickle-able
        self.conn.send(request)
        # always receive reply
        if self.conn.poll(2):
            reply = self.conn.recv()
            assert isinstance(reply, ReplyMessage)
            return reply
        else:
            print "Warning: no reply received for request (" + str(request) + ")"
            return NullReplyMessage()

    def _tryToPickle(self, obj):
        """Raises exception if not pickle-able"""
        pickle.dumps(obj)

