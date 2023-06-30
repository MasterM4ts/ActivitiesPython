#Apresentação#

import matplotlib.pyplot as plt

x = [2023,2022,2021,2005]
y = [1300,1212,1100,2000]

plt.plot(x, y, "y")
plt.grid()
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.bar(x, y)
plt.show()