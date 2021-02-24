"""Assert that a certain exception is raised:"""
# import pytest

# def f():
#     raise SystemExit(1)

# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()

# """Group multiple tests in a class"""
# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x

#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, "check")

"""Request a unique temporary directory for functional tests"""
def test_needs(tmpdir):
    print(tmpdir)
    assert 0

    