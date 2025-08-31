# Experiment 27: Time Series Lineplot with Confidence Interval
import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")

plt.figure(figsize=(8,5))
sns.lineplot(x="timepoint", y="signal", data=fmri, ci="sd")
plt.title("Time Series Lineplot with Confidence Interval")
plt.show()
