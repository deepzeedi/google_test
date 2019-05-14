# google_test
Test program which open GChrome send in form query and return results in console (optional).
***
The programm was test on Ubuntu v. 18.04, Chrome webbrowser v.74.
For launch programm you need to instal Selenium. 
To instal selenium run in terminal with pip:

    pip install selenium

To make possible launching GChrome on Linux x64 you need download webdriver (in the repository) and paste the path in 5 line:

    browser = webdriver.Chrome(executable_path='youre/webdriver/path')
    
Or Windows x64

    browser = webdriver.Chrome("C:\\your\\path\\to\\webdriver")

Possible problems:
- uncoding. Need to use UTF-8 encoding to launch programm.
- browser. I was use only GChrome.
