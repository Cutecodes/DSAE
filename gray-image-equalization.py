from PIL import Image
from pylab import *
import numpy

def histeq(im,nbr_bins = 256):
    """对一幅灰度图像进行直方图均衡化"""
    #计算图像的直方图
    #在numpy中，也提供了一个计算直方图的函数histogram(),第一个返回的是直方图的统计量，第二个为每个bins的中间值
    imhist,bins = numpy.histogram(im.flatten(),nbr_bins)
    cdf = imhist.cumsum()   #
    cdf = 255.0 * cdf / cdf[-1]
    #使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape),cdf

img = Image.open('test.jpg')
subplot(321)
axis('off')
imshow(img)

gray()
img_gray = Image.open('test.jpg').convert('L')
subplot(322)
axis('off')
imshow(img_gray)

im=array(img_gray)
subplot(323)
hist(im.flatten(), 128)
plt.xlim([0,260])
plt.ylim([0,60000])


img_gray2,cdf=histeq(im)
subplot(324)
axis('off')
imshow(img_gray2)

im2=array(img_gray2)
subplot(325)
hist(im2.flatten(), 128)
plt.xlim([0,260])
plt.ylim([0,60000])
show()

