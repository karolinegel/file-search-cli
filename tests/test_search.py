from search.finder import find_files

def test_find_files():
    files = find_files(".")
    assert isinstance(files, list)
from search.finder import filter_by_extension

def test_filter():
    result = filter_by_extension(["a.py", "b.txt"], ".py")
    assert "a.py" in result
