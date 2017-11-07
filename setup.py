from setuptools import setup

setup(name='pipeproxy',
      version='0.5',
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
                'pipeproxy.lib.proxyMessages'],
      # package_dir={'pipeproxy': 'lib'},
      zip_safe=False)
