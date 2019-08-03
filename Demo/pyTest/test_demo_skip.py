import pytest
# import sys


# @pytest.mark.skip(reason="not required for now")
# def test_demo_1():
#     assert True
#
# @pytest.mark.skipif(sys.version_info > (3,7),reason="requires python 3.6 or higher")
# def test_demo_2():
#     assert True
#
# def test_demo_3():
#     assert True


@pytest.mark.windows
def test_window_1():
    assert True


@pytest.mark.windows
def test_window_2():
    assert True


@pytest.mark.mac
def test_mac_1():
    assert True


@pytest.mark.mac
def test_mac_2():
    assert True



