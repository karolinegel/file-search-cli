from search.finder import find_files

def test_find_files():
    files = find_files(".")
    assert isinstance(files, list)
from search.finder import filter_by_extension

def test_filter():
    result = filter_by_extension(["a.py", "b.txt"], ".py")
    assert "a.py" in result
from search.reader import read_file

def test_read_file():
    with open("test.txt", "w") as f:
        f.write("hello")
    assert "hello" in read_file("test.txt")
