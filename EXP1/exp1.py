import numpy as np
import matplotlib.pyplot as plt
import time

# AND gate dataset with bias
X = np.array([
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
])

T = np.array([0, 0, 0, 1])

# Initialize weights
w = np.zeros(3)
learning_rate = 1

epoch = 0
errors_per_epoch = []

def step(net):
    return 1 if net > 0 else 0

plt.ion()

while True:
    epoch += 1
    total_error = 0

    print(f"\nEpoch {epoch}")
    print("-" * 80)
    print("x1 x2 | Target | Output | Status        | Error | Updated Weights")
    print("-" * 80)

    outputs = []

    for i in range(len(X)):
        net = np.dot(w, X[i])
        y = step(net)
        error = T[i] - y

        status = "SUCCESS" if error == 0 else "MISCLASSIFIED"

        # Update weights
        w = w + learning_rate * error * X[i]

        total_error += abs(error)
        outputs.append(y)

        print(f"{X[i][1]}  {X[i][2]}  |   {T[i]}    |   {y}    | "
              f"{status:<13} | {error:+d}   | {w}")

    errors_per_epoch.append(total_error)

    # Plot
    plt.clf()
    for i in range(len(X)):
        color = 'green' if T[i] == outputs[i] else 'red'
        marker = 'o' if T[i] == outputs[i] else 'x'
        plt.scatter(X[i][1], X[i][2], c=color, marker=marker, s=100)

    if w[2] != 0:
        x_vals = np.array([-0.5, 1.5])
        y_vals = -(w[0] + w[1]*x_vals) / w[2]
        plt.plot(x_vals, y_vals, 'b--')

    plt.title(f"Perceptron AND Gate - Epoch {epoch}")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 1.5)
    plt.grid(True)

    plt.draw()
    plt.pause(0.5)

    if total_error == 0:
        break

plt.ioff()

# Error vs Epoch
plt.figure()
plt.plot(range(1, epoch + 1), errors_per_epoch, marker='o')
plt.xlabel("Epoch")
plt.ylabel("Total Error")
plt.title("Error vs Epoch")
plt.grid(True)
plt.show()
