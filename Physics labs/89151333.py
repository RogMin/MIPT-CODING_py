import math
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.transforms as mtransforms

"""
TRASH TRASH TRASH ЭТО СВАЛКА НЕ ЗАГЛЯДЫВАЙТЕ СЮДА TRASH TRASH TRASH 
"""

def lab141(xc,y,t, mc = 0.869, mg= 0.311 ,l = 1): #Значения подавать в СИ mc 0.869 кг вес стержня, mg 0.311 кг вес груза, 100 м длина
    period = t/20
    x = (period**2) * xc
    _y = y**2
    BuildScatterPlot(x,_y,True,5,"$T^2x_{ц},с^2{\cdot}м$","$y^2,м^2$")
    BuildScatterPlot(y,period, False,5,"$y,м$", "$T,с$")
    g = np.array((4*math.pi**2)* ((mc*l**2)/12 + (mc*xc**2) + (mg*y**2))/(period**2*(mc*xc+mg*y)))
    return g #Ускорение свободного падения

def BuildLinePlot(x,y,mnk = False,xlbl = "" ,ylbl = ""):
    plt.minorticks_on()
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.grid(which='major', axis='both', alpha=1)
    plt.grid(which='minor', axis='both', alpha=0.5)
    if mnk:
        p_f = np.poly1d(np.polyfit(x, y, deg=1))
        plt.plot(x, p_f(x), "o")
    plt.plot(x,y)
    plt.show()
    return

def BuildScatterPlot(x,y,mnk = False, mrksz = 5, xlbl = "" ,ylbl = ""):
    plt.minorticks_on()
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.grid(which='major', axis='both', alpha=1)
    plt.grid(which='minor', axis='both', alpha=0.5)
    if mnk:
        p_f = np.poly1d(np.polyfit(x, y, deg=1))
        plt.plot(x, p_f(x), "#808080")
    plt.plot(x, y, "ok",markersize=mrksz)
    plt.show()
    return

#def LagrangeInt(x,y):

   # return f

#plt.minorticks_on()
#plt.grid(which='major', axis='both', alpha=1)
#plt.grid(which='minor', axis='both', alpha=0.5)
#x = np.arange(-0.4,0.9,0.01)
#y = 2*math.pi*(((0.1518+0.3113*(x**2))/(2.7179*x+2.2935))**1/2)

#plt.plot(x,y,"#808080")
#plt.plot(np.mean(x),np.min(y), "ok")
#plt.show()

#BuildLinePlot(x,y)


def mandelbrot(h, w, maxit=20):
    y, x = np.ogrid[-1.4:1.4:h * 1j, -2:0.8:w * 1j]
    c = x + y * 1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)
    for i in range(maxit):
        z = (z ** 2 + c) * np.complex(1)
        diverge = z * np.conj(z) > 2 ** 2
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = 2
    return divtime
def is_prime(x):
    x = int(x)
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
        return True

def coll(n):
    numb = []
    n_pr =[]
    while n > 1:
        if (n % 2) == 0:
            n /= 2
            numb.append(n)
        else:
            n = (n * 3) + 1
            numb.append(n)

        if (is_prime(n)): n_pr.append((n))
    return numb,n_pr


x = [17, 19, 20, 21,22,23,24,25,26,27,28]
y = [3.5,3.5, 4 ,4.5 ,2.5 ,4.5, 4.5, 4, 3.5, 4,3]

BuildLinePlot(x,y)
numb, n_pr = coll(1005)
BuildLinePlot(np.arange(0,len(numb)), numb, np.arange(0,len(n_pr), n_pr))
plt.polar(numb)
BuildLinePlot(np.arange(0,len(n_pr)),n_pr)
plt.polar(n_pr)



#xs = np.arange(7)
#ys = xs**2

#fig = plt.figure(figsize=(5, 10))
#ax = plt.subplot(2, 1, 1)


#trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
#                                       x=0.05, y=0.10, units='inches')
#for x, y in zip(xs, ys):
#    plt.plot(x, y, 'ro')
#    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)




#ax = plt.subplot(2, 1, 2, projection='polar')

#trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                      # y=6, units='dots')

#for x, y in zip(xs, ys):
#    plt.polar(x, y, 'ro')
#    plt.text(x, y, '%d, %d' % (int(x), int(y)),
#             transform=trans_offset,
#             horizontalalignment='center',
#             verticalalignment='bottom')

plt.show()

#plt.imshow(mandelbrot(400, 400))
#plt.show()












