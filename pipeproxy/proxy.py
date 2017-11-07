from objectProxy.objectProxyMaker import ObjectProxyMaker, ObjectProxy
from proxyListener.proxyListener import ProxyListener
from multiprocessing import Pipe


def createProxy(obj):
    """ Create a multiprocessing Pipe connection ends. Create Proxy and ProxyListener connecting threw the Pipe"""
    parentConnection, childConnection = Pipe()

    objectProxy = ObjectProxyMaker(obj, childConnection).make()
    proxyListener = ProxyListener(parentConnection, obj)

    return objectProxy, proxyListener
