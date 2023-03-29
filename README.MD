# Readme

## Require
 - Python 3 (new version)
 - Create environment on Windows using CMD(run as admin)
    + Install virtualenv
        $ python -m pip install --user virtualenv
    + Create a virtual environment
        $python -m venv venv
    + Activate a virtual environment
        $ .\venv\Scripts\activate
    + Leave the virtual environment
        $ deactivate

 - Install requirments.txt file
    $ pip install -r requirements.txt

 ## Run test
    - Browser list: Chrome, Edge, Firefox, Safari(Mac), Opera, Internet Explore. Default is Chrome
    - Run without pytest:
        $ pytest main.py --browser=<Browser Name>
    - Run with pytest
        $ pytest main.py

 ## Test Report
    - pytest-html, allure-pytest:
        $ pytest -v -s --alluredir=allure\allure-report --html=.\report\report.html main.py
    - Open allure
        $ allure serve <path allure-report folder>

## Discription
    - allure/allure report: Contain test result allure - It is created after run --alluredir=\allure-report
    - report/report.html: Contain test result is html file - It is created after run --html=.\report\report.html
    - data: Contain data as url, email,...
    - driver: Contain driver files: Chrome, Firefox, Edge, Opera, Internet Explore, Safari,...
    - manages/driverManages: Init browser
    - locators: Contain element locator: Id, Name, Css-selector, Class, Xpath,...
    - pages: Contain Object element
    - tests: Contain event, test case
    - conftest.py: config parameters for pytest (--browser)
    - main.py: Testsuite, executable file
    - requirments.txt: framework need to be install