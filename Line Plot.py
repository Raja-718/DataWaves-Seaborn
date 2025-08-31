# Experiment 3: Line Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.lineplot(x="size", y="tip", data=tips, estimator="mean")
plt.title("Average Tip by Table Size")
plt.show()
