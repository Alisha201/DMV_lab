import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding='ISO-8859-1')


countries = ['India', 'United States of America', 'United Kingdom', 'Australia']
df_filtered = df[df['Area'].isin(countries)]


year_cols = [col for col in df.columns if col.startswith('Y')]
year_cols = year_cols[:20]   

india_row = df_filtered[df_filtered['Area'] == 'India'].iloc[0]
usa_row = df_filtered[df_filtered['Area'] == 'United States of America'].iloc[0]
uk_row = df_filtered[df_filtered['Area'] == 'United Kingdom'].iloc[0]
aus_row = df_filtered[df_filtered['Area'] == 'Australia'].iloc[0]


india_temps = india_row[year_cols].values
usa_temps = usa_row[year_cols].values
uk_temps = uk_row[year_cols].values
australia_temps = aus_row[year_cols].values


years = [int(col[1:]) for col in year_cols]


fig, ax = plt.subplots()

ax.plot(years, india_temps, label='India')
ax.plot(years, usa_temps, label='USA')
ax.plot(years, uk_temps, label='UK')
ax.plot(years, australia_temps, label='Australia')

ax.set_xlabel('Year')
ax.set_ylabel('Temperature Change (°C)')
ax.set_title('Temperature Variation Over Years')

ax.legend()

plt.show()