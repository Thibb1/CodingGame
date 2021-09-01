I=input
n,horsePower,horsePowerDiff=int(I()),[],[]
for i in range(n):
    horsePower.append(int(I()))
horsePower.sort()
for i in range(n-1):
    horsePowerDiff.append(horsePower[i+1] - horsePower[i])
horsePowerDiff.sort()
print(horsePowerDiff[0])
