import numpy as np
import matplotlib.pyplot as plt

# First we define the appropriate variables.

R = .083144
a = 16.02
b = .1124

# Giving values to P and V
'''
P = np.linspace(1,10,100)
V = np.linspace(10,30,100)

Templist = []

for v in V:
    
    tv = []

    for p in P:

        tpv = (p + a / (v**2)) * (v - b) / R

        tv.append(tpv)

    Templist.append(tv)

Temp = np.array(Templist)

# print(Temp)


plt.imshow(Temp,origin='lower')
plt.colorbar()
plt.show()'''

# I realized that I could've done all this in just a couple of lines using np.meshgrid


P,V = np.meshgrid(np.linspace(1,10,100),np.linspace(10,30,100))


T = (P + 16.02 / (V ** 2)) * (V - .1124) / .083144

print(T)

plt.imshow(T,origin='lower',extent=[1,10,10,30],aspect='auto')

plt.xlabel('Pressure ' r'$(bar)$')
plt.ylabel('Volume ' r'$(liters)$')
plt.title('Van Der Waals Model Temperature Model')
plt.colorbar(label='Temperature ' r'$(Kelvin)$')

plt.show()


