# Retail Sales Analytics - Project Summary

## Project Overview

A comprehensive retail sales analytics project that analyzes retail sales data to identify trends in revenue, profit, and product performance across regions and categories. This project demonstrates end-to-end data analysis workflow from data cleaning to visualization and business intelligence.

### Project Objectives

- Perform data cleaning and transformation to ensure data accuracy
- Conduct exploratory data analysis (EDA) to understand data patterns
- Identify key business insights such as top products, sales trends, and regional performance
- Create professional visualizations and an interactive Power BI dashboard
- Generate actionable business insights for data-driven decision making

## Tools & Technologies Used

| **Programming** | Python 3.12 |
| **Data Analysis** | Pandas, NumPy |
| **Data Visualization** | Matplotlib, Seaborn |
| **BI & Dashboard** | Microsoft Power BI |

## Step-by-Step Analysis

### Data Loading & Exploration

- Load retail sales CSV dataset with UTF-8 encoding
- Examine first few rows and data structure
- Check data types, missing values, and statistical summary
- Dataset contains 9,994 rows and 21 columns

### Data Cleaning & Preprocessing

- Remove duplicate records
- Handle missing values (none found in this dataset)
- Convert date columns (Order Date, Ship Date) to datetime format
- Ensure data consistency and accuracy

### Exploratory Data Analysis (EDA)

- Analyze data distributions
- Identify outliers and patterns
- Generate summary statistics
- Understand overall data structure and relationships

### Sales Trend Analysis

- Analyze monthly sales patterns
- Identify seasonal trends
- Visualize sales over time
- Detect peak and low sales periods

### Product Performance Analysis

- Identify top 10 products by sales
- Identify top 10 products by profit
- Analyze category performance
- Compare product profitability

### Regional Analysis

- Analyze sales by region (West, East, Central, South)
- Compare regional profitability
- Create region-category cross-tabulation
- Identify best and worst performing regions

### Correlation Analysis

- Calculate correlation matrix for numeric variables
- Visualize relationships using heatmaps
- Identify key variable relationships (Sales, Profit, Quantity, Discount)

### Export Cleaned Data

- Export cleaned dataset to CSV for Power BI
- Final data ready for dashboard creation

---

## Key Business Insights

### 1. Revenue Performance

- **Total Sales Generated**: $2,297,200.86
- **Total Profit**: $286,397.02
- **Dataset Size**: 9,994 transactions across 4 regions
- **Profit Margin**: ~12.5%

### 2. Product Insights

- **Top Performing Categories**: Technology, Office Supplies, Furniture
- **High-Performing Products**: Canon imageCLASS, Fellowes PB500, Cisco TelePresence
- **Discount Impact**: Products with higher discounts show lower profit margins
- **Average Order Value**: $230 per transaction

### 3. Regional Performance

- **Strongest Region**: West (highest sales volume)
- **Profitability Leaders**: Central and East regions
- **Regional Distribution**: West > East > Central > South
- **Regional Variation**: Sales performance varies significantly across regions

### 4. Seasonal Patterns

- **Peak Sales Period**: Q4 (October-December)
- **Consistent Performance**: Sales trend relatively stable throughout year
- **Monthly Variation**: Clear peaks and troughs identified

### 5. Customer Behavior

- **Customer Segments**: Consumer (50.6%), Corporate (31.7%), Home Office (17.7%)
- **Consumer Segment**: Largest by volume, drives majority of sales
- **Corporate Segment**: Most profitable per transaction
- **Average Customers per Region**: Distributed across US

### 6. Key Relationships

- **Sales vs Profit**: Strong positive correlation
- **Discount vs Profit**: Negative correlation (discounts reduce margins)
- **Quantity vs Sales**: Direct positive relationship

---

## Key Visualizations

1. **Data Distribution** - Distribution of key numeric variables
2. **Monthly Sales Trend** - Line chart showing sales over time
3. **Sales by Month** - Aggregated monthly performance
4. **Top 10 Products** - Best performing products by revenue
5. **Top 10 Products (Profit)** - Most profitable products
6. **Category Analysis** - Sales and profit by product category
7. **Regional Analysis** - Performance comparison across regions
8. **Region-Category Heatmap** - Cross-dimensional analysis
9. **Correlation Heatmap** - Relationships between numeric variables

---

## Power BI Dashboard Components

### Page 1: Sales Overview

- KPIs: Total Sales, Total Profit, Average Order Value
- Visualizations:
  - Sales by Region (column chart)
  - Monthly Sales Trend (line chart)
  - Sales Distribution (pie chart)
- Filters: Region, Year, Month

### Page 2: Product Analysis

- Visualizations:
  - Top Products (horizontal bar chart)
  - Category Performance (column chart)
  - Product Profitability Matrix
- Filters: Category, Sub-category

### Page 3: Customer & Regional Trends

- Visualizations:
  - Sales by Region Map
  - Customer Segment Performance
  - Purchase Pattern Analysis
- Filters: Region, Segment, Time Period

---

## How to Use This Project

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn
```

### Running the Analysis

1. **Dataset Location**
   - Ensure `Sample - Superstore.csv` is in the `dataset/` folder

2. **Run the Python Script**

   ```bash
   python run_analysis.py
   ```    - Script will process data and generate all visualizations
          - Visualizations saved to `visuals/` folder
          - Cleaned data exported to `dataset/cleaned_sales_data.csv`
          - Total execution time: ~2-5 minutes

3. **Open Power BI Dashboard**

   - Open `powerbi/Retail_Sales_Dashboard.pbix` with Microsoft Power BI Desktop
   - View the 3-page interactive dashboard:
     - **Page 1**: Sales Overview (KPIs, trends, regional breakdown)
     - **Page 2**: Product Analysis (top products, categories)
     - **Page 3**: Customer Trends (segments, regional distribution)
   - Use slicers to filter by Region, Category, and Year

---

## Code Snippets

### Data Loading (With Correct Encoding)

```python
import pandas as pd
import numpy as np

# Load with latin-1 encoding (important for Windows CSV files)
df = pd.read_csv("dataset/Sample - Superstore.csv", encoding='latin-1')
print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
```

### Data Cleaning

```python
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
```

### Top Products Analysis

```python
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
```

### Regional Analysis

```python
region_sales = df.groupby('Region')['Sales'].sum()
region_profit = df.groupby('Region')['Profit'].sum()
```

### Visualizations with Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
corr = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.savefig('visuals/09_correlation_heatmap.png', dpi=300, bbox_inches='tight')
```

### Export Cleaned Data

```python
df.to_csv("dataset/cleaned_sales_data.csv", index=False)
```

---

## Key Metrics & KPIs

| **Total Sales** | Sum of all revenue | SUM(Sales) |
| **Total Profit** | Total profitability | SUM(Profit) |
| **Profit Margin** | Profitability percentage | (Profit/Sales) × 100 |
| **Average Order Value** | Mean transaction value | AVG(Sales per Order) |
| **Return on Discount** | Impact of discounts on profit | Analysis of Discount vs Profit |
| **Regional Performance** | Sales by geographic region | SUM(Sales) by Region |
| **Category Contribution** | Revenue contribution by category | % of Total Sales by Category |

---

## Data Quality Checks

- Duplicates removed
- Missing values handled
- Date formats standardized
- Data type conversions completed
- Outliers identified
- Data consistency verified

---

## Skills Demonstrated

- Data Analysis & Manipulation (Pandas, NumPy)
- Data Visualization (Matplotlib, Seaborn)
- Business Intelligence & Dashboard Creation (Power BI)
- Python Programming & Scripting
- Data Cleaning & Quality Assurance
- Time-Series Analysis
- Statistical Analysis

---

## Project Information

**Dataset**: Sample Superstore Dataset

**Data Size**: 9,994 transactions across 21 columns

**Key Columns**:

- Order Date, Ship Date, Ship Mode
- Region, Country, City, State
- Customer ID, Customer Name, Segment
- Product ID, Product Name, Category, Sub-Category
- Sales, Quantity, Discount, Profit
