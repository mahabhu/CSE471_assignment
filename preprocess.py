# read the blog.md and for every $...$ block (but not $$..$$) replace with \(..\) block
# and write to index.md

import re

def preprocess():

    def replacer(m):
        content = m.group(1)
        content = re.sub(r'(?<!\\)_', r'\\_', content)
        content = re.sub(r'\\{', r'\\\\{', content)
        content = re.sub(r'\\}', r'\\\\}', content)
        return "\\\\(" + content + "\\\\)"

    with open("blog.md", "r") as f:
        data = f.read()
        data = re.sub(r'(?<!\$)\$([^\$]+)\$(?!\$)', replacer, data)

    with open("index.md", "w") as f:
        f.write(data)

if __name__ == "__main__":
    preprocess()
