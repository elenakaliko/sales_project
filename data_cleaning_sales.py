import pandas as pd

# data loading
sales = pd.read_csv(
    r'C:\Users\User\Sales.csv'
)
print("------------------------------------")
print("Loaded sales data:")
print(sales.info())
print("------------------------------------")
print(sales.head(5))
print("------------------------------------")
count = sales['Order_ID'].count()
print("Count of Order_ID before cleaning:", count)
print("------------------------------------")

# data cleaning

df = sales.drop_duplicates()

print(df[['Total Sales', 'Total Cost']].isna().sum())
if df['Total Cost'].isna().sum().sum() > 0 or df['Total Sales'].isna().sum().sum() > 0 or (df['Total Sales'] < 0).any() or (df['Total Cost'] < 0).any():
    df = df.fillna({'Total Sales': 0, 'Total Cost': 0})
    
df = df.dropna()

if (df['Total Sales'] < 0).any() or (df['Total Cost'] < 0).any():
    print("Negative values found in 'Total Sales'", (df['Total Sales'] < 0).any() )
    print("Negative values found in 'Total Cost'", (df['Total Cost'] < 0).any() )
    df_negative = df[(df['Total Sales'] < 0) & (df['Total Cost'] < 0)]
    print("Rows with negative values loaded to a specific dataset for further reconciliation")
    df = df[(df['Total Sales'] >= 0) & (df['Total Cost'] >= 0)]
    print("Removed rows with negative values")
    print("------------------------------------")

print(df['ReturnFlag'].unique())
df['ReturnFlag'] = df['ReturnFlag'].str.strip().str.upper()
df['ReturnFlag'] = df['ReturnFlag'].astype('category')

# data format
df['Date_ID'] = pd.to_datetime(df['Date_ID'], format="%d/%m/%Y")
df['year'] = df['Date_ID'].dt.year
df['month'] = df['Date_ID'].dt.month
df['day'] = df['Date_ID'].dt.day

df['Customer Group'] = df['Customer Group'].str.strip().str.title()
df['Data source'] = df['Data source'].str.strip().str.title()

df['Customer Group'] = df['Customer Group'].astype('category')
df['Data source'] = df['Data source'].astype('category')


count = df['Order_ID'].count()
print("Count of Order_ID after cleaning: ", count)

df.columns = df.columns.str.lower().str.replace(' ', '_')

# data saving
df.to_csv("Sales_Data_cleaned.csv", index=False, encoding="utf-8")
print("------------------------------------")
print("Cleaned data saved to 'Sales_Data_cleaned.csv'")
if 'df_negative' in globals():
    df_negative.to_csv("Sales_Data_for_reconciliation.csv", index=False, encoding="utf-8")
    print("Rows with negative values saved to 'Sales_Data_for_reconciliation.csv'")

print("------------------------------------")
print("END OF PROCESS")