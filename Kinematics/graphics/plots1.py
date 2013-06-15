import matplotlib.pyplot as plt
from numpy import *

saveThem = 0

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
y = arange(5)+5
plt.plot(2*x - 3)
plt.plot(- 2*y + 4)
plt.ylabel('x(t)')
plt.xlabel('t')
plt.grid(True)
makeImage()

