import os

dir_path = "C:\practice\AtCoder\practice"

files = os.listdir(dir_path)

print(type(files))

for i in files:
    print(i)
    oldfliename = i 
    pyname = i + ".py"
    filename = i.split("_")[0]

    print(oldfliename)
    print(pyname)
    print(filename)

    try:
        new_dir_path = 'C:/practice/AtCoder/practice/' + filename
        os.mkdir(new_dir_path)
        path1 = f"practice/{i}/main.py"
        path2 = f"practice/{filename}/{pyname}"
        # ファイル名の変更 
        os.rename(path1, path2) 
        os.rmdir('C:/practice/AtCoder/practice/' + oldfliename)
    except FileExistsError:
        try:
                path1 = f"practice/{i}/main.py"
                path2 = f"practice/{filename}/{pyname}"
                # ファイル名の変更 
                os.rename(path1, path2) 
                os.rmdir('C:/practice/AtCoder/practice/' + oldfliename)
        except FileNotFoundError:
            print("エラー:" + filename)