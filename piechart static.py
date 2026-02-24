import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
colors = ['gold', 'lightpink', 'lightskyblue', 'lightgreen']

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=140)

plt.title("Programming Language ")
plt.axis('equal')  
plt.show()
