import matplotlib.pyplot as plt
from numpy import *

saveThem = 1

figCount = 0

######################
def makeImage():
    global figCount
    if saveThem == 1:
        plt.savefig("fig" + str(figCount) + ".pdf", format="pdf")
        plt.show()
        figCount += 1
    if saveThem == 0:
        plt.show()
    return
#######################

x = arange(6)

plt.plot(2*x - 3)
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
makeImage()

plt.plot(-4*x + 12)
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
makeImage()

x = arange(0,5,.02)

plt.plot(x,x*x*sin(2*pi*x))
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
makeImage()

plt.plot(x, 2*exp(x - 3) - 8)
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
makeImage()

