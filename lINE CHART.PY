import pandas as pd
import matplotlib.pyplot as pt
data = pd.read_csv("your_data_file.csv")
# Plot line chart for year-over-year automobile sales
pt.figure(figsize=(10, 6))
pt.plot(data['Year'], data['Total_Sales'], marker='o', color='b')
pt.title('Yearly Automobile Sales')
pt.xlabel('Year')
pt.ylabel('Total Sales')
pt.show()
# Filter data for recession periods if data has a 'Recession' column
recession_data = data[data['Recession'] == True]

# Plot different lines for each vehicle type
pt.figure(figsize=(12, 8))
for vehicle_type in data['Vehicle_Type'].unique():
    type_data = recession_data[recession_data['Vehicle_Type'] == vehicle_type]
    pt.plot(type_data['Year'], type_data['Sales'], label=vehicle_type, marker='o')

pt.title('Sales Trends by Vehicle Type During Recession')
pt.xlabel('Year')
pt.ylabel('Sales')
pt.legend()
pt.show()
import seaborn as sns

# Filter data for recession and non-recession
non_recession_data = data[data['Recession'] == False]

# Plot using Seaborn's lineplot for comparison
pt.figure(figsize=(12, 8))
sns.lineplot(data=recession_data, x='Year', y='Sales', hue='Vehicle_Type', marker='o', label='Recession Period')
sns.lineplot(data=non_recession_data, x='Year', y='Sales', hue='Vehicle_Type', marker='x', linestyle='--', label='Non-Recession Period')
pt.title('Sales Trend Comparison by Vehicle Type (Recession vs. Non-Recession)')
pt.xlabel('Year')
pt.ylabel('Sales')
pt.legend()
pt.show()
fig, ax = pt.subplots(1, 2, figsize=(14, 6))

# Recession period GDP
sns.lineplot(data=recession_data, x='Year', y='GDP', ax=ax[0], marker='o')
ax[0].set_title('GDP During Recession')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('GDP')

# Non-recession period GDP
sns.lineplot(data=non_recession_data, x='Year', y='GDP', ax=ax[1], marker='o')
ax[1].set_title('GDP During Non-Recession')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('GDP')

pt.tight_layout()
pt.show()
# Add seasonality and sales columns to plot bubble sizes based on sales volume
pt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Month', y='Sales', size='Sales', hue='Season', sizes=(20, 200), legend=False)
pt.title('Seasonality Impact on Automobile Sales')
pt.xlabel('Month')
pt.ylabel('Sales')
pt.show()
pt.figure(figsize=(10, 6))
sns.scatterplot(data=recession_data, x='Average_Price', y='Sales_Volume', hue='Vehicle_Type')
pt.title('Average Vehicle Price vs Sales Volume During Recessions')
pt.xlabel('Average Price')
pt.ylabel('Sales Volume')
pt.show()
# Sum of advertising expenses for each period
ad_expense = data.groupby(['Recession'])['Advertising_Expense'].sum()

pt.figure(figsize=(8, 8))
pt.pie(ad_expense, labels=['Non-Recession', 'Recession'], autopct='%1.1f%%', startangle=140)
pt.title('Advertising Expenditure during Recession vs Non-Recession')
pt.show()
# Filter recession period and group by vehicle type
recession_ad_expense = recession_data.groupby('Vehicle_Type')['Advertising_Expense'].sum()

pt.figure(figsize=(8, 8))
pt.pie(recession_ad_expense, labels=recession_ad_expense.index, autopct='%1.1f%%', startangle=140)
pt.title('Advertising Expenditure by Vehicle Type During Recession')
pt.show()
pt.figure(figsize=(12, 8))
for vehicle_type in recession_data['Vehicle_Type'].unique():
    type_data = recession_data[recession_data['Vehicle_Type'] == vehicle_type]
    pt.plot(type_data['Year'], type_data['Unemployment_Rate'], label=vehicle_type, marker='o')

pt.title('Unemployment Rate vs Vehicle Sales During Recession')
pt.xlabel('Year')
pt.ylabel('Unemployment Rate')
pt.legend()
pt.show()
