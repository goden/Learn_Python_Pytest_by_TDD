
# Understand the lifecycle of the setup and teardown

def setup_module():
    print('setup module')

def setup_function():
    print('setup function')

def test_add_numbers():
    assert 10 == 4 + 6


def teardown_function():
    print('teardown function')

def teardown_module():
    print('teardown module')
