try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Project',
    'author': 'Ankit Bhatnagar',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ankit.bhatnagar4@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'project1'
}

setup(**config)