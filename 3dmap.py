#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(1)
ax = plt.axes(projection='3d')

contrast_small= [34.1484446, 28.8275027, 23.2473774, 73.8745658, 68.5131439, 57.4827156, 15.6011515, 13.6726030, 11.0482861, 87.0821986, 67.9805632, 52.8906617]

contrast_large = [5.2064916, 4.5363534, 2.7000166, 29.6619887, 17.4274736, 15.1775172, 4.3600259, 4.3726055, 3.6056773, 21.5700644, 20.1985495, 18.3212576]

bitrate_small = [566017,
122173,
83482,
531988,
94316,
58099,
567624,
127630,
87457,
515151,
89887,
50023]

bitrate_large = [561654,
132254,
90012,
576224,
116541,
78911,
528787,
129324,
88689,
522062,
99318,
67491]

k_small = [0.703479,
3.259106,
4.769579,
0.748478,
4.221679,
6.853294,
0.701489,
3.119768,
4.552814,
0.772940722,
4.429708005,
7.959633839]

k_large = [0.74833,
3.177955,
4.669289,
0.729408,
3.606401,
5.326136,
0.753008,
3.078901,
4.489567,
0.762709,
4.009098,
5.89961]

d_small = [361, 361, 361, 361, 361, 361, 542, 542, 542, 542, 542, 542]
d_large = [361, 361, 361, 361, 361, 361, 542, 542, 542, 542, 542, 542]


xdata = bitrate_small
ydata = k_small
zdata = contrast_small
ax.set_xlabel('bitrate [kbps]')
ax.set_ylabel('compression [a.u.]')
ax.set_zlabel('contrast [a.u.]');
ax.set_title('small ABCD');
ax.scatter3D(xdata, ydata, zdata, c=zdata)

fig = plt.figure(2)
bx = plt.axes(projection='3d')
bx.set_xlabel('bitrate [kbps]')
bx.set_ylabel('compression [a.u.]')
bx.set_zlabel('contrast [a.u.]');
bx.set_title('large ABCD');
bx.scatter3D(bitrate_large, k_large, contrast_large, c=zdata)

plt.show()