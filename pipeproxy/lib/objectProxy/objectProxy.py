from pipeproxy.lib.proxyMessages.requestMessage import RequestMessage
from proxyMessenger.proxyMessageSender import ProxyMessageSender


class ObjectProxy:
    def __init__(self, proxyMessageSender):
        # type: (ProxyMessageSender) -> None
        """
        Has all the methods like the object that it is a proxy of. This must be ensured by the proxy maker.
        Difference is that methods that are called don't get executed, rather sent using the message sender.
        It is then up to the proxy listener to receive these methods (in a form of request message) and
        execute them as well as to reply with whatever a method returns (in a form of a reply message).
        :param proxyMessageSender: Object that takes care of the communication part.
        """
        self.proxyMessageSender = proxyMessageSender

    def sendMessage(self, functionName, args):
        """Creates a Request and sends it. Always expects a reply"""
        request = RequestMessage(functionName, args)
        reply = self.proxyMessageSender.sendMessage(request)
        return reply

    @classmethod
    def addMethod(cls, method, name):
        assert callable(method)
        setattr(cls, name, method)
