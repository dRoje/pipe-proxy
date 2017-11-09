from threading import Timer


class TestObject:
    def __init__(self):
        self.parameter = None

    def setParameter(self, parameter):
        print "setting parameter to: " + str(parameter)
        self.parameter = parameter

    def getParameter(self):
        print "getting parameter: " + str(self.parameter)
        return self.parameter


class UnpickleableTestObject:
    def __init__(self):
        self.unpickleableAttribute = Timer(1, self.method)

    def method(self):
        print "method was called"

    def startTimer(self):
        print "start timer"
        self.unpickleableAttribute.start()

