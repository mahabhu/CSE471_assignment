# read the blog.md and for every $...$ block (but not $$..$$) replace with \(..\) block
# and write to index.md

import re

def preprocess():
    with open("blog.md", "r") as f:
        data = f.read()
        data = re.sub(
            r'(?<!\$)\$([^\$]+)\$(?!\$)',
            lambda m: "\\\\(" + re.sub(r'(?<!\\)_', r'\\_', m.group(1)) + "\\\\)",
            data
        )
        data = data.replace("\{", "\\{").replace("\}", "\\}")
    with open("index.md", "w") as f:
        f.write(data)

if __name__ == "__main__":
    preprocess()
