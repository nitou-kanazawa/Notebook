import frontmatter # type: ignore
import os
import sys

def list_files_by_tag(directory, tag):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                    if tag in post.get("tags", []):
                        print(os.path.join(root, file))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("使用方法: python list_by_tag.py <ディレクトリ> <タグ>")
    else:
        list_files_by_tag(sys.argv[1], sys.argv[2])
