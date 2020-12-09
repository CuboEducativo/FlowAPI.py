from distutils.core import setup


setup(
  name='flowapi',
  packages=['flowapi'],
  version='0.0.1',
  license='MIT',
  description='Use the Flow.cl\'s REST API without problems',
  author='Gabriel Pérez',
  author_email='gabriel@garox.org',
  url='https://github.com/cuboEducativo/FlowAPI.py',
  download_url='https://github.com/CuboEducativo/FlowAPI.py/\
      archive/0.0.2.tar.gz',
  keywords=['flow', 'api', 'py', 'flow.cl'],
  install_requires=[
          'requests',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
