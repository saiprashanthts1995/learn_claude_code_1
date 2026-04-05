import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
from io import StringIO
import urllib.request

# Step 1: Fetch the iris.csv from GitHub
url = "https://raw.githubusercontent.com/saiprashanthts1995/Github_action_practice/main/iris.csv"

print("Step 1: Fetching data from GitHub...")
try:
    df = pd.read_csv(url)
    print(f"✓ Data loaded successfully. Shape: {df.shape}")
except Exception as e:
    print(f"Error loading data: {e}")
    exit(1)

# Step 2: Quality check and handle missing values
print("\nStep 2: Quality Check and Handling Missing Values...")
print(f"Initial shape: {df.shape}")
print(f"\nMissing values before filling:")
print(df.isnull().sum())

# Fill missing values with mean
numeric_columns = df.select_dtypes(include=[np.number]).columns
for col in numeric_columns:
    if df[col].isnull().sum() > 0:
        mean_value = df[col].mean()
        df[col].fillna(mean_value, inplace=True)
        print(f"Filled {col} missing values with mean: {mean_value:.4f}")

print(f"\nMissing values after filling:")
print(df.isnull().sum())
print("✓ Quality check completed")

# Step 3: Summary statistics
print("\nStep 3: Summary Statistics")
print("="*70)
summary_stats = {
    'columns': {}
}

for col in numeric_columns:
    stats = {
        'mean': float(df[col].mean()),
        'median': float(df[col].median()),
        'std_dev': float(df[col].std()),
        'min': float(df[col].min()),
        'max': float(df[col].max()),
        'count': int(df[col].count())
    }
    summary_stats['columns'][col] = stats
    print(f"\n{col}:")
    print(f"  Mean:       {stats['mean']:.6f}")
    print(f"  Median:     {stats['median']:.6f}")
    print(f"  Std Dev:    {stats['std_dev']:.6f}")
    print(f"  Min:        {stats['min']:.6f}")
    print(f"  Max:        {stats['max']:.6f}")

# Step 4: Create pair plot visualization
print("\n\nStep 4: Creating Pair Plot Visualization...")
try:
    plt.figure(figsize=(12, 10))
    sns.pairplot(df, hue='Species' if 'Species' in df.columns else None, diag_kind='hist')
    plt.tight_layout()
    output_dir = '/Users/saiprashanththalanayarswaminathan/Desktop/Learning/Claude/output/2026-04-04'
    plot_path = f'{output_dir}/iris_pairplot.png'
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f"✓ Pair plot saved to {plot_path}")
    plt.close()
except Exception as e:
    print(f"Warning: Could not create pair plot: {e}")

# Step 5: Save data as JSON
print("\nStep 5: Saving Data as JSON...")
output_dir = '/Users/saiprashanththalanayarswaminathan/Desktop/Learning/Claude/output/2026-04-04'
json_path = f'{output_dir}/extracted_data.json'

# Prepare data for JSON
json_data = {
    'metadata': {
        'source': 'https://github.com/saiprashanthts1995/Github_action_practice/blob/main/iris.csv',
        'rows': len(df),
        'columns': list(df.columns)
    },
    'summary_statistics': summary_stats,
    'data': df.to_dict(orient='records')
}

# Save to JSON file
with open(json_path, 'w') as f:
    json.dump(json_data, f, indent=2)

print(f"✓ Data saved to {json_path}")
print(f"\nJSON file contains:")
print(f"  - Metadata (source, shape, columns)")
print(f"  - Summary statistics (mean, median, std dev for each column)")
print(f"  - Complete dataset with {len(df)} rows")

print("\n" + "="*70)
print("✓ All steps completed successfully!")
