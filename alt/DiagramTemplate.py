# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.legend_handler import HandlerLine2D
from matplotlib import rc
rc('mathtext', default='regular')

ls1=16
width1=2
tl1=10 #tickLength
zeit1=np.array([2.5, 5, 7.5, 10, 14, 18, 22, 24, 29, 34, 36])
weg1=np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.5, 4.5, 5.5, 6])
fig, ax1 = plt.subplots(figsize=(8, 6))
h1=ax1.plot(zeit1,weg1, 'ro', ms=12, mec='k', mfc='w', mew=3, label='Velocity', 
             ls='-', lw=3, color='k')
#ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.tick_params(which='major', width=width1, length=tl1, labelsize=ls1, pad=15,
                direction='in')
ax1.axhline(linewidth=width1)
for axis in ['top','bottom','left','right']:
  ax1.spines[axis].set_linewidth(width1)

ax1.set_xlabel('Zeit (s)',fontsize=16,fontweight='bold',labelpad=5)#
ax1.set_ylabel('Geschwindigkeit (m/s)',fontsize=16,fontweight='bold',labelpad=5)
ax1.set_xlim(0,np.amax(zeit1)*1.1)
ax1.set_ylim(0,np.amax(weg1)*1.1)
plt.show()