import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.random.randint(0, 40, 30)
y = np.random.randint(0, 40, 30)
z = np.random.randint(0, 40, 30)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for xx, yy, zz in zip(x, y, z):
    color = 'y'
    if 10 < zz < 20:
        color = '#C71585'
    elif zz >= 20:
        color = '#008B8B'
    ax.scatter(xx, yy, zz, c=color, marker='*', s=160, linewidth=1, edgecolor='black')
ax.set_xlabel('x轴')
ax.set_ylabel('y轴')
ax.set_zlabel('z轴')
ax.set_title('3D散点图', fontproperties='simhei', fontsize=14)
plt.tight_layout()
plt.show()
