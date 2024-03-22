import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,1)

indexvalues = np.arange(1,41,1)



x1 = np.random.uniform(0,100,40)
x2 = np.random.uniform(0,100,40)
x3 = np.random.uniform(0,100,40)


axes[0].plot(indexvalues,x1,'tab:orange',linewidth=10)
axes[0].plot(indexvalues,x2,'--r')



axes[1].scatter(indexvalues,x3,c='m',marker='d')



plt.show()





