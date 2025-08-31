# Experiment 32: KDE Plot with Shade=True
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

plt.figure(figsize=(7,5))
sns.kdeplot(data=iris, x="sepal_width", shade=True, color="purple", lw=2)
plt.title("KDE Plot with Shading (Sepal Width)")
plt.show()
