"test file to verify setup"
import sys 

def test_python_version():
    assert sys.version_info.major == 3 and sys.version_info.minor == 10
    print(f"Python version is {sys.version_info.major}.{sys.version_info.minor}") 

def test_playwright_import():
    import playwright
    print(f"Playwright imported successfully : {playwright}")   
    
def test_pytest_working():
    assert True
    print("Pytest is working correctly")