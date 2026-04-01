from search.finder import find_files

def test_find_files():
    files = find_files(".")
    assert isinstance(files, list)
