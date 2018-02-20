from matplotlib import pyplot as plt



s = input("file path:  ")
f = open(s)
y = []

for line in f:
    line = line.split()
    if len(line) > 0:
        number = float(line[0])
        y.append(number)
print(len(y))
f.close()

plt.title(s)
plt.grid(b=True)
plt.plot(y)
plt.show()

