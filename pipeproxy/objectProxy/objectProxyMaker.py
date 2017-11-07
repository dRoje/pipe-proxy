from objectProxy import ObjectProxy
from proxyMessanger.proxyMessageSender import ProxyMessageSender
import multiprocessing


def proxyFunctionDecorator(function):
    assert callable(function)

    def wrapper(*args):
        instance = args[0]
        argsWithoutInstance = args[1:]
        assert isinstance(instance, ObjectProxy)
        instance.sendMessage(function.__name__, argsWithoutInstance)

    return wrapper


class ObjectProxyMaker:
    def __init__(self, obj, pipeConnection):
        # type: (obj, multiprocessing.Pipe) -> None
        self.obj = obj
        self.conn = pipeConnection

    def make(self):
        # type: () -> ObjectProxy
        # get all methods from obj
        for methodName in dir(self.obj):
            if not methodName.startswith('__') and callable(getattr(self.obj, methodName)):
                # decorate each method and add to ProxyObject
                actualObjectMethod = getattr(self.obj, methodName)
                decoratedMethod = proxyFunctionDecorator(actualObjectMethod)
                ObjectProxy.addMethod(decoratedMethod, methodName)

        return ObjectProxy(ProxyMessageSender(self.conn))
