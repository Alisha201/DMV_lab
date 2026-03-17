import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel("DATASET.xlsx")


df = df.dropna(axis=1, how='all')


df['population'] = pd.to_numeric(df['population'], errors='coerce')



# Numerical → Mean
for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Categorical → Mode
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("✅ Missing values after filling:\n")
print(df.isnull().sum())


top_data = df.groupby("country")["population"].sum().sort_values(ascending=False).head(10)

plt.figure()
top_data.plot(kind='bar')
plt.title("Top 10 Countries by Population")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


top5 = df.groupby("country")["population"].sum().sort_values(ascending=False).head(5)

plt.figure()
plt.pie(top5, labels=top5.index, autopct='%1.1f%%')
plt.title("Population Share (Top 5 Countries)")
plt.show()



country_name = df['country'].iloc[0]  # first country
country_data = df[df['country'] == country_name].sort_values("year")

plt.figure()
plt.step(country_data["year"], country_data["population"], where='mid')
plt.title(f"Population Trend (Stair Chart) - {country_name}")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid()
plt.show()


df.to_excel("Cleaned_DATASET.xlsx", index=False)

print("\n✅ All charts generated + dataset saved!")