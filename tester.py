import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(6,4))
plt.plot(x, y, label="Sine Wave")
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Example Temporal Plot")
plt.legend()
plt.savefig("assets/images/example-plot.png")  # Save the plot
