# Sales Data Analysis

## 1. Project Overview

The **Sales Data Analysis** project is a beginner-level data analysis project developed using Python and Pandas.

The purpose of this project is to analyze sales data, clean the dataset, calculate important sales metrics, and identify useful business insights.

The project uses a dataset containing **100 sales records and 7 columns**.

## 2. Objectives

The main objectives of this project are:

* Load sales data using Pandas.
* Explore the structure of the dataset.
* Check data types and statistical information.
* Identify missing values and duplicate records.
* Clean the dataset.
* Calculate important sales metrics.
* Identify the best-selling product.
* Identify the product generating the highest revenue.
* Create a clear and formatted analysis report.

## 3. Technologies Used

* **Python**
* **Pandas**
* **CSV**
* **Markdown**

## 4. Dataset Description

The dataset contains 100 sales records with the following columns:

| Column      | Description                |
| ----------- | -------------------------- |
| Date        | Date of the sale           |
| Product     | Name of the product sold   |
| Quantity    | Number of units sold       |
| Price       | Price of the product       |
| Customer_ID | Unique customer identifier |
| Region      | Sales region               |
| Total_Sales | Total value of the sale    |

### Dataset Size

* **Rows:** 100
* **Columns:** 7

## 5. Data Exploration

Pandas functions were used to understand the dataset.

### First Five Rows

The first five records were displayed using:

```python
df.head()
```

### Dataset Shape

```python
df.shape
```

Result:

```text
(100, 7)
```

This means the dataset contains 100 rows and 7 columns.

### Data Types

The dataset contains:

* Integer values for Quantity, Price, and Total_Sales.
* String values for Date, Product, Customer_ID, and Region.

### Statistical Summary

The `df.describe()` function was used to calculate basic statistics.

Important results:

| Metric  | Quantity |     Price | Total Sales |
| ------- | -------: | --------: | ----------: |
| Average |     4.78 | 25,808.51 |  123,650.48 |
| Minimum |        1 |     1,308 |       6,540 |
| Maximum |        9 |    49,930 |     373,932 |

## 6. Data Cleaning

The dataset was checked for missing values and duplicate records.

### Missing Values

```python
df.isnull().sum()
```

Result:

```text
All columns: 0 missing values
```

Therefore, there were no missing values that needed to be removed.

### Duplicate Records

```python
df.duplicated().sum()
```

Result:

```text
0
```

Therefore, the dataset contained no duplicate records.

The dataset was still passed through the cleaning process to ensure that the data was ready for analysis.

## 7. Sales Analysis

Several important metrics were calculated using Pandas.

### Total Revenue

```python
total_revenue = df["Total_Sales"].sum()
```

**Total Revenue: $12,365,048.00**

### Total Quantity Sold

```python
total_quantity = df["Quantity"].sum()
```

**Total Quantity Sold: 478 units**

### Average Sale

```python
average_sale = df["Total_Sales"].mean()
```

**Average Sale: $123,650.48**

### Best-Selling Product

The quantity sold was grouped by product:

```python
product_quantity = df.groupby("Product")["Quantity"].sum()
```

The product with the highest quantity was identified using:

```python
best_selling_product = product_quantity.idxmax()
```

**Best-Selling Product: Laptop**

**Quantity Sold: 136 units**

### Highest Revenue Product

Revenue was grouped by product:

```python
product_revenue = df.groupby("Product")["Total_Sales"].sum()
```

The product generating the highest revenue was:

**Laptop — $3,889,210.00**

## 8. Key Findings

The analysis produced the following findings:

1. The dataset contains **100 sales transactions**.
2. The total quantity sold was **478 units**.
3. The total recorded revenue was **$12,365,048.00**.
4. The average sale value was **$123,650.48**.
5. **Laptop** was the best-selling product based on quantity.
6. Laptop also generated the highest revenue.
7. The dataset contained **no missing values**.
8. The dataset contained **no duplicate records**.

## 9. Testing

The program was tested by running the complete Python script and checking the generated output.

The following areas were verified:

* CSV file loads successfully.
* Dataset displays correctly.
* Dataset shape is correctly identified.
* Column names are displayed.
* Data types are identified.
* Missing values are checked.
* Duplicate records are checked.
* Total revenue is calculated.
* Total quantity is calculated.
* Average sale is calculated.
* Best-selling product is identified.
* Highest-revenue product is identified.

## 10. Project Structure

```text
sales-data-analysis/
│
├── sales_analysis.py
├── sales_data.csv
├── analysis_report.md
├── requirements.txt
└── screenshots/
    ├── data_loaded.png
    ├── data_exploration.png
    ├── data_cleaning.png
    └── sales_analysis.png
```

## 11. How to Run the Project

### Step 1: Install Pandas

```bash
pip install pandas
```

### Step 2: Open the project directory

Navigate to the project folder using the terminal.

### Step 3: Run the Python program

```bash
python sales_analysis.py
```

The program will load the CSV file, explore and clean the data, and display the sales analysis results.

## 12. Learning Outcomes

Through this project, I learned:

* How to install and use Pandas.
* How to read CSV files using Python.
* How to work with Pandas DataFrames.
* How to explore a dataset.
* How to identify missing values.
* How to detect duplicate records.
* How to perform basic data cleaning.
* How to calculate statistics using Pandas.
* How to group data using `groupby()`.
* How to identify maximum values using `idxmax()`.
* How to generate useful insights from real-world data.

## 13. Conclusion

The Sales Data Analysis project demonstrates the basic process of working with real-world data using Python and Pandas.

The dataset was successfully loaded, explored, checked for data-quality issues, cleaned, and analyzed.

The analysis showed that the total recorded revenue was **$12,365,048.00**, with **478 units sold**. Laptop was identified as both the best-selling product by quantity and the highest-revenue product.

This project provided practical experience with the fundamental concepts of data analysis and Pandas.
