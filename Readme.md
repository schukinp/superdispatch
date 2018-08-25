# Test to rate books on goodreads.com

This is an automated test for registration on https://www.goodreads.com.com/ and rating of books

# File architecture and description

`conftest.py` set up file
 
`data.py` test data file


`elements.py` elements `set` module

`locators.py` elements location module

`pages.py` file with test methods

`requirements.txt` file with necessary libraries

`test_goodreads.py` file with test

# Preconditions

* [Python](https://www.python.org/) 3+
* Latest version of [chromedriver](http://chromedriver.chromium.org/downloads) for Chrome
* Latest [Chrome](https://www.google.com/chrome/) web browser
* Latest version of [pytest-selenium](https://pypi.org/project/pytest-selenium/) web driver for Python

# How to start

Install dependencies `pip3 install -r requirements.txt`

Example of launch on Linux, Python 3.6.5:
```
$ python test_goodreads.py
```
