<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://github.com/Emericdefay/win32path/blob/main/com/logo.png?raw=true" alt="logo"></a>
</p>

<h3 align="center">Win32Path</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/emericdefay/win32path.svg)](https://github.com/emericdefay/win32path/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/emericdefay/win32path.svg)](https://github.com/emericdefay/win32path/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> The library is useful for managing and organizing file paths in a Windows environment.
    <br> 
</p>

<h2> Table of Contents</h2>

- [About ](#about-)
- [Getting Started ](#getting-started-)
  - [Installing](#installing)
    - [from Pypi](#from-pypi)
    - [from Github :](#from-github-)
- [Usage ](#usage-)
- [Authors ](#authors-)

##  About <a name = "about"></a>

The `win32path` library is a simple Python library that 
provides CRUD (Create, Read, Update, Delete) methods for managing file paths
on a Windows operating system. It stores the paths in a JSON file located at 
`%APPDATA%/Local/win32path/paths.json` and allows the user to easily add, 
retrieve, update and delete file paths using the provided methods. The library
is easy to use and can be imported and used in any Python project.

##  Getting Started <a name = "getting_started"></a>

Here is a list of each class and method, along with their docstrings in English:

- `obj.list_paths()`: Returns a list of all the registered paths.
- `obj.get_path(key)`: Returns the path associated with the specified key.
- `obj.set_path(key, value)`: Save the specified path for the specified key.
- `obj.update_path(key, value)`: Updates the path associated with the specified key.
- `obj.delete_path(key)`: Removes the path associated with the specified key.

### Installing

#### from Pypi

```
pip install win32path
```

#### from Github :

```
pip install git+https://github.com/Emericdefay/win32path
```

##  Usage <a name="usage"></a>

```python

        # define object
        >>> path = Win32Path()
        >>> the_key = 'key'
        >>> the_path = 'C:\\Users\\...\\Desktop'
        # set a path
        >>> path.set_path(the_key, the_path)

        # get a path
        >>> path.get_path(the_key)
        'C:\\Users\\...\\Desktop'

        # get all paths
        >>> win32path.list_paths()
        { 'key': 'C:\\Users\\...\\Desktop'}

        # update path
        >>> new_path = 'C:\\Users\\...\\Downloads'
        >>> path.update_path(the_key, new_path)

        # delete path
        >>> path.delete_path(the_key)
```

##  Authors <a name = "authors"></a>

- [@Emericdefay](https://github.com/Emericdefay) - Idea & Initial work

See also the list of [contributors](https://github.com/emericdefay/win32path/contributors) who participated in this project.
