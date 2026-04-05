import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from datetime import datetime
import urllib.request

def fetch_csv_from_github(url):
    """Fetch CSV file from GitHub raw URL"""
    # Convert GitHub web URL to raw URL
    raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    print(f"Fetching data from: {raw_url}")
    df = pd.read_csv(raw_url)
    return df

def quality_check(df):
    """Check data quality and return report"""
    print("\n=== DATA QUALITY CHECK ===")
    print(f"Shape: {df.shape}")
    print(f"\nNull values:\n{df.isnull().sum()}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nFirst few rows:\n{df.head()}")
    return df.isnull().sum()

def fill_missing_values(df):
    """Fill missing values with mean"""
    print("\n=== FILLING MISSING VALUES ===")
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print("Found null values. Filling with mean...")
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                mean_val = df[col].mean()
                df[col].fillna(mean_val, inplace=True)
                print(f"  Filled {null_counts[col]} null values in '{col}' with mean: {mean_val:.4f}")
    else:
        print("No null values found!")
    return df

def generate_summary_stats(df):
    """Generate summary statistics"""
    print("\n=== SUMMARY STATISTICS ===")
    stats = {}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            stats[col] = {
                "mean": float(df[col].mean()),
                "median": float(df[col].median()),
                "std_dev": float(df[col].std()),
                "min": float(df[col].min()),
                "max": float(df[col].max())
            }
            print(f"\n{col}:")
            print(f"  Mean: {stats[col]['mean']:.4f}")
            print(f"  Median: {stats[col]['median']:.4f}")
            print(f"  Std Dev: {stats[col]['std_dev']:.4f}")
            print(f"  Min: {stats[col]['min']:.4f}")
            print(f"  Max: {stats[col]['max']:.4f}")
    return stats

def create_pairplot(df, output_dir):
    """Create and save pairplot visualization"""
    print("\n=== CREATING PAIR PLOT ===")
    plt.figure(figsize=(12, 10))

    # Check if there's a target column (like 'species' or 'Name')
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(numeric_cols) > 1:
        pairplot_df = df[numeric_cols]

        # Check for categorical column
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

        if categorical_cols:
            pairplot_df[categorical_cols[0]] = df[categorical_cols[0]]
            sns.pairplot(pairplot_df, hue=categorical_cols[0], diag_kind='kde')
        else:
            sns.pairplot(pairplot_df, diag_kind='kde')

        pairplot_path = os.path.join(output_dir, 'pairplot.png')
        plt.savefig(pairplot_path, dpi=150, bbox_inches='tight')
        print(f"Pair plot saved to: {pairplot_path}")
        plt.close()
    return

def save_as_json(df, stats, output_dir):
    """Save dataframe and statistics as JSON"""
    print("\n=== SAVING DATA AS JSON ===")

    current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f'extracted_data_{current_timestamp}.json')

    output_data = {
        "metadata": {
            "extraction_date": datetime.now().isoformat(),
            "total_records": len(df),
            "total_columns": len(df.columns)
        },
        "columns": df.columns.tolist(),
        "data": df.to_dict('records'),
        "summary_statistics": stats
    }

    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"Data saved to: {output_file}")
    return output_file

def main():
    """Main execution function"""
    github_url = "https://github.com/saiprashanthts1995/Github_action_practice/blob/main/iris.csv"

    # Create output directory
    current_date = datetime.now().strftime("%Y-%m-%d")
    output_dir = f"output/{current_date}"
    os.makedirs(output_dir, exist_ok=True)

    print(f"Output directory: {output_dir}")

    # Step 1: Fetch data
    print("\n=== STEP 1: FETCHING DATA ===")
    df = fetch_csv_from_github(github_url)

    # Step 2: Quality check
    print("\n=== STEP 2: QUALITY CHECK ===")
    quality_check(df)

    # Step 3: Fill missing values
    print("\n=== STEP 3: FILLING MISSING VALUES ===")
    df = fill_missing_values(df)

    # Step 4: Generate statistics
    print("\n=== STEP 4: GENERATING STATISTICS ===")
    stats = generate_summary_stats(df)

    # Step 5: Create visualization
    print("\n=== STEP 5: CREATING VISUALIZATION ===")
    create_pairplot(df, output_dir)

    # Step 6: Save as JSON
    print("\n=== STEP 6: SAVING DATA ===")
    save_as_json(df, stats, output_dir)

    print("\n=== EXTRACTION COMPLETE ===")
    print(f"All outputs saved to: {output_dir}")

if __name__ == "__main__":
    main()
