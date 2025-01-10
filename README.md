Amazon Website Crawling Automation

Overview
---------

This project involves creating Selenium automation scripts in Python to validate the Crawling functionality on the Amazon website. The objective is to ensure that the website's crawling feature works as expected under different scenarios.


Approach
---------

Understanding Requirements:

Reviewed the detailed instructions provided in the assessment document.

Focused on validating the website functionality with positive, negative, and edge test cases.

Setup:
---------

1) Utilized Selenium WebDriver with Python.

2) Structured the tests using the Pytest framework for easy scalability and maintainability.

3) Followed the Page Object Model (POM) design pattern to separate locators and actions from test scripts.

Test Cases:
--------------

**** Positive Test Cases ****:

1) Verify that a valid search term returns the expected results.

**** Negative Test Cases ****:

1) Check the behavior for invalid or random search terms.

**** Edge Test Cases ****:

1) Validate search with empty input.

2) Validate search with special characters.

Prerequisites
----------------
1) Python (version 3.7 or above)

2) Selenium (version 4.x)

3) Pytest (version 7.x)    

4) Latest version of GeckoDriver installed and that it matches your Firefox browser version.

5) Install pytest-html (for html report generation)

6) Install pytest-xdist for parallel testing

7) Install  openpyxl for excel reader

8) Pycharm Editor

Practices Followed:
----------------------

1) Used descriptive and modular functions for readability and reusability.

2) Implemented assertions to validate search results accurately.

3) Added explicit waits to ensure stability and avoid flaky tests.

4) Maintained logs for better debugging and tracking of test execution.

5) Included parameterized test cases for varied inputs.

6) Followed PEP8 coding standards for Python.


Tools & Frameworks:
---------------------
Tools : Selenium
Framework: Pytest


Running the Script:
----------------------
1) run test cases using Pytest:
   pytest -s -v .\testcases\qa_selenium_test.py

1) run parallel test case using pytest:
   Start the hub and node on your machine (I started hub and node on same machine)
   Keep the jar file and all the browser driver in same folder and run the below command from that folder
     java -jar selenium-server-<version>.jar  hub
     java -jar selenium-server-<version>.jar  node

    and after hub and node start then run below command on IDE terminal
       pytest -s -v .\testcases\<file.py>  -n <number of parallel process (e.g 2>

Assumptions:
--------------
1) All the search product, if its present in website then Test case will pass as expected and if it is not available then Test case will fail as expected.

