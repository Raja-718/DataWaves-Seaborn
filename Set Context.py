# Experiment 17: Set Context (paper, notebook, talk, poster)
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_context("talk")  # options: paper, notebook, talk, poster

plt.figure(figsize=(6,4))
sns.histplot(tips['tip'], bins=15, kde=True)
plt.title("Seaborn Context: Talk")
plt.show()
