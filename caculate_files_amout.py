import os
import tkinter as tk
from tkinter import filedialog, messagebox

def get_folder_structure(path):
    folder_structure = {}
    for root, dirs, files in os.walk(path):
        folder_structure[root] = {
            'sub_folders': dirs,
            'file_count': len(files)
        }
    return folder_structure

def calculate_and_display():
    folder_path = filedialog.askdirectory(title='选择路径')
    if not folder_path:
        return

    folder_structure = get_folder_structure(folder_path)
    deepest_folders = {k: v for k, v in folder_structure.items() if not v['sub_folders']}

    total_files = sum(v['file_count'] for v in deepest_folders.values())

    result_message = f"总文件数: {total_files}\n\n"
    for folder, info in deepest_folders.items():
        relative_path = os.path.relpath(folder, folder_path)
        result_message += f"{relative_path}: {info['file_count']} 文件\n"

    messagebox.showinfo("结果", result_message)

app = tk.Tk()
app.title("文件夹结构统计")

select_button = tk.Button(app, text="选择路径", command=calculate_and_display)
select_button.pack(pady=20)

app.mainloop()
