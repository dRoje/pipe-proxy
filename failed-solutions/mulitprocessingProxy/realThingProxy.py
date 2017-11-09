from multiprocessing.managers import NamespaceProxy


class RealThingProxy(NamespaceProxy):
    _exposed_ = ('__getattribute__', '__setattr__', '__delattr__', 'myFunc', "setValue", "getValue")

    def myFunc(self):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('myFunc')

    def setValue(self, value):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('setValue', args=[value])

    def getValue(self):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('getValue')


class RealThingUnpickleableProxy(NamespaceProxy):
    _exposed_ = (
        '__getattribute__', '__setattr__', '__delattr__')

