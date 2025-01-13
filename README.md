### Amazon Website Crawling Automation

#### Overview
This project involves creating Selenium automation scripts in Python to validate the Crawling functionality on the Amazon website. The objective is to ensure that the website's crawling feature works as expected under different scenarios.

---

### Approach
- Reviewed the detailed instructions provided in the assessment document.
- Focused on validating website functionality with positive, negative, and edge test cases.
- Utilized Selenium WebDriver with Python.
- Structured the tests using the Pytest framework for scalability and maintainability.
- Followed the Page Object Model (POM) design pattern to separate locators and actions from test scripts.

---

### Prerequisites
1. **Python** (version 3.7 or above).
2. **Selenium** (version 4.x).
3. **Pytest** (version 7.x).
4. Latest version of **GeckoDriver** installed and match with your Firefox browser version.
5. Install `pytest-html` for HTML report generation.
6. Install `pytest-xdist` for parallel testing.
7. Use **PyCharm Editor** for development.

---

### Practices Followed
1. Used descriptive and modular functions for readability and reusability.
2. Implemented assertions to validate search results accurately.
3. Added explicit waits to ensure stability and avoid flaky tests.
4. Maintained logs for better debugging and tracking of test execution.
5. Included parameterized test cases for varied inputs.

---

### Tools & Frameworks
- **Tools:** Selenium
- **Framework:** Pytest

---

### Project Setup
1. **Clone the Repository:**
   git clone https://github.com/Sajjanrepo/AmazonEcommerce.git

2. Navigate to the project folder:
   cd <repository_folder>
   python -m venv venv
   source venv\Scripts\activate
   
4. Install the necessary Python dependencies:
   pip install -r requirements.txt
  

---

### Running the Script
1. **Run test cases using Pytest:(By default it will use firefox browser)**
   pytest -s -v .\testcases\<test_case_test.py>  --browser <browser_name>

2. **Run parallel test cases using Pytest:**
   - Start the hub and node on your machine (I ran both hub and node on the same machine).
   - Keep the Selenium JAR file and all browser drivers in the same folder.
   - Run the following commands from that folder:
     java -jar selenium-server-<version>.jar hub
     -In other terminal from same folder
           java -jar selenium-server-<version>.jar node

   - After starting the hub and node, execute the tests in parallel:
     pytest -s -v .\testcases\<file_test.py> -n <number of parallel processes (e.g., 2)> --browser <browser_name>

---

### Assumptions
1. If a search product is present on the website, the test case will pass as expected. If it is not available, the test case will fail as expected.

---

### Note
1. **Test Data:**
   - A CSV file is present in the `testdata` directory. This file contains the search terms and expected results.
   - Ensure the test data is structured for clarity and aligned with Amazon.in’s product search behavior.

2. **Enhancements:**
   - Include detailed comments in the CSV file for each test case.
   - Make the changes in conftest.py file for running test script for parallel testing (Just uncomment the commented line under browser and change the hub ip as per your hub)
   - Report will be generated with filename initials under reports directory
---

This project validates key functionalities of Amazon's search and crawling features, providing a robust and scalable automation testing framework using Python and Selenium.


