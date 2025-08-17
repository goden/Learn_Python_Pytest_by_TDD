# Conftest.py of pytest
## Overview
In Pytest, conftest.py is a special file that serves as a local, per-directory plugin for managing and sharing test configurations, fixtures, and hooks. It is automatically discovered and loaded by Pytest when tests are run within its directory or any of its subdirectories.

## Key purposes
**Sharing Fixtures:**<BR>
The primary use of conftest.py is to define reusable fixtures that can be accessed by multiple test files within the same directory or its subdirectories without explicit imports. This promotes code reuse and simplifies test setup and teardown.

**Defining Hooks:**<BR>
conftest.py can be used to implement Pytest hooks, which are functions that allow you to customize various aspects of the test execution process, such as setup and teardown methods for tests or sessions.

**Loading External Plugins:**<BR>
While many Pytest plugins are automatically discovered, you can explicitly load external plugins or custom modules within conftest.py using pytest_plugins = ["plugin_name"].

**Managing Configurations:**<BR>
It can be used to set up global configurations or environment variables that are needed for your tests.

**Hierarchical Scope:**<BR>
You can have multiple conftest.py files in a project, each in a different directory. Fixtures and hooks defined in a parent conftest.py are available to child conftest.py files and their respective tests, allowing for modular and organized test setups. Child conftest.py files can also override fixtures or hooks defined in parent conftest.py files.



