import re
import os

def preprocess(input_file="blog.md", output_file="index.md"):
    def replacer(m):
        content = m.group(1)
        content = re.sub(r'(?<!\\)_', r'\\_', content)
        content = re.sub(r'\\{', r'\\\\{', content)
        content = re.sub(r'\\}', r'\\\\}', content)
        return "\\\\(" + content + "\\\\)"

    with open(input_file, "r") as f:
        data = f.read()
        data = re.sub(r'(?<!\$)\$([^\$]+)\$(?!\$)', replacer, data)

    with open(output_file, "w") as f:
        f.write(data)

if __name__ == "__main__":
    markdown_files = [f for f in os.listdir(".") if f.endswith(".md")]
    for f in markdown_files:
        preprocess(f, f)
        if f == "blog.md":
            preprocess(f, "index.md")
    print("Preprocessing done!")
