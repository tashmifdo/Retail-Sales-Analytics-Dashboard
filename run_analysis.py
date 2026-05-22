#!/usr/bin/env python3
"""
Retail Sales Analytics - Data Processing & Visualization
Run with: python run_analysis.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

#Create output folder.
os.makedirs('visuals', exist_ok=True)

print("=" * 60)
print("RETAIL SALES ANALYTICS - STARTING ANALYSIS")
print("=" * 60)

#LOAD DATA WITH ENCODING
print("\n[1/10] Loading dataset...")
df = pd.read_csv('dataset/Sample - Superstore.csv', encoding='latin-1')
print(f"✓ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"✓ Columns: {list(df.columns)}")

#CHECK FOR MISSING VALUES
print("\n[2/10] Checking data quality...")
print(f"Missing values BEFORE cleaning:\n{df.isnull().sum().sum()}")

#CLEAN DATA
print("\n[3/10] Cleaning data...")
before_shape = df.shape
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)
print(f"✓ Duplicates removed: {before_shape[0]} → {df.shape[0]} rows")
print(f"✓ Missing values AFTER cleaning: {df.isnull().sum().sum()}")

#CONVERT DATES
print("\n[4/10] Converting date columns...")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
print("✓ Order Date and Ship Date converted to datetime")

#VISUALIZATION 1 - DATA DISTRIBUTION
print("\n[5/10] Creating Visualization 1: Data Distribution...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
for idx, col in enumerate(['Sales', 'Profit', 'Quantity', 'Discount']):
    if col in df.columns:
        ax = axes[idx//2, idx%2]
        df[col].hist(bins=30, ax=ax, color='skyblue', edgecolor='black')
        ax.set_title(f'Distribution of {col}', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('visuals/01_data_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart saved: 01_data_distribution.png")

#VISUALIZATION 2 - MONTHLY SALES TREND
print("\n[6/10] Creating Visualization 2: Monthly Sales Trend...")
df['Year_Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Year_Month')['Sales'].sum()
plt.figure(figsize=(14, 6))
monthly_sales.plot(kind='line', marker='o', color='#2E86AB', linewidth=2)
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visuals/02_monthly_sales_trend.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart saved: 02_monthly_sales_trend.png")

#VISUALIZATION 3 - SALES BY MONTH
print("\n[7/10] Creating Visualization 3: Sales by Month...")
df['Month'] = df['Order Date'].dt.month
monthly_agg = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(12, 6))
monthly_agg.plot(kind='bar', color='#A23B72', edgecolor='black')
plt.title('Sales by Month', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visuals/03_sales_by_month.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart saved: 03_sales_by_month.png")

#VISUALIZATION 4 & 5 - TOP PRODUCTS
print("\n[8/10] Creating Visualization 4-5: Top Products...")
if 'Product Name' in df.columns:
    top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 7))
    top_products.plot(kind='barh', color='#F18F01', edgecolor='black')
    plt.title('Top 10 Products by Sales', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('visuals/04_top_10_products.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart saved: 04_top_10_products.png")

    top_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 7))
    top_profit.plot(kind='barh', color='#06A77D', edgecolor='black')
    plt.title('Top 10 Products by Profit', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('visuals/05_top_10_products_profit.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart saved: 05_top_10_products_profit.png")

#VISUALIZATION 6 - CATEGORY ANALYSIS
print("\n[9/10] Creating Visualization 6-9: Advanced Analysis...")
if 'Category' in df.columns:
    cat_sales = df.groupby('Category')['Sales'].sum()
    cat_profit = df.groupby('Category')['Profit'].sum()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    cat_sales.plot(kind='bar', ax=axes[0], color='#FF6B6B', edgecolor='black')
    axes[0].set_title('Sales by Category', fontsize=12, fontweight='bold')
    cat_profit.plot(kind='bar', ax=axes[1], color='#4ECDC4', edgecolor='black')
    axes[1].set_title('Profit by Category', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig('visuals/06_category_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart saved: 06_category_analysis.png")

#VISUALIZATION 7 - REGIONAL ANALYSIS
if 'Region' in df.columns:
    region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    region_sales.plot(kind='bar', ax=axes[0], color='#95E1D3', edgecolor='black')
    axes[0].set_title('Sales by Region', fontsize=12, fontweight='bold')
    region_profit.plot(kind='bar', ax=axes[1], color='#F38181', edgecolor='black')
    axes[1].set_title('Profit by Region', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig('visuals/07_regional_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart saved: 07_regional_analysis.png")

#VISUALIZATION 8 - REGION-CATEGORY HEATMAP
if 'Region' in df.columns and 'Category' in df.columns:
    heatmap_data = pd.crosstab(df['Region'], df['Category'], values=df['Sales'], aggfunc='sum')
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt='.0f', cmap='YlGnBu')
    plt.title('Sales by Region and Category', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('visuals/08_region_category_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart saved: 08_region_category_heatmap.png")

#VISUALIZATION 9 - CORRELATION HEATMAP
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, square=True, linewidths=1)
plt.title('Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visuals/09_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart saved: 09_correlation_heatmap.png")

#EXPORT CLEANED DATA
print("\n[10/10] Exporting cleaned data...")
df.to_csv('dataset/cleaned_sales_data.csv', index=False)
print(f"✓ Cleaned data exported: cleaned_sales_data.csv")
print(f"✓ Total rows: {len(df)}")
print(f"✓ Total columns: {len(df.columns)}")

print("\n" + "=" * 60)
print(" ANALYSIS COMPLETE!")
print("=" * 60)
print("\nGenerated files:")
print("   Visualizations (PNG): visuals/01-09_*.png")
print("   Cleaned data (CSV): dataset/cleaned_sales_data.csv")
print("\nNext step: Import cleaned_sales_data.csv into Power BI")
print("=" * 60)
