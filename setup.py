try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'This is a Python translation of some useful problems from computational physics.',
        'author': 'Colin A. McFaul',
        'url': 'URL to get it.',
        'download_url': 'Where to download it.',
        'author_email': 'cmcfaul@tulane.edu',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'teaching'
        }

setup(**config)
