import glob

files = list(glob.glob("./abc*"))
text = """
# 問題リンクとフォルダの一覧

### テンプレート
```md
##
[問題]()
[フォルダ]()
```
"""
for i in range(len(files)):
    question_files = files[i]

    files_name = list(question_files.split(".\\"))[1]
    name_cut = list(files_name.split("_"))
    text += f"## {files_name}\n[問題](https://atcoder.jp/contests/{name_cut[0]}/tasks/{files_name})\n\n[フォルダ]({files_name})\n"

    with open ("README.md", "w", encoding= "utf-8") as f:
        f.write(text)
        