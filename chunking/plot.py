import matplotlib.pyplot as plt

file = open("results", "r")

x, y = [], []

for line in file:
  n, t = line.split() 
  x.append(int(n))
  y.append(float(t))

plt.plot(x, y) 
plt.xlabel("chunk size n") 
plt.ylabel("time in seconds")

plt.savefig("graph.png")
