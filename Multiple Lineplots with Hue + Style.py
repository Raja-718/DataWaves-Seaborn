# Experiment 28: Multiple Lineplots with Hue + Style
import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")

plt.figure(figsize=(8,5))
sns.lineplot(x="timepoint", y="signal", hue="event", style="region", data=fmri)
plt.title("Lineplot with Hue and Style")
plt.show()
