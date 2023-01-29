from setuptools import find_packages, setup


long_description = open('README.md').read()

setup(
    name='win32path',
    packages=find_packages(),
    version='0.1.0',
    description="Easy to use and can be imported and used in any Python project.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Emericdefay',
    license='MIT',
    install_requires=[],
    test_suite="tests",
)