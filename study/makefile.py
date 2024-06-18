import os
url = input("URLを入力してください: ")
file_path = url.split("/")[-1]
folder_path = file_path.split("_")[0]
mondai = "/study/" + file_path.split("_")[1]

def make_file(folder_path, file_path, mondai):
    open(f"{folder_path}/{file_path}.py", "w")
    print("ファイルを作成しました")
    with open (f"{folder_path}/README.md", "a", encoding= "utf-8") as f:
        f.write(f"## [{mondai}問題]({url})\n\n")
    print("README.mdに追記しました")
    return  0

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("フォルダを作成しました")
    make_file(folder_path, file_path, mondai)
    open(f"{folder_path}/README.md", "w")

    
elif not os.path.exists(f"{folder_path}/{file_path}.py"):
    make_file(folder_path, file_path, mondai)

else:
    print("ファイルが既に存在します")
