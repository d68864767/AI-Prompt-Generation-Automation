# qa_engineer.py

import pytest
from selenium import webdriver

class QAEngineer:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def run_unit_tests(self):
        pytest.main(["--verbose", "unit_tests.py"])
    
    def run_system_tests(self):
        pytest.main(["--verbose", "system_tests.py"])
    
    def run_user_acceptance_tests(self):
        self.driver.get("http://localhost:5000")
        # Implement user acceptance tests using Selenium
    
    def execute_testing(self):
        self.run_unit_tests()
        self.run_system_tests()
        self.run_user_acceptance_tests()

if __name__ == "__main__":
    qa_engineer = QAEngineer()
    qa_engineer.execute_testing()
