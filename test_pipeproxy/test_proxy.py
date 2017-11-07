from pipeproxy import proxy
from testObject import TestObject
from pipeproxy.objectProxy.objectProxy import ObjectProxy
from pipeproxy.proxyListener.proxyListener import ProxyListener
from multiprocessing import Process
import time
import unittest


def setParameterTest(testObjectLookAlike):
    # type: (TestObject) -> None
    testObjectLookAlike.setParameter(5)


def getParameterTest(testObjectLookAlike):
    return testObjectLookAlike.getParameter() == 1


class ProxyTest(unittest.TestCase):
    def test_proxyCreate(self):
        testObject = TestObject()
        testObjectProxy, testObjectProxyListener = proxy.createProxy(testObject)

        assert isinstance(testObjectProxy, ObjectProxy)
        assert isinstance(testObjectProxyListener, ProxyListener)

    def test_proxySetParameter(self):
        testObject = TestObject()
        testObjectProxy, testObjectProxyListener = proxy.createProxy(testObject)
        p = Process(target=setParameterTest, args=(testObjectProxy,))
        p.start()
        time.sleep(1)
        testObjectProxyListener.listen()
        assert testObject.getParameter() == 5

    def test_proxyGetParameter(self):
        testObject = TestObject()
        testObjectProxy, testObjectProxyListener = proxy.createProxy(testObject)
        p = Process(target=getParameterTest, args=(testObjectProxy,))
        p.start()
        testObject.setParameter(1)
        while testObjectProxyListener.listen():
            pass


if __name__ == '__main__':
    unittest.main()
