import pandas as pd
import numpy as np

# 1. Load dataset
df = pd.read_excel("DATASET.xlsx")

print("Original Dataset:\n", df.head())

# 2. Find Missing Values
print("\nMissing Values in each column:")
print(df.isnull().sum())

# 3. Replace Missing Values
# Option 1: Replace with mean (for numerical columns)
df_filled = df.copy()

for col in df_filled.select_dtypes(include=np.number).columns:
    df_filled[col].fillna(df_filled[col].mean(), inplace=True)

# Option 2: Replace categorical missing values with mode
for col in df_filled.select_dtypes(include='object').columns:
    df_filled[col].fillna(df_filled[col].mode()[0], inplace=True)

print("\nDataset after handling missing values:\n", df_filled.head())

# 4. Detect Outliers using IQR method
def detect_outliers(df):
    outlier_indices = []

    for col in df.select_dtypes(include=np.number).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)].index
        outlier_indices.extend(outliers)

    return list(set(outlier_indices))

outliers = detect_outliers(df_filled)
print("\nOutlier row indices:", outliers)

# 5. Remove or Replace Outliers
# Option: Replace outliers with median
for col in df_filled.select_dtypes(include=np.number).columns:
    Q1 = df_filled[col].quantile(0.25)
    Q3 = df_filled[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    median = df_filled[col].median()

    df_filled[col] = np.where(
        (df_filled[col] < lower_bound) | (df_filled[col] > upper_bound),
        median,
        df_filled[col]
    )

print("\nDataset after handling outliers:\n", df_filled.head())


df_filled.to_excel("Cleaned_DATASET.xlsx", index=False)

print("\nCleaned dataset saved as 'Cleaned_DATASET.xlsx'")