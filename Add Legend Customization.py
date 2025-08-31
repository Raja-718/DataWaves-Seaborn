# Experiment 16: Add Legend Customization
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.scatterplot(x="total_bill", y="tip", hue="sex", style="smoker", data=tips)
plt.title("Custom Legend Example")
plt.legend(title="Customer Info", loc="upper left", frameon=True)
plt.show()
