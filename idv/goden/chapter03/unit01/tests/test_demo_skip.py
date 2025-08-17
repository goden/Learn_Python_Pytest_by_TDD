import sys
import pytest

@pytest.mark.skip(reason="This is an example which always is skipped.")
def test_demo_skip():
    assert 2 == 1 + 1

@pytest.mark.skipif(
    condition=sys.platform == 'win32',
    reason="This is an example to skip by condition"
)
def test_demo_skipif():
    print(sys.platform)
    assert 2 == 1 + 1