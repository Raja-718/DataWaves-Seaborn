# Experiment 34: Rug Plot Overlay with Histogram
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(7,5))
sns.histplot(tips["tip"], bins=15, kde=True, color="teal", alpha=0.6)
sns.rugplot(tips["tip"], color="black", height=0.1)
plt.title("Histogram with Rug Plot Overlay (Tips)")
plt.show()
