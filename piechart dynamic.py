import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'JavaScript']

sizes = []
for label in labels:
    value = int(input(f"Enter value for {label}: "))
    sizes.append(value)

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Dynamic Pie Chart")
plt.show()
3