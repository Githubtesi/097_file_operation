# ----------------------------
# 097 ファイルパス
# os オペレーティングシステム
# https://docs.python.org/ja/3/library/os.html#module-os
# pathlib ブジェクト指向のファイルシステムパス
# https://docs.python.org/ja/3/library/pathlib.html
# shutil 高水準のファイル操作
# https://docs.python.org/ja/3/library/shutil.html
# glob Unix 形式のパス名
# https://docs.python.org/ja/3/library/glob.html
# ----------------------------
import contextlib
import glob
import pathlib
import shutil

print("---- 097 ファイルパス ----")
# 01.  exist or not
import os

# ファイルが存在するか
is_exist = os.path.exists("test.txt")
is_dir_exist = os.path.isdir("test")
is_file_exist = os.path.isfile("test.txt")

# 02. rename 名前変更
try:
    os.rename("renamed.txt", "renamed2.txt")
except FileNotFoundError as exc:
    print("renamed.txt がない")
except FileExistsError as exc:
    print("renamed2.txt がある")

# 03. short_cut の作成
try:
    os.symlink("renamed.txt", "renamed2.txt")
except FileNotFoundError as exc:
    print("renamed.txt がない")
except FileExistsError as exc:
    print("renamed2.txt がある")

# 04. create directory
try:
    os.mkdir("test_dir")
except FileExistsError:
    print("すでにtest_dirがあります")

# ex) create directry エラー無視
main_home = pathlib.Path(__file__).parent
folder_name = "lesson_package"
folder_path = os.path.join(main_home, folder_name)
with contextlib.suppress(FileExistsError):
    os.mkdir("lesson_package")

# 05. remove directroy
os.rmdir("test_dir")
shutil.rmtree("test_dir")

# 06.create file
pathlib.Path("empty.txt").touch()

# 07. remove file
os.remove("empty.txt")

# 08.file list
# ファイル一覧の取得
path = r"C:\Users\yoshiaki"
file_list = os.listdir(path)

# 　特定ファイルの取得
matched_list = glob.glob(path + "\\" + "*.bat")

#  全てのファイルパスを取得
all_list = glob.glob(r"C:\Users\yoshiaki\**", recursive=True)

# 09. copy
# folderAの中にa.pyがコピー
shutil.copy('a.py', 'folderA')

# 10. get 相対パス
os.getcwd()

# 11. change dir
os.chdir("git_tutorial")

# main file path
# 相対パス
print(__file__)

# 実行ファイルの親フォルダ
print(pathlib.Path(__file__).parent)

# 子フォルダのパス作成
file_path = os.path.join(dir_path, file_name)
