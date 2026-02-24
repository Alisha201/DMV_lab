import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [10, 15, 13, 17, 20, 18, 25]

plt.figure(figsize=(6,4))
plt.scatter(x, y, color='blue', marker='o', s=100)

plt.title("Static Scatter Plot (Fixed Values)")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)
plt.show()
