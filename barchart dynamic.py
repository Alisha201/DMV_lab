import matplotlib.pyplot as plt

plt.ion()

categories = []
values = []

fig, ax = plt.subplots()

while True:
    label = input("Enter category name (or 'q' to quit): ")
    if label.lower() == 'q':
        break

    try:
        value = float(input(f"Enter value for {label}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    categories.append(label)
    values.append(value)

    ax.clear()
    ax.bar(categories, values, color='skyblue')
    ax.set_title("Dynamic Bar Chart")
    ax.set_ylabel("Values")
    ax.set_xlabel("Categories")

    plt.pause(0.1)

plt.ioff()
plt.show()
