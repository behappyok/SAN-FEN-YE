'''
Description  : 
Author       : zyl
Date         : 2023-05-26 23:57:34
LastEditTime : 2023-05-27 01:08:31
FilePath     : \\love.py
'''
import numpy as np,random
from PIL import Image
import matplotlib.pyplot as plt
import gif


def plot_scatter(ax,x, y,  beta, s, c="#d66582", alpha=0.8, marker=r'$\heartsuit$'):
    def scatter_inside(x, y, beta=0.15):
        ratio_x = - beta * np.log(np.random.rand(x.shape[0]))
        ratio_y = - beta * np.log(np.random.rand(y.shape[0]))
        dx = ratio_x * x
        dy = ratio_y * y
        return x - dx, y - dy
    x1, y1 = scatter_inside(x, y , beta)
    ax.scatter(x1, y1, s,c)


@gif.frame
def plot_heart(x, y, ratio):
    fig = plt.figure(figsize=(7, 7),facecolor="black")
    ax = plt.gca()
    ax.set_facecolor("black")
    x = x * np.sin(ratio) 
    y = y * np.sin(ratio) 
    ax.scatter(x, y, s=3, c="#d66582")
    plot_scatter(ax,x,y,0.15,1)
    plot_scatter(ax,x,y,0.15,2)
    plot_scatter(ax,x,y,0.15,3)
    # plt.scatter(x, y, s=3, c="#d66582")
    x1=x[0:x.shape[0]:2]* np.sin(ratio) * .7
    y1=y[0:x.shape[0]:2]* np.sin(ratio) * .7
    # ax.scatter(x1, y1, s=3, c="#d66582")
    plot_scatter(ax,x1,y1,0.25,4)
    # x1, y1 = scatter_inside(x*0.7, y*0.7 , beta=0.15)
    # ax.scatter(x1, y1, s=3, c="#d66582")
    xo = x[0:x.shape[0]:2]* np.sin(ratio) * 1.2
    yo = y[0:y.shape[0]:2]* np.sin(ratio) * 1.2 # scatter_inside(x*1.2, y*1.2, beta=0.1)
    np.random.seed(random.randint(1,3))
    plot_scatter(ax,xo, yo, 0.1,4, alpha=0.8)
    # ax.set_facecolor("black")
    
    for spine in ax.spines.values():
            spine.set_visible(False)
    ax.tick_params(bottom=False, labelbottom=False,
                       left=False, labelleft=False)   
    plt.xlim((-6*np.pi, 6*np.pi))
    plt.ylim((-6*np.pi, 6*np.pi))
    plt.tight_layout(pad=0)
    
frames = []
for ratio in np.linspace(np.pi/3, 2*np.pi/3, 20):
    t = np.linspace(0, 2*np.pi, 2000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    of = plot_heart(x, y, ratio)
    frames.append(of)
gif.save(frames, "love.gif", duration=100)  
im=Image.open("love.gif")