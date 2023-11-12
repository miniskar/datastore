This repository is imported from https://bitbucket.org/Geekdude/datastore

All credits goes to original Author: Aaron Young (https://github.com/Geekdude)


Container object for datasets

Dictionary-like object that exposes its keys as attributes.

```
>>> b = Bunch(a=1, b=2)
>>> b['b']
2
>>> b.b
2
>>> b.a = 3
>>> b['a']
3
>>> b.c = 6
>>> b['c']
6
```

## Development
Use

    pip3 install --user -e .

or

    python3 setup.py develop --user

to install the package in an "editable" mode for testing and development.

## Installation
Install the monitoring gui by first packaging the program as a python wheel and 
then instal the wheel using pip.

    python3 setup.py bdist_wheel
    pip3 install --user dist/<wheel_file>
