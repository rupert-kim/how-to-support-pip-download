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