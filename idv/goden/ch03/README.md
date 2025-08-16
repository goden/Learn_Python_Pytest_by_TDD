# Setup&Teardown of Pytest
## Using xUnit-Style Setup/Teardown Functions
Pytest also supports xUnit-style setup and teardown functions, which are named conventions within test modules or classes.

### Concept
`setup` and `teardown` is common to execute the initialization before test and cleanup after test. This reduces the duplicate code and keep your code clean. 

### Scope
#### Module-level:
- def **setup_module(module)**: runs once before all tests in the module.
- def **teardown_module(module)**: runs once after all tests in the module.

#### Class-level:
- def **setup_class(cls)**: runs once before all tests in the class.
- def **teardown_class(cls)**: runs once after all tests in the class.

#### Method-level (within a class):
- def **setup_method(self, method)**: runs before each test method in the class.
- def **teardown_method(self, method)**: runs after each test method in the class.

```python
class TestExample:
    def setup_class(cls):
        print("\nSetup Class: Before all tests in the class")

    def teardown_class(cls):
        print("Teardown Class: After all tests in the class")

    def setup_method(self, method):
        print(f"Setup Method: Before {method.__name__}")

    def teardown_method(self, method):
        print(f"Teardown Method: After {method.__name__}")

    def test_one(self):
        print("Running test_one")
        assert True

    def test_two(self):
        print("Running test_two")
        assert False
```
Run the `pytest -rP <test_path>` to run the tests in chapter3. 
This prints the messages during the test execution.