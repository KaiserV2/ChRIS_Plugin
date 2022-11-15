from setuptools import setup

setup(
    name='ChRIS_Plugin',
    version='1.0.0',
    description='A ChRIS plugin to do something awesome',
    author='FNNDSC',
    author_email='dev@babyMRI.org',
    url='https://github.com/KaiserV2/ChRIS_Plugin',
    py_modules=['commandname'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'commandname = commandname:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1',
            'pytest-mock~=3.8'
        ]
    }
)
