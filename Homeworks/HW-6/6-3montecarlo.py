import numpy as np
import matplotlib.pyplot as plt


def montepi(N):

    counts = 0
    xinlist = []
    yinlist = []
    xoutlist = []
    youtlist = []

    for i in range(N):

        x,y = np.random.rand(2)

        if x**2 + y**2 < 1:

            xinlist.append(x)
            yinlist.append(y)

            counts += 1
        
        else:
            xoutlist.append(x)
            youtlist.append(y)


    piest = 4 * counts / N

    return piest, xinlist, yinlist, xoutlist, youtlist

e3 = montepi(1000)
e4 = montepi(10000)
e5 = montepi(100000)
e6 = montepi(1000000)

print('Estimated Values of pi:')
print('N = 1e3: {:5.4f}'.format(e3[0]))
print('N = 1e4: {:5.4f}'.format(e4[0]))
print('N = 1e5: {:5.4f}'.format(e5[0]))
print('N = 1e6: {:5.4f}'.format(e6[0]))



plt.scatter(e4[1],e4[2],c='b')
plt.scatter(e4[3],e4[4],c='r')
plt.title('Monte Carlo Estimation of ' r'$\pi$' ', N = 1e4\nObtained value: {:5.4f}'.format(e4[0]))

plt.show()


