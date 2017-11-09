from threading import Timer


class RealThing(object):
    def __init__(self):
        self.myValue = 0

    def myFunc(self):
        print "realThing func"

    def setValue(self, value):
        self.myValue = value

    def getValue(self):
        return self.myValue


class RealThingUnpickleable(object):
    def __init__(self):
        self.myValue = 0
        self.timer = None

