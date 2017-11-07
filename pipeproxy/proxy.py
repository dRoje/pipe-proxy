from multiprocessing import Pipe

from lib.proxyListener.proxyListener import ProxyListener

from lib.objectProxy.objectProxyMaker import ObjectProxyMaker


def createProxy(obj):
    """ Create a multiprocessing Pipe connection ends. Create Proxy and ProxyListener connecting threw the Pipe"""
    parentConnection, childConnection = Pipe()

    objectProxy = ObjectProxyMaker(obj, childConnection).make()
    proxyListener = ProxyListener(parentConnection, obj)

    return objectProxy, proxyListener
