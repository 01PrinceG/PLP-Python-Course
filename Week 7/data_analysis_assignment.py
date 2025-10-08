# ==============================================================
# Data Analysis and Visualization using Pandas and Matplotlib
# ==============================================================

# --- Import Libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1: Load and Explore the Dataset ---
print("=== Task 1: Load and Explore the Dataset ===")

try:
    # Load dataset (you can replace this URL with your own CSV file path)
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    data = pd.read_csv(url)
    print(" Dataset loaded successfully!")
except FileNotFoundError:
    print(" Error: The dataset file was not found.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")

# Display first few rows
print("\n--- First 5 Rows ---")
print(data.head())

# Checking data info and types
print("\n--- Dataset Info ---")
print(data.info())

# Checking for missing values
print("\n--- Missing Values ---")
print(data.isnull().sum())

# Clean dataset (drop rows with missing values, if any)
data = data.dropna()
print("\n Cleaned dataset (no missing values remaining).")

# --- Step 2: Basic Data Analysis ---
print("\n=== Task 2: Basic Data Analysis ===")

# Compute descriptive statistics
print("\n--- Statistical Summary ---")
print(data.describe())

# Group by species and compute mean values
grouped = data.groupby('species').mean(numeric_only=True)
print("\n--- Mean Measurements by Species ---")
print(grouped)

# Identify patterns / findings
print("\n--- Observations ---")
print("""
1. The dataset contains 150 flower samples divided equally into 3 species.
2. Petal and sepal dimensions differ significantly between species.
3. Virginica generally has the largest petal and sepal sizes, while Setosa has the smallest.
""")

# --- Step 3: Data Visualization ---
print("\n=== Task 3: Data Visualization ===")

# Use Seaborn style for better visuals
sns.set(style="whitegrid")

# Line Chart – Showing trend of petal length across dataset index
plt.figure(figsize=(8,5))
plt.plot(data['petal_length'], label='Petal Length', color='teal')
plt.title('Line Chart: Petal Length Trend')
plt.xlabel('Index')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# Bar Chart – Average sepal width per species
plt.figure(figsize=(8,5))
sns.barplot(x='species', y='sepal_width', data=data, palette='Set2')
plt.title('Bar Chart: Average Sepal Width per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Width (cm)')
plt.show()

# Histogram – Distribution of petal length
plt.figure(figsize=(8,5))
plt.hist(data['petal_length'], bins=15, color='skyblue', edgecolor='black')
plt.title('Histogram: Petal Length Distribution')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot – Sepal length vs Petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=data, palette='Dark2')
plt.title('Scatter Plot: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# --- My Findings ---
print("\n=== Findings and Observations ===")
print("""
🔹 The petal length increases steadily across samples, with visible variation between species.
🔹 The average sepal width is highest in Setosa species.
🔹 The histogram shows petal lengths are right-skewed for some species.
🔹 The scatter plot reveals clear separation between species — suggesting strong correlation between sepal and petal dimensions.
""")
