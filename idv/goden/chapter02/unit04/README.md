# Using Pytest Fixture
## Overview
Pytest fixtures are functions designed to provide a reliable and consistent baseline for tests to execute upon. They offer a structured way to manage the setup and teardown of resources, data, or state required by tests.

Key characteristics and benefits of pytest fixtures:
- **Explicit**<BR>Fixtures are explicitly declared and activated by tests, modules, classes, or even entire projects, making dependencies clear.
- **Modular**<BR>They are implemented as functions, allowing for the creation of reusable and composable setup routines. Fixtures can also utilize other fixtures, promoting a layered approach to test setup.
- **Scalable**<BR>Fixtures can be parameterized to handle various test scenarios and configurations. Their scope can be controlled (function, class, module, or session) to optimize resource usage and ensure test isolation.
- **Resource Management**<BR>Fixtures can handle the setup of resources like temporary files, database connections, or mock objects, and automatically manage their cleanup after tests complete.
- **Improved Readability and Maintainability**<BR>By centralizing setup logic within fixtures, test functions become cleaner and more focused on the actual test logic, leading to more readable and maintainable test suites.

## How to use
Follow the below steps:
- **Define a fixture:**<BR> A function is marked as a fixture using the `@pytest.fixture` decorator. 
```python
import pytest

@pytest.fixture
def my_fixture():
    # Setup code
    data = "some_data"
    yield data  # Provide the data to the test
    # Teardown code (executed after the test)
    print("Fixture teardown complete")
```

- **Use a fixture in a test:**<BR> A test function can consume a fixture by declaring its name as an argument. Pytest automatically injects the return value of the fixture into the test function.
```python
def test_using_fixture(my_fixture):
    assert my_fixture == "some_data"
```
- **Define is conftest.py**<BR> Fixtures can be defined in conftest.py files to make them available across multiple test files within a directory and its subdirectories.

## New Modules
Before starting the chapter 4, install the new modules that are used in this lessons.
```java
pip install fake-useragent requests
```
### fake-useragent
[fake-useragent](https://pypi.org/project/fake-useragent/) is up-to-date simple useragent faker with real world database.

### requests
[requests](https://pypi.org/project/requests/) is a simple, yet elegant, HTTP library.

Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!

Requests is one of the most downloaded Python packages today, pulling in around 30M downloads / week— according to GitHub, Requests is currently depended upon by 1,000,000+ repositories. You may certainly put your trust in this code.