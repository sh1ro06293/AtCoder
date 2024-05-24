import os
url = input("URLを入力してください: ")
file_path = url.split("/")[-1]

if not os.path.exists(file_path):
    os.makedirs(file_path)
    f = open(f"{file_path}/main.py", "w")
    print("ファイルを作成しました")

    with open ("README.md", "a", encoding= "utf-8") as f:
        f.write(f"## {file_path}\n[問題]({url})\n\n[フォルダ]({file_path})\n")
    print("README.mdに追記しました")
else:
    print("ファイルが既に存在します")
