import multiprocessing
from pipeproxy.objectProxy.objectProxyMaker import ObjectProxyMaker
import unittest
from test_pipeproxy.testObject import TestObject, UnpickleableTestObject


class ObjectProxyMakerTest(unittest.TestCase):
    def test_make(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        testObject = TestObject()
        testObjectProxy = ObjectProxyMaker(testObject, parentConnection).make()

        assert hasattr(testObjectProxy, 'getParameter')
        assert hasattr(testObjectProxy, 'setParameter')

        assert callable(getattr(testObjectProxy, 'getParameter'))
        assert callable(getattr(testObjectProxy, 'setParameter'))

    def test_makeUnpickleableObject(self):
        parentConnection, childConnection = multiprocessing.Pipe()
        testObject = UnpickleableTestObject()
        testObjectProxy = ObjectProxyMaker(testObject, parentConnection).make()

        assert 1


