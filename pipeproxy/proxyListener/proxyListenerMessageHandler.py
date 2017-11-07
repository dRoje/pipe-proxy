from pipeproxy.proxyMessages.requestMessage import *
from pipeproxy.proxyMessages.replyMessage import *


class ProxyListenerMessageHandler:
    def __init__(self, obj):
        self.obj = obj

    def handleReceivedMessage(self, message):
        # type: (RequestMessage) -> ReplyMessage
        """
        Execute the method that corresponds with the function in the Request message.
        :return: Reply message containing return argument from the executed method.
        """
        assert isinstance(message, RequestMessage)
        function = message.getFunction()
        args = message.getArgs()
        # execute method and get return argument
        try:
            reply = getattr(self.obj, function)(*args)
            return ReplyMessage(reply)
        except AttributeError as e:
            # no wanted method to execute
            return ErrorReplyMessage(e.message)

