import os

ss = input("File path : ")
s = ss.split(".")[0]
if not os.path.exists("./"+s+"_output"):
    os.makedirs("./"+s+"_output")
f = open(ss)
threshold = int(input("Threshold : "))
span = int(input("Span : "))
y = []
# t = 1e-3
for line in f:
    line = line.split()
    if len(line) > 0:
        number = float(line[0])
        y.append(number)
print(len(y))
f.close()

count = 0
state = 0
fileCount = 0
out = ""
n = 0

while n < len(y):
    if y[n] >= threshold and n - 3 + span < len(y):
        out = open("./"+s+"_output/slice"+str(fileCount), "w")
        fileCount = fileCount + 1
        tempSlice = y[n - 5:n+span-4]
        slices = []
        for x in tempSlice:
            slices.append(str(x)+'\n')

        out.writelines(slices)
        out.close()
        n = n + span + 20
    else:
        n += 1
