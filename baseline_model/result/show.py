import matplotlib.pyplot as plt

avg_f= open("avg","r")
max_f= open("max","r")

max_data=[]
avg_data=[]
n=[]

for line in avg_f:
    avg_data.append(float(line))
for line in max_f:
    max_data.append(float(line))
for i in range(1,10001):
    n.append(i)

plt.plot(n,max_data,label="max")
plt.plot(n,avg_data,label="avg")
plt.xscale('log')
plt.xlabel("Generations")
plt.ylabel("fitness")
plt.legend()
plt.show()
