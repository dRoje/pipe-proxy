from setuptools import setup

setup(name='pipeproxy',
      version='0.6',
      description='A sort-of-proxy solution for multiprocess communication using Pipe from mulitprocessing.',
      url='https://github.com/dRoje/pipe-proxy.git',
      author='Duje Roje',
      author_email='rojeduje@gmail.com',
      license='MIT',
      packages=['pipeproxy',
                'pipeproxy.lib',
                'pipeproxy.lib.objectProxy',
                'pipeproxy.lib.objectProxy.proxyMessanger',
                'pipeproxy.lib.proxyListener',
                'pipeproxy.lib.proxyMessages',

                'test_pipeproxy',
                'test_pipeproxy.test_lib',
                'test_pipeproxy.test_lib.test_objectProxy',
                'test_pipeproxy.test_lib.test_objectProxy.test_proxyMessanger',
                'test_pipeproxy.test_lib.test_proxyListener',
                'test_pipeproxy.test_lib.test_proxyMessages'],

      # package_dir={'pipeproxy': 'lib'},
      zip_safe=False)
