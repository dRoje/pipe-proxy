# pipe-proxy

A sort-of-proxy solution for multiprocess communication using Pipe from mulitprocessing. 

## Description

This module is meant to be used when you need a proxy of an object that can be used in a different process.
<br>
Basically it means you can treat the proxy as if you have the original object in a different process. At least 
method calling. You don't have access to original object attributes (unless you write setters and getters). Also
all the parameters passed in the method calling must be picklable.
<br/> 
Why not use an already existing solution: https://docs.python.org/2/library/multiprocessing.html#proxy-objects ?
<br/>
Because I needed my proxy to be able to handle big objects with attributes that can't be pickled. This is a 
problem when using the solution from the multiprocessing module.

Read more about the package on this blog post:
http://matkodjipalo.com/index.php/2017/11/12/proxy-solution-python-multiprocessing/

### How to use it?

You call a method 'createProxy' from the pipeproxy.proxy module. You must also provide the object of which you want
the proxy to be created. (See Usage).
The method returns objects proxy and also it's proxy listener. The proxy has all the callable methods of the original
object. The proxy and proxy listener communicate using multiprocessing.Pipe.
<br/>
After calling the "createProxy" method you are left with three objects:
* original object
* proxy of the original object (with all the methods like the original)
* proxy listener

In the main process where you created these objects you keep the original object and the proxy listener. To the other
process you 'give' the proxy. (See example in Test)
<br/>

### How does it work?

Every time a method of proxy is called it is sent as a message threw the multiprocessing.Pipe to the proxy listener, who
then uses the original object to execute the actual method and respond back to the proxy with the return value of the 
method. Even arguments can be passed to the object as long as the can be pickled. 

<pre>
MAIN PROCESS                       |                    OTHER PROCESS
1. PROXY LISTENER      <-- message(someMethodName) <--       PROXY

2. PROXY LISTENER      
    - find method by name == "someMehtodName" in the original object
    - execute method
    - store return value
    
3. PROXY LISTENER      --> message(returnValue) -->         PROXY
</pre>


## Getting Started

### Prerequisites

Python 2.7


### Installing

Install package using pip:

```
pip install pipeproxy
```


### Usage

Import proxy python module:

```
from pipeproxy import proxy
```

Use 'createProxy' method for creating both object proxy and proxy listener:

```
proxy, proxyListener = proxy.createProxy(someObject)
```


## Test

```
from pipeproxy import proxy
from multiprocessing import Process
import time 


class Example:
    def __init__(self):
        self.parameter = None

    def setParameter(self, parameter):
        print "setting parameter to: " + str(parameter)
        self.parameter = parameter

    def getParameter(self):
        print "getting parameter: " + str(self.parameter)
        return self.parameter


def setParameterTest(exampleLookAlike):
    exampleLookAlike.setParameter(5)


def getParameterTest(exampleLookAlike):
    return exampleLookAlike.getParameter() == 1


example = Example()
exampleProxy, exampleProxyListener = proxy.createProxy(example)


# TEST 1
p = Process(target=setParameterTest, args=(exampleProxy,))
p.start()
time.sleep(1)
exampleProxyListener.listen()
assert example.getParameter() == 5

# TEST 2
p = Process(target=getParameterTest, args=(exampleProxy,))
p.start()
example.setParameter(1)
while exampleProxyListener.listen():
    pass

```

For extra testing a clone from github: https://github.com/dRoje/pipe-proxy.git <br/>
Run unittests in test_pipeproxy:

```
python -m unittest discover
```


## Authors

* **Duje Roje** - *Initial work* - [https://github.com/dRoje](https://github.com/dRoje)


## License

This project is licensed under the MIT License. 
Feel free to use it any way you want to.
