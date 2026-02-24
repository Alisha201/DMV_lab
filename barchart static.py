import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 24, 36, 18, 12]

plt.bar(categories, values, color='skyblue')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Static Bar Chart')


plt.show()

