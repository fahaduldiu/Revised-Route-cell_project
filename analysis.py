import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cells.csv")

plt.plot(df['time'], df['cell_count'], marker='o')
plt.title("Cell Growth Over Time")
plt.xlabel("Time (hours)")
plt.ylabel("Number of Cells")
plt.savefig("plot_line.png")
plt.show()

plt.scatter(df['time'], df['cell_count'])
plt.title("Scatter Plot of Cell Growth")
plt.xlabel("Time (hours)")
plt.ylabel("Number of Cells")
plt.savefig("plot_scatter.png")
plt.show()

plt.bar(df['time'], df['cell_count'])
plt.title("Bar Chart of Cell Growth")
plt.xlabel("Time (hours)")
plt.ylabel("Number of Cells")
plt.savefig("plot_bar.png")
plt.show()
