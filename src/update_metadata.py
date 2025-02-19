import frontmatter
import os
import sys
from datetime import datetime

# 
def update_updated_at(file_path):
    with open(file_path, 'r+', encoding='utf-8') as f:
        post = frontmatter.load(f)
        post['updated_at'] = datetime.now().isoformat()
        f.seek(0)
        f.write(frontmatter.dumps(post))
        f.truncate()
    print(f"{file_path} の updated_at を更新しました")

# 
def main(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                update_updated_at(os.path.join(root, file))

if __name__ == "__main__":
    main(sys.argv[1])

