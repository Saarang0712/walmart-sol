#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_excel('Walmart Sales (1).xlsx')


# In[3]:


df


# In[8]:


df.head()


# In[9]:


df.tail()


# In[11]:


#grouping_part #question A

city_branch_sales = df.groupby(['City', 'Branch'])['Sales'].sum().reset_index()

print("Sales by City and Branch:")
print(city_branch_sales)


# In[12]:


# Data visualization for sales by City and Branch
plt.figure(figsize=(12, 6))
plt.bar(city_branch_sales['City'] + ' - ' + city_branch_sales['Branch'], city_branch_sales['Sales'])
plt.xlabel('City - Branch')
plt.ylabel('Total Sales')
plt.title('Total Sales by City and Branch')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[13]:


# Calculate the average price of an item sold at each branch of the city
avg_price_per_branch_city = df.groupby(['City', 'Branch'])['Unit price'].mean().reset_index()

# Display the average price
print("\nAverage Price of an Item Sold at Each Branch of the City:")
print(avg_price_per_branch_city)


# In[14]:


# Data visualization for average price per branch of the city
plt.figure(figsize=(12, 6))
plt.bar(avg_price_per_branch_city['City'] + ' - ' + avg_price_per_branch_city['Branch'], avg_price_per_branch_city['Unit price'])
plt.xlabel('City - Branch')
plt.ylabel('Average Price')
plt.title('Average Price of an Item Sold at Each Branch of the City')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[18]:


# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='mm/dd/yyyy')

# Filter data for April 2019
april_data = df[df['Date'].dt.month == 4]

# Group by Month, Product line, Gender, and Payment Method, and calculate total sales and revenue
monthly_performance = april_data.groupby(['Date', 'Product line', 'Gender', 'Payment'])[['Quantity', 'Sales']].sum().reset_index()

# Display the result
print("Monthly Performance for April 2019:")
print(monthly_performance)


# In[19]:


df


# In[20]:


# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='mm/dd/yyyy')

# Filter data for April 2019
april_data = df[df['Date'].dt.month == 4]

# Group by Month, Product line, Gender, and Payment Method, and calculate total sales and revenue
monthly_performance = april_data.groupby(['Date', 'Product line', 'Gender', 'Payment'])[['Quantity', 'Sales']].sum().reset_index()

# Display the result
print("Monthly Performance for April 2019:")
print(monthly_performance)


# In[22]:


# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Group by Month, Product line, Gender, and Payment Method, and calculate total sales and revenue
monthly_performance = df.groupby([df['Date'].dt.month, 'Product line', 'Gender', 'Payment'])[['Quantity', 'Sales']].sum().reset_index()

# Display the result
print("Monthly Performance across Product Line, Gender, and Payment Method:")
print(monthly_performance)


# In[26]:


import seaborn as sns

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Group by Month, Product line, Gender, and Payment Method, and calculate total sales and revenue
monthly_performance = df.groupby([df['Date'].dt.month, 'Product line', 'Gender', 'Payment'])[['Quantity', 'Sales']].sum().reset_index()

# Data visualization
plt.figure(figsize=(14, 8))
sns.barplot(x='Date', y='Sales', hue='Product line', data=monthly_performance)
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Total Sales Month over Month by Product Line')
plt.legend(title='Product Line', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(range(1, 13), ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 8))
sns.barplot(x='Date', y='Sales', hue='Gender', data=monthly_performance)
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Total Sales Month over Month by Gender')
plt.legend(title='Gender', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(range(1, 13), ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 8))
sns.barplot(x='Date', y='Sales', hue='Payment', data=monthly_performance)
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Total Sales Month over Month by Payment Method')
plt.legend(title='Payment Method', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(range(1, 13), ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




