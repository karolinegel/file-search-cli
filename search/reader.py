def read_file(filename):
    with open(filename) as f:
        return f.read()
def search_text(filename, text):
    content = read_file(filename)
    return text in content
