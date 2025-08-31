# Experiment 5: Countplot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.countplot(x="day", data=tips, hue="sex")
plt.title("Count of Records by Day and Sex")
plt.show()
