"""
pip install tkinter
pip install PyPDF2
pip install python-docx
pip install pypiwin32 pywin32   # 仅在 Windows 上
pip install PyMuPDF
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
from docx import Document
import os
import pythoncom
import win32com.client as win32  # 仅在 Windows 上


class FileConverter:
    def __init__(self, root):
        self.root = root
        root.title("文件转换器")

        self.filename = tk.StringVar()
        tk.Label(root, text="选择文件").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.filename, state='readonly', width=50).grid(row=0, column=1)
        tk.Button(root, text="浏览", command=self.load_file).grid(row=0, column=2)
        tk.Button(root, text="转换", command=self.convert_file).grid(row=1, columnspan=3)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx;*.doc")])
        self.filename.set(file_path)

    def convert_file(self):
        file_path = self.filename.get()
        if not file_path:
            messagebox.showwarning("警告", "请选择一个文件")
            return

        file_name, file_extension = os.path.splitext(file_path)
        if file_extension.lower() in ['.pdf']:
            self.pdf_to_word(file_path, file_name + '.docx')
        elif file_extension.lower() in ['.docx', '.doc']:
            self.word_to_pdf(file_path, file_name + '.pdf')
        else:
            messagebox.showwarning("警告", "不支持的文件格式")

    def pdf_to_word(self, pdf_file, word_file):
        try:
            doc = Document()
            pdf = fitz.open(pdf_file)

            for page in pdf:
                text = page.get_text()
                doc.add_paragraph(text)

            doc.save(word_file)
            messagebox.showinfo("成功", f"文件已保存到 {word_file}")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    def word_to_pdf(self, word_file, pdf_file):
        try:
            pythoncom.CoInitialize()
            word = win32.DispatchEx('Word.Application')
            doc = word.Documents.Open(word_file)
            doc.SaveAs(pdf_file, FileFormat=17)
            doc.Close()
            word.Quit()
            messagebox.showinfo("成功", f"文件已保存到 {pdf_file}")
        except Exception as e:
            messagebox.showerror("错误", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    converter = FileConverter(root)
    root.mainloop()
