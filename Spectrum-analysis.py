import numpy as np

import matplotlib.pyplot as plt

import matplotlib.animation as animation

import pyaudio

from scipy.fftpack import fft,ifft


chunk=4096
rate=44100

p = pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16, channels=1, rate=rate,input=True,frames_per_buffer=chunk)


fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
t = np.linspace(0, chunk - 1, chunk)
ax1.set_xlabel('t')
ax1.set_ylabel('x')
line1, = ax1.plot([], [], lw=2)
ax1.set_xlim(0, chunk)
ax1.set_ylim(-15000, 15000)
ax2.set_xlabel('hz')
ax2.set_ylabel('y')
line2, = ax2.plot([], [], lw=2)
ax2.set_xlim(0, chunk)
ax2.set_ylim(-50, 100)
# 更新间隔/ms
interval = int(1000*chunk/rate)


x = np.linspace(0, chunk - 1, chunk)
freqs = np.linspace(0, rate / 2, chunk / 2 + 1)
def update(data):
	y = np.fromstring(stream.read(chunk), dtype=np.int16)			
	line1.set_data(x, y)
# 傅里叶变化

	xf = abs(np.fft.rfft(y) / chunk)
	xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
	line2.set_data(freqs, xf)
ani= animation.FuncAnimation(fig, update, interval=interval)
plt.show()
		




