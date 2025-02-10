import os

ROOT_DIR = "."
IGNORE_FILES = {"README.md"}

def get_markdown_files(root):
    """ 指定したディレクトリ内のMarkdownファイルを再帰的に取得 """
    md_files = []
    for dirpath, _, filenames in os.walk(root):
        for file in filenames:
            if file.endswith(".md") and file not in IGNORE_FILES:
                rel_path = os.path.relpath(os.path.join(dirpath, file), ROOT_DIR)
                md_files.append(rel_path.replace("\\", "/"))  # Windows対策
    return md_files

def generate_readme():
    """ Readme.md を生成する """
    md_files = get_markdown_files(ROOT_DIR)
    content = "# 記事一覧\n\n"

    category_map = {}
    for path in md_files:
        category, filename = os.path.split(path)
        if category not in category_map:
            category_map[category] = []
        category_map[category].append((filename, path))

    for category, files in sorted(category_map.items()):
        content += f"## {category}\n"
        for filename, path in sorted(files):
            content += f"- [{filename}]({path})\n"
        content += "\n"

    with open("Readme.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_readme()
