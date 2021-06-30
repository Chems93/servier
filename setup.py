from setuptools import setup, find_packages

setup(
    name='project',
    version='1.1',
    #packages=find_packages(),
    packages=['main', 'feature_extractor'],
    url='',
    license='',
    author='Chems',
    author_email='chems.rachdi@gmail.com',
    description='Servier',
    entry_points={
        'console_scripts': [
            'servier-predict = main.main:main',
        ],
    },
)
