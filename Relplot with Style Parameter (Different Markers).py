
# Experiment 25: Relplot with Style Parameter
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.relplot(x="total_bill", y="tip", hue="sex", style="smoker", data=tips)
plt.suptitle("Relplot with Style Parameter (Markers)", y=1.02)
plt.show()
