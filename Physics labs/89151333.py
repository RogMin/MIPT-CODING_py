import math
import numpy as np
from matplotlib import pyplot as plt


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


#plt.minorticks_on()
#plt.grid(which='major', axis='both', alpha=1)
#plt.grid(which='minor', axis='both', alpha=0.5)
#x = np.arange(-0.4,0.9,0.01)
#y = 2*math.pi*(((0.1518+0.3113*(x**2))/(2.7179*x+2.2935))**1/2)

#plt.plot(x,y,"#808080")
#plt.plot(np.mean(x),np.min(y), "ok")
#plt.show()

#BuildLinePlot(x,y)
xc = np.array([36.35, 38.2, 37.2, 36.3, 35.4, 34.5, 33.1, 32.5,31.6, 31,30.1,29.2,28.1,26.6,26,24.3,23.1,21.3]) / 100
y = np.array([63.5,70.6,66.65,62.8,59.4,55.8,50.5,47.9,43.75,41.1,37.9,34.2,29.9,24.5,21,15.5,10.9,3.5]) /100
t = np.array([31.1,32.05,31.57,31.1,30.72,30.33,29.8,29.59,29.26,29.07,28.88,28.6,28.56,28.5,28.57,28.77,29.1,30.01])
print(np.mean(lab141(xc,y,t)))

