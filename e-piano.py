import numpy as np
import matplotlib.pyplot as plt
import threading
from matplotlib.animation import FuncAnimation
import tkinter as tk
import matplotlib
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import pyaudio
import wave

CHUNK = 1
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.5
pitch=[262,277,294,311,330,349,370,392,415,440,466,494,523]
dt=1.0/RATE

def play(j):#
	
	p = pyaudio.PyAudio()
	
	stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=False,
                output=True,
                frames_per_buffer=CHUNK)
	xdata, ydata = [], []      #初始化两个数组
	
	for i in range(0, int(RATE * RECORD_SECONDS)):
		xdata.append(i/RATE)
		ydata.append(2000*np.sin(i/RATE*2*np.pi*pitch[j]))
		data=str(2000*np.sin(i/RATE*2*np.pi*pitch[j]))
		stream.write(data, CHUNK)
		
	
	   
	matplotlib.use('TkAgg')   
	fig =plt.Figure(figsize=(5,4), dpi=80)   #设置空画布fig，figsize为大小，dpi为分辨率
	draw_set=FigureCanvasTkAgg(fig, master=window)#将空画布设置在tkinter上
	ax = fig.add_subplot(111)##设置坐标轴
	ax.set_xlim(0, 0.02)  #设置x轴的范围pi代表3.14...圆周率，
	ax.set_ylim(-2000, 2000)
	
	draw_set.get_tk_widget().place(x=15,y=20,height=250,width=300)   #将画好的画布放置在tkinter界面上
	ax.plot(xdata,ydata,'r-')
	

	stream.stop_stream()
	stream.close()
	p.terminate()
	
	
	#ani = FuncAnimation(fig, update, frames=np.linspace(0,0.02, 50),init_func=init,interval=40, blit=True)#25帧


if __name__ == '__main__':
	window=tk.Tk()       
	window.geometry("330x450")      #tkinter界面长宽，根据像素点来的，每个不同的分辨率电脑上显示不一样
	window.title("简易电子琴")   #设置tkinter界面名字
	window.resizable(0,0)#界面不能放大缩小
	matplotlib.use('TkAgg')   
	fig =plt.Figure(figsize=(5,4), dpi=80)   #设置空画布fig，figsize为大小，dpi为分辨率
	draw_set=FigureCanvasTkAgg(fig, master=window)#将空画布设置在tkinter上
	
	ax = fig.add_subplot(111)##设置坐标轴
	ax.set_xlim(0, 0.02)  #设置x轴的范围pi代表3.14...圆周率，
	ax.set_ylim(-2000, 2000)
	
	draw_set.get_tk_widget().place(x=15,y=20,height=250,width=300)   #将画好的画布放置在tkinter界面上
	ax.plot([0,1],[0,0],'r-')
	
	
	key0=tk.Button(window,width=3,height=5,background='white',command=lambda:play(0))
	key0.place(x=30,y=330)
	key2=tk.Button(window,width=3,height=5,background='white',command=lambda:play(2))
	key2.place(x=60,y=330)
	key4=tk.Button(window,width=3,height=5,background='white',command=lambda:play(4))
	key4.place(x=90,y=330)
	key5=tk.Button(window,width=3,height=5,background='white',command=lambda:play(5))
	key5.place(x=120,y=330)
	key7=tk.Button(window,width=3,height=5,background='white',command=lambda:play(7))
	key7.place(x=150,y=330)
	key9=tk.Button(window,width=3,height=5,background='white',command=lambda:play(9))
	key9.place(x=180,y=330)
	key11=tk.Button(window,width=3,height=5,background='white',command=lambda:play(11))
	key11.place(x=210,y=330)
	key12=tk.Button(window,width=3,height=5,background='white',command=lambda:play(12))
	key12.place(x=240,y=330)

	key1=tk.Button(window,width=2,height=5,background='black',command=lambda:play(1))
	key1.place(x=50,y=280)
	key3=tk.Button(window,width=2,height=5,background='black',command=lambda:play(3))
	key3.place(x=80,y=280)
	key6=tk.Button(window,width=2,height=5,background='black',command=lambda:play(6))
	key6.place(x=140,y=280)
	key8=tk.Button(window,width=2,height=5,background='black',command=lambda:play(8))
	key8.place(x=170,y=280)
	key10=tk.Button(window,width=2,height=5,background='black',command=lambda:play(10))
	key10.place(x=200,y=280)
	window.mainloop()
