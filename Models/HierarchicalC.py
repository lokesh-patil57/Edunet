import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('Models/CSV/environmental_socioeconomic.csv')
data.head()

from sklearn.preprocessing import StandardScaler
# Normalize the features using StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
# Display scaled data
print(pd.DataFrame(data_scaled, columns=data.columns).head())

import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# Create a dendrogram to visualize the hierarchical clustering process
plt.figure(figsize=(10, 7))
dendrogram = sch.dendrogram(sch.linkage(data_scaled, method='ward'))
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Index')
plt.ylabel('Euclidean Distance')
plt.show()

# Apply Agglomerative Clustering
# Let's assume we decide on 4 clusters based on the dendrogram
hierarchical_clustering = AgglomerativeClustering(n_clusters=4, 
                                                  affinity='euclidean', linkage='ward')

data['cluster'] = hierarchical_clustering.fit_predict(data_scaled)

# Display the first few rows with cluster labels
print(data.head())

from sklearn.metrics import silhouette_score
# Calculate Silhouette Score
sil_score = silhouette_score(data_scaled, data['cluster'])
print(f'Silhouette Score: {sil_score}')

import seaborn as sns
# Visualize the clusters using two features: 'co2_emissions' and 'waste_production'
plt.figure(figsize=(8, 6))
# Create a scatter plot with cluster labels
sns.scatterplot(x='co2_emissions', y='waste_production', hue='cluster', 
                data=data, palette='viridis', s=100, alpha=0.7, edgecolor='k')
# Title and labels
plt.title('Hierarchical Clustering of Environmental and Socioeconomic Factors')
plt.xlabel('CO₂ Emissions')
plt.ylabel('Waste Production')
plt.legend(title='Cluster', bbox_to_anchor=(1.05, 1), loc='upper left')
# Display the plot
plt.show()

