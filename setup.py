from setuptools import find_packages, setup


setup(
    name='win32path',
    packages=find_packages(),
    version='0.1.0',
    description="The 'win32path' library is a simple Python library that \
provides CRUD (Create, Read, Update, Delete) methods for managing file paths\
on a Windows operating system. It stores the paths in a JSON file located at \
'%APPDATA%/Local/win32path/paths.json' and allows the user to easily add, \
retrieve, update and delete file paths using the provided methods. The library\
 is easy to use and can be imported and used in any Python project.",
    author='Emericdefay',
    license='MIT',
    install_requires=[],
    test_suite="tests",
)