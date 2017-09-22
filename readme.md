## what is this project?
* this is the example for people who want to support pip download like a library in the project they made.

## how to support pip download?
* it is essential to have __setup.py__ and write some features in the file.
* below this is the __example of setup.py__

## Warning Point
* It can be there is the __same project name__, so __decide carefully.__
* when user who install your project through the __pip__, there are just designated directories on the __packages__ attributes in __setup.py__. Therefore, check the directories that you want to release.

```
from setuptools import setup


setup(
    name='project_name',
    version='0.0.1',
    description='illustrating how to make the project that people can download through the pip on the github',
    url='https://github.com/yoonsubKim/how-to-support-pip-download',
    author='rupert kim',
    author_email='my@rupert.in',
    license='MIT',
    install_requires=[
        'requests'
    ],
    packages=['packages']
)
```

## references
* https://docs.python.org/3.6/distutils/setupscript.html