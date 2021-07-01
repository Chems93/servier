from setuptools import setup, find_packages

setup(
    name='project',
    version='1.1',
    packages=find_packages(),
    #packages=['bin', 'lib'],
    url='',
    license='',
    author='Chems',
    author_email='chems.rachdi@gmail.com',
    description='Servier',
    entry_points={
        'console_scripts': [
            'servier-predict = bin.main:main',
            'train-evaluate = bin.train_evaluate:main',
            'predict = bin.predict:main'

        ],
    },
)
