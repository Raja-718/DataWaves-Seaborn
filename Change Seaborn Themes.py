# Experiment 11: Change Seaborn Themes
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Apply theme
sns.set_theme(style="darkgrid")

plt.figure(figsize=(6,4))
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex")
plt.title("Seaborn Theme: Darkgrid")
plt.show()
