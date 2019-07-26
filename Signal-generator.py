
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter
from tkinter import messagebox
 
freq = 1
margin = 1
deviation = 0
wave = 0
 
ss = []
 
fig = plt.figure()
axes1 = fig.add_subplot(111)
line, = axes1.plot(np.linspace(-10,10,3000))
 
def fangbo(data):
  lis = []
  for i in list(data):
    if i//5%2 == 1:
      lis.append(1)
    else:
      lis.append(-1)
  return np.array(lis)
 
def juchi(data):
  lis = []
  for i in list(data):
    lis.append(i%5/2.5)
  return np.array(lis)-1
 
def sanjiao(data):
  lis = []
  for i in list(data):
    if i//5%2 == 1:
      lis.append(i%5/2.5)
    else:
      lis.append((5-i%5)/2.5)
  return np.array(lis)-1
 
def update(data):
  line.set_ydata(data)
  return line,
def data_gen():
  i = 50
  res = [0*i for i in range(3000)]
  while True:
    global freq, margin, deviation, wave, ss
    if wave == 0:
      lis = list(margin*np.sin(freq*3.1415926/5*np.linspace(1,100,3000))+deviation)
    elif wave == 1:
      lis = list(margin*juchi(freq*np.linspace(1,100,3000))+deviation)
    elif wave == 2:
      lis = list(margin*sanjiao(freq*np.linspace(1,100,3000))+deviation)
    elif wave == 3:
      lis = list(margin*fangbo(freq*np.linspace(1,100,3000))+deviation)
    ss = ss+lis[i-50:i]
    yield ss+res[len(ss):]
    i = i+50
    if len(ss) >= 3000:
      ss = ss[50:]
    if i > 3050:
      i = 50
 
def ssin():
  global wave
  wave = 0
 
def jjc():
  global wave
  wave = 1
 
def ssj():
  global wave
  wave = 2
 
def ffb():
  global wave
  wave = 3
 
def simu():
  global freq, margin, deviation
  try:
    fe1 = float(fe.get('0.0','end'))
    me1 = float(me.get('0.0','end'))
    de1 = float(de.get('0.0','end'))
    xe1 = float(xe.get('0.0','end'))
  except:
    messagebox.showinfo(title='错误',message='属性值必须为浮点数')
  else:
    freq = fe1
    margin = me1
    deviation = de1
 
if __name__ == '__main__':
  root = tkinter.Tk()
  root.title('波形发生器')
  root.maxsize(320,140)
  root.minsize(320,140)
  lb = tkinter.Label(root,text='波形选择')
  lb.pack()
  fbt = tkinter.Button(root,text='正弦波',command=ssin)
  fbt.place(x=20,y=20)
  sbt = tkinter.Button(root,text='三角波',command=ssj)
  sbt.place(x=100,y=20)
  jbt = tkinter.Button(root,text='锯齿波',command=jjc)
  jbt.place(x=180,y=20)
  jbt = tkinter.Button(root,text='方波',command=ffb)
  jbt.place(x=260,y=20)
  ib = tkinter.Label(root,text='属性控制')
  ib.place(x=130,y=50)
  fl = tkinter.Label(root,text='频率')
  fl.place(x=10,y=70)
  fe = tkinter.Text(root,width=3,height=1)
  fe.insert('end','1')
  fe.place(x=50,y=70)
  ml = tkinter.Label(root,text='幅值')
  ml.place(x=85,y=70)
  me = tkinter.Text(root,width=3,height=1)
  me.insert('end','1')
  me.place(x=125,y=70)
  dl = tkinter.Label(root,text='偏移')
  dl.place(x=160,y=70)
  de = tkinter.Text(root,width=3,height=1)
  de.insert('end','0')
  de.place(x=200,y=70)
  xl = tkinter.Label(root,text='相位')
  xl.place(x=235,y=70)
  xe = tkinter.Text(root,width=3,height=1)
  xe.insert('end','0')
  xe.place(x=275,y=70)
  mb = tkinter.Button(root,text='仿真',command=simu)
  mb.place(x=130,y=95)
  ani = animation.FuncAnimation(fig, update, data_gen, interval=10)
  plt.show()
  root.mainloop()
