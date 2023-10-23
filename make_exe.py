import os
import subprocess
import shutil

# 指定Python脚本的路径
python_script_path = 'caculator.py'

# 获取Python脚本的名字和目录
script_dir, script_name = os.path.split(python_script_path)
script_name_without_ext = os.path.splitext(script_name)[0]

# 创建一个与Python脚本名字相同的文件夹，用于保存exe文件
exe_dir = os.path.join(script_dir, script_name_without_ext)
os.makedirs(exe_dir, exist_ok=True)

# 构造PyInstaller命令
command = f'pyinstaller --onefile -n {script_name_without_ext} {python_script_path}'

# 使用subprocess来运行命令
subprocess.run(command, shell=True)

# 将生成的EXE文件移动到新创建的文件夹
shutil.move(os.path.join('dist', f'{script_name_without_ext}.exe'), exe_dir)