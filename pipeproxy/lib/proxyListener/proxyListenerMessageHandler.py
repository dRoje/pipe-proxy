from pipeproxy.lib.proxyMessages.replyMessage import *
from pipeproxy.lib.proxyMessages.requestMessage import *

import inspect

class WrongArgumentsError(Exception):
    pass


class MissingFunctionError(Exception):
    pass


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
        except AttributeError:
            raise MissingFunctionError("No function " + str(function) + " found in " + str(self.obj.__class__.__name__))
        except TypeError:
            functionSpecs = inspect.getargspec(getattr(self.obj, function)).args
            raise WrongArgumentsError(
                "Wrong arguments " + str(args) + " for '" + str(function) + "' in " + str(self.obj.__class__.__name__) + " expected: " + str(functionSpecs) )


