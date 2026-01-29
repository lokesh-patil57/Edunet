import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


df = pd.read_csv(r"C:\Users\lucky\OneDrive\Desktop\Edunet\iris.csv")



# df = pd.read_csv("iris.csv")

# Basic Histograms
df.hist(figsize=(10,8))
plt.suptitle("Feature Distributions", fontsize=16)
# plt.show()



# Scatterplot
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")
plt.title("Sepal Length vs Sepal Width")
# plt.show()

# pair plot
sns.pairplot(df, hue="species")
# plt.show()

# boxplot 
sns.boxplot(data=df, x="species", y="petal_length")
plt.title("Petal Length Distribution by Species")
plt.show()

sns.violinplot(data=df, x="species", y="petal_length")
plt.title("Petal Length Violin Plot by Species")
# plt.show()

# heatmap
corr = df.drop(columns="species").corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
# plt.show()

# pca 
from sklearn.decomposition import PCA

X = df.drop(columns="species")
pca = PCA(n_components=2)
components = pca.fit_transform(X)

df["PC1"] = components[:,0]
df["PC2"] = components[:,1]

sns.scatterplot(data=df, x="PC1", y="PC2", hue="species")
plt.title("PCA Projection of Iris Dataset")
# plt.show()

#create a heatmap to show the correlation matrix
correlation_matrix = df.select_dtypes(include=[np.number]).corr()
#plot heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',linewidths=0.5)
#add title
plt.title("Correlation Between Sources")
plt.show()


# create a Box plot
sns.boxplot(data=df)

#add title
plt.title("Distribution of Energy Consumption by source")
plt.show()

#create a violin plot
sns.violinplot(data=df)
#add title
plt.title("Violin Plot of Energy Consumption Disstribution ")
plt.show()