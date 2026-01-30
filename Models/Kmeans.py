from pathlib import Path
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


def load_data(path: str | None = None) -> pd.DataFrame:

    if path:
        data_path = Path(path)
    else:
        data_path = Path(__file__).resolve().parent / "CSV" / "environmental factors.csv"

    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found at: {data_path}")

    df = pd.read_csv(data_path)
    return df


def scale_data(df: pd.DataFrame) -> np.ndarray:
    """Scale numeric features using StandardScaler"""
    scaler = StandardScaler()
    # Use all numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    data_scaled = scaler.fit_transform(df[numeric_cols])
    return data_scaled, numeric_cols


def plot_elbow(data_scaled: np.ndarray, k_max: int = 10) -> None:
    """Plot inertia for k in 1..k_max to find the elbow"""
    inertia = []
    k_range = range(1, k_max + 1)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data_scaled)
        inertia.append(kmeans.inertia_)

    plt.figure()
    plt.plot(k_range, inertia, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Inertia')
    plt.xticks(k_range)
    plt.grid(True)
    plt.show()


def fit_kmeans_and_label(df: pd.DataFrame, data_scaled: np.ndarray, n_clusters: int = 7) -> pd.DataFrame:
    """Fit KMeans and attach cluster labels to a copy of the dataframe."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(data_scaled)
    df_out = df.copy()
    df_out['cluster'] = labels
    return df_out, kmeans


def plot_clusters(df: pd.DataFrame, numeric_cols: pd.Index) -> None:
    """Scatter plot of clusters using two sensible features."""
    # Preferred columns (as in the notebook); fallback to first two numeric cols
    preferred = [col for col in ['carbon_emissions', 'pollution_level'] if col in df.columns]
    if len(preferred) >= 2:
        x_col, y_col = preferred[0], preferred[1]
    else:
        if len(numeric_cols) < 2:
            print("Not enough numeric columns to plot clusters.")
            return
        x_col, y_col = numeric_cols[0], numeric_cols[1]

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x_col, y=y_col, hue='cluster', data=df, palette='viridis', s=100, alpha=0.7, edgecolor='k')
    plt.title('K-Means Clustering of Environmental Factors')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend(title='Cluster', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()


def main(argv=sys.argv[1:]):
    # Allow passing a custom CSV path as the first argument
    csv_path = argv[0] if len(argv) >= 1 else None

    print("Loading data...")
    df = load_data(csv_path)
    print("First 5 rows:")
    print(df.head())

    print("\nScaling data...")
    data_scaled, numeric_cols = scale_data(df)
    print(pd.DataFrame(data_scaled, columns=numeric_cols).head())

    print("\nPlotting Elbow method (close plot window to continue)...")
    plot_elbow(data_scaled, k_max=10)

    # Fit with k=7 as in the notebook
    k = 7
    print(f"\nFitting KMeans with k={k}...")
    df_clustered, kmeans = fit_kmeans_and_label(df, data_scaled, n_clusters=k)

    print("First 5 rows with cluster labels:")
    print(df_clustered.head())

    print("\nCalculating Silhouette Score...")
    try:
        sil_score = silhouette_score(data_scaled, df_clustered['cluster'])
        print(f"Silhouette Score: {sil_score}")
    except Exception as e:
        print(f"Could not compute silhouette score: {e}")

    print("\nPlotting clusters (close plot window to finish)...")
    plot_clusters(df_clustered, numeric_cols)

    # Optionally save results
    out_path = Path(__file__).resolve().parent / 'environmental_factors_clustered.csv'
    df_clustered.to_csv(out_path, index=False)
    print(f"Clustered data saved to: {out_path}")


if __name__ == "__main__":
    main()