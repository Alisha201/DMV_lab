import matplotlib.pyplot as plt

n = int(input("Enter number of subplots: "))

for i in range(1, n + 1):
    plt.subplot(1, n, i)
    x = list(range(1, 6))
    y = [j * i for j in x]
    plt.plot(x, y)
    plt.title(f"Plot {i}")

plt.tight_layout()
plt.show()
