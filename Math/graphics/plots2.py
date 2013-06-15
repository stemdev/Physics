import matplotlib.pyplot as plt
from numpy import *

saveThem = 1

figCount = 20

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

plt.plot(-2.5*x + 8)
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
makeImage()

plt.plot(3*x - 6)
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
makeImage()

x = arange(0,5,.02)

plt.plot(x,log(x)*sin(2*pi*x)+2)
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
makeImage()

x = arange(2,7,.02)
#x = arange(0,5,.02)

plt.plot(x, 2*exp(-x + 4) + 6)
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
makeImage()

