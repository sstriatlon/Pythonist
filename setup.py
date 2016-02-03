try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'Pythonist',
    'author': 'Santiago Suarez',
    'url': 'https://github.com/sstriatlon/Pythonist.git',
    'download_url': 'https://github.com/sstriatlon/Pythonist.git',
    'author_email': 'sstriatlon@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Pythonist'
}


setup(**config)