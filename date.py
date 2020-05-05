import datetime
import time
import calendar
from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
import sys, os

class Main(object):

	def __init__(self):

		def resource_path(relative_path):
		#Get absolute path to resource, works for dev and for PyInstaller
			try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
				base_path = sys._MEIPASS
			except Exception:
				base_path = os.path.abspath(".")
			return os.path.join(base_path, relative_path)

		def futuredate():
			entryvalue = inputdays.get()
			try: #利用將輸入字串轉換成數字int型式判斷是否輸入為數字
				d = int(entryvalue)

			except ValueError:
				messagebox.showwarning("Error","請輸入數字！！")
				inputdays.delete(0, END)
				answer1.config(text = "")
			else:
				if len(entryvalue) > 5:
					messagebox.showwarning("Error","此處請勿輸入超過5位數")
					inputdays.delete(0, END)
					answer1.config(text = "")
				else:
					today = datetime.date.today()
					future = today + datetime.timedelta( days = d )
					answer1.config(text = future)

		def timedifference():
			year1entryvalue = inputyear1.get()
			year2entryvalue = inputyear2.get()
			mounth1entryvalue = inputmounth1.get()
			mounth2entryvalue = inputmounth2.get()
			day1entryvalue = inputday1.get()
			day2entryvalue = inputday2.get()

			try: #利用將輸入字串轉換成數字int型式判斷是否輸入為數字
				d1year = int(year1entryvalue)
				d1month = int(mounth1entryvalue)
				d1day = int(day1entryvalue)

				d2year = int(year2entryvalue)
				d2month = int(mounth2entryvalue)
				d2day = int(day2entryvalue)
			except ValueError:
				messagebox.showwarning("Error","請輸入數字！！")
				answer2.config(text = "")
			else:
				if len(year1entryvalue) > 4:
					messagebox.showwarning("Error","年份請勿輸入超過4位數！！")
					inputyear1.delete(0, END)
				elif len(year2entryvalue) > 4:
					messagebox.showwarning("Error","年份請勿輸入超過4位數！！")
					inputyear2.delete(0, END)
				else:
					try: #利用將輸入的年月日放入datatime.date函式裡判斷輸入值是否為正確的年月日型式
						d1 = datetime.date( d1year, d1month, d1day)
						d2 = datetime.date( d2year, d2month, d2day)
					except ValueError:
						messagebox.showwarning("Error","輸入日期有誤！！")
						answer2.config(text = "")
					else:
						dayCount = abs( (d2 - d1).days )
						answer2.config(text = str(dayCount) + "天")

		icon = resource_path("Calendar.ico")
		self.window = Tk()
		self.window.iconbitmap(icon)
		self.window.title("DateCount") #視窗名稱
		self.window.config(background = "#f0f0f0")#更該視窗背景顏色
		self.window.geometry("210x330+800+250") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
		self.window.resizable(0,0)#不可以更改大⼩
		Font = tkfont.Font(family = "新細明體", size = 10, weight = "bold")
#Function1:第N天後日期=============================================================================================================================#
		frame1 = LabelFrame(self.window, text = "第N天後日期", font = Font)
		frame1.place(x = 25, y = 15)

		inputtitle = Label(frame1, font = Font, text = "N      = ")
		inputtitle.grid(row = 0, padx = 2, pady = 10)

		inputdays = Entry(frame1, font = Font, width = 10)
		inputdays.grid(row = 0, column = 1, padx = 10, pady = 10)

		function1count = Button(frame1, text = "計算", font = Font, bg = "skyblue", width = 10, height = 1,command = futuredate)
		function1count.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

		answertitle1 = Label(frame1, text = "Answer:", font = Font)
		answertitle1.grid(row = 2, column = 0, padx = 5, pady = 5)

		answer1 = Label(frame1, font = Font)
		answer1.grid(row = 2, column = 1, padx = 5, pady = 5)
#Function2:日期相差=============================================================================================================================#
		frame2 = LabelFrame(self.window, text = "日期相差", font = Font)
		frame2.place(x = 25, y = 150)

		inputyear1 = Entry(frame2, font = Font, width = 4)
		inputyear1.grid(row = 0, padx = 10, pady = 10)

		inputmounth1 = Entry(frame2, font = Font, width = 2)
		inputmounth1.grid(row = 0, column = 2, padx = 5, pady = 10)

		inputday1= Entry(frame2, font = Font, width = 2)
		inputday1.grid(row = 0, column = 4, padx = 10, pady = 10)

		inputyear2 = Entry(frame2, font = Font, width = 4)
		inputyear2.grid(row = 1, padx = 10, pady = 10)

		inputmounth2 = Entry(frame2, font = Font, width = 2)
		inputmounth2.grid(row = 1,column = 2, padx = 5, pady = 10)

		inputday2= Entry(frame2, font = Font, width = 2)
		inputday2.grid(row = 1,column = 4, padx = 10, pady = 10)

		for i in range(0, 4, 2):#range(0, 4, 2)：產生從0, 2的整數序列(遞增值為2)。
			Label(frame2, text = "/", font = Font).grid(row = 0, column = i+1)
			Label(frame2, text = "/", font = Font).grid(row = 1, column = i+1)

		function2count = Button(frame2, text = "計算", font = Font, bg = "skyblue", width = 10, height = 1, command = timedifference)
		function2count.grid(row = 2, columnspan = 5, padx = 30, pady = 5)

		answertitle2 = Label(frame2, text = "Answer:", font = Font)
		answertitle2.grid(row = 3, padx = 10, pady = 5)

		answer2 = Label(frame2, font = Font)
		answer2.grid(row = 3,column = 1, columnspan = 4, pady = 10)

		self.window.mainloop()

if __name__ == '__main__':
	Main()