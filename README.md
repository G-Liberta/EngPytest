# Selenium-Pytest Automation Project

This project contains automated UI tests for the **[ENG Homepage](https://www.eng.it)** 
using **Selenium** with **Python** and **Pytest**. 


---

## Project Structure

The project is organized as follows:

- **pages/**: Contains Page Object Model (POM) classes for different pages under test.
- **tests/**: Contains test cases that use the POM classes to interact with the web pages.
- **requirements.txt**: Lists the dependencies needed to run the project.
- **config.py**: Project comon file to save various data that will be used among tc.
- **conftest.py**: Project common file where all test files can access the same fixture

---

## Requirements

Before running the tests, ensure the following prerequisites are met:

- Python 3.10+
- [Google Chrome](https://www.google.com/chrome/) browser
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (make sure it's added to the system's PATH)
- Jenkins (optional, for CI)

### Installing Dependencies

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```


### Setting up project

1. Clone the repository: git clone "url git repo"
2. Setup Chrome Driver. Ensure chromedriver.exe is in your system's PATH or provide the full path 
   in the test setup and the version of ChromeDriver matches your installed Chrome browser version.

   
---
### Future Enhancements
- Add More Test Coverage: Expand test cases to cover more aspects of the website.
- Pipeline as Code: Integrated with Jenkins for Continuous Integration (CI) for better scalability.
- Browser Compatibility: Add support for other browsers such as Firefox or Edge.
- Integrate with Allure: For enhanced reporting.
- Run Tests in Parallel: Speed up test execution by running tests in parallel.

---


### **Explanation of Key Sections**:

- **Project Structure**: Gives an overview of the file and folder layout.
- **Requirements**: Lists the software and dependencies needed to run the tests.
- **Future Enhancements**: Lists potential improvements to the testing and CI setup.

---

Would you like any specific sections modified or expanded? :)