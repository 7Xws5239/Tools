"""
pip install pandas matplotlib
"""
import tkinter as tk
from tkinter import messagebox
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 设置课程数量
NUM_COURSES = 5

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x300+500+200")  # 设置窗口大小并居中
        root.title("课程计时器")
        self.course_vars = [tk.IntVar() for _ in range(NUM_COURSES)]
        self.start_times = [None] * NUM_COURSES
        self.elapsed_times = [0] * NUM_COURSES
        self.running = [False] * NUM_COURSES
        
        for i in range(NUM_COURSES):
            tk.Checkbutton(root, text=f"第{i+1}节课", variable=self.course_vars[i]).grid(row=i, column=0)
            tk.Button(root, text="开始计时", command=lambda i=i: self.start_timer(i)).grid(row=i, column=1)
            tk.Button(root, text="暂停计时", command=lambda i=i: self.pause_timer(i)).grid(row=i, column=2)
            tk.Button(root, text="结束课程", command=lambda i=i: self.end_timer(i)).grid(row=i, column=3)
            tk.Label(root, text="0h 0min 0s").grid(row=i, column=4)
        
        tk.Button(root, text="提交", command=self.save_data).grid(row=NUM_COURSES, columnspan=5)
        tk.Button(root, text="图表", command=self.show_chart).grid(row=0, column=5)
    
    def update_timer(self, i):
        if self.running[i]:
            elapsed = time.time() - self.start_times[i] + self.elapsed_times[i]
            hours, remainder = divmod(elapsed, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.root.grid_slaves(row=i, column=4)[0].config(text=f"{int(hours)}h {int(minutes)}min {int(seconds)}s")
            self.root.after(1000, lambda: self.update_timer(i))
    
    def start_timer(self, i):
        if not self.running[i]:
            self.start_times[i] = time.time()
            self.running[i] = True
            self.update_timer(i)
    
    def pause_timer(self, i):
        if self.running[i]:
            self.elapsed_times[i] += time.time() - self.start_times[i]
            self.running[i] = False
    
    def end_timer(self, i):
        self.pause_timer(i)
    
    def save_data(self):
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        selected_courses = sum(var.get() for var in self.course_vars)
        total_time = sum(self.elapsed_times)
        course_times = ', '.join(f"{int(hours)}h {int(minutes)}min {int(seconds)}s"
                                 for elapsed in self.elapsed_times
                                 for hours, remainder in [divmod(elapsed, 3600)]
                                 for minutes, seconds in [divmod(remainder, 60)])
        
        with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # 如果文件是空的，就写入头部
                writer.writerow(['DateTime', 'SelectedCourses', 'CourseTimes', 'TotalTime'])
            writer.writerow([date_time, selected_courses, course_times, total_time])
        
        messagebox.showinfo("信息", "数据已保存")
    
    def show_chart(self):
        df = pd.read_csv('data.csv')
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        df.set_index('DateTime', inplace=True)
        df['TotalTime'].plot()
        plt.ylabel('学习时间（秒）')
        plt.show()

root = tk.Tk()
app = App(root)
root.mainloop()
