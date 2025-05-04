"""
Fruit Inventory Analyzer (Lab 5 Adaptation for Cars Dataset)

This program allows interactive exploration, cleaning, and visualization
of a car dataset. Uses pandas, numpy, matplotlib, seaborn.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

# 📁 Always load the CSV file from the same directory as this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, 'cars_data.csv')

def load_data(file_path=CSV_FILE):
    """Loads the car dataset from CSV into a DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Loaded {len(df)} rows from {file_path}")
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return pd.DataFrame()

def drop_unnecessary_columns(df):
    """Drops columns that are not useful for analysis."""
    columns_to_drop = ['Engine Cylinders', 'Number of Doors', 'Market Category', 'Popularity']
    return df.drop(columns=[col for col in columns_to_drop if col in df.columns])

def show_basic_overview(df):
    """Displays head, tail, shape, and descriptive statistics."""
    print("🔍 First 5 rows:\n", df.head())
    print("🔍 Last 5 rows:\n", df.tail())
    print(f"📊 Shape: {df.shape}")
    print("📈 Description:\n", df.describe(include='all'))

def convert_qualitative_to_quantitative(df):
    """Converts 'Brand' column to numeric IDs."""
    if 'Brand' not in df.columns:
        print("⚠️ Column 'Brand' not found.")
        return df
    df['Brand_ID'] = pd.factorize(df['Brand'])[0]
    print("✅ Converted 'Brand' to numeric IDs.")
    return df

def merge_multiple_csvs():
    """Merges all CSV files in the folder that start with 'cars_dat'."""
    csv_files = glob.glob("cars_dat*.csv")
    if not csv_files:
        print("⚠️ No matching CSV files found.")
        return pd.DataFrame()
    dfs = [pd.read_csv(file) for file in csv_files]
    merged_df = pd.concat(dfs, ignore_index=True)
    print(f"✅ Merged {len(csv_files)} files with total {len(merged_df)} rows.")
    return merged_df

def rename_columns(df):
    """Renames some common columns for clarity."""
    return df.rename(columns={'Make': 'Brand', 'MSRP': 'Price'})

def drop_null_values(df):
    """Removes rows with missing (NaN) values."""
    return df.dropna()

def summarize_data(df):
    """Prints summary statistics for selected columns."""
    for col in ['Year', 'Price']:
        if col in df.columns:
            print(f"\n📊 Summary for {col}:")
            print(f"Count: {df[col].count()}")
            print(f"Mean: {df[col].mean():.2f}")
            print(f"Median: {df[col].median():.2f}")
            print(f"5th percentile: {np.percentile(df[col], 5):.2f}")
            print(f"95th percentile: {np.percentile(df[col], 95):.2f}")

def drop_outliers(df):
    """Removes rows where 'Year' is outside 5th–95th percentile."""
    if 'Year' not in df.columns:
        print("⚠️ Column 'Year' not found.")
        return df
    lower, upper = np.percentile(df['Year'], [5, 95])
    df = df[(df['Year'] >= lower) & (df['Year'] <= upper)]
    print(f"✅ Removed outliers outside {lower:.1f}–{upper:.1f} for 'Year'")
    return df

def plot_data(df):
    """Creates plots for data visualization."""
    if 'Engine HP' in df.columns and 'Price' in df.columns:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='Engine HP', y='Price', data=df)
        plt.title('Engine HP vs Price')
        plt.show()

    if 'Price' in df.columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(df['Price'], kde=True)
        plt.title('Price Distribution')
        plt.show()

    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

def save_data(df, filename='cars_data_cleaned.csv'):
    """Saves the cleaned data to a new CSV file."""
    output_path = os.path.join(SCRIPT_DIR, filename)
    df.to_csv(output_path, index=False)
    print(f"💾 Data saved to {output_path}")

def show_menu():
    """Displays all menu options."""
    print("""
========== 🚗 Car Dataset Menu ==========
1. Drop unnecessary columns
2. Show basic data overview
3. Convert 'Brand' to numeric ID
4. Merge CSV files (cars_dat*.csv)
5. Rename columns
6. Drop rows with missing values
7. Show summary statistics
8. Drop outliers in 'Year'
9. Plot visualizations
10. Exit and save
=========================================
""")

def main():
    df = load_data()
    while True:
        show_menu()
        choice = input("📌 Enter your choice (1-10): ")
        if choice == '1':
            df = drop_unnecessary_columns(df)
        elif choice == '2':
            show_basic_overview(df)
        elif choice == '3':
            df = convert_qualitative_to_quantitative(df)
        elif choice == '4':
            df = merge_multiple_csvs()
        elif choice == '5':
            df = rename_columns(df)
        elif choice == '6':
            df = drop_null_values(df)
        elif choice == '7':
            summarize_data(df)
        elif choice == '8':
            df = drop_outliers(df)
        elif choice == '9':
            plot_data(df)
        elif choice == '10':
            save_data(df)
            print("👋 Exiting program. Bye!")
            break
        else:
            print("❌ Invalid input. Please enter a number from 1 to 10.")

if __name__ == '__main__':
    main()
