from setuptools import setup, find_packages
from polygmsh import __version__


setup(
    name='polygmsh',
    version=__version__,
    packages=find_packages(),
    install_requires=[
            'geoscr',
            'click'
        ],
    entry_points={
        'console_scripts': [
                'polygmsh = polygmsh.core:cli'
            ]
    },
)
