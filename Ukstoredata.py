import pandas as pd
df=pd.read_csv("UK_Retail_dataa.csv")
print(df.head())
print (df.shape)
print(df.dtypes)
print (df.describe())

#duplicate_count=df.duplicated().sum()
#print(f"\n Number of duplicate rows : {duplicate_count}")
#if duplicate_count>0:
   # print("Duplicate rows found:")
#else:
 #   print("No duplicate rows found.")
#print(df[df.duplicated(keep=False)])


# Look at ACTUAL duplicate rows



duplicate_subset = [
    'InvoiceNo', 'StockCode', 'Description', 'Quantity', 
    'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'
]

true_duplicate_count = df[df.duplicated(subset=duplicate_subset, keep=False)].shape[0]
print(df[df.duplicated(subset=duplicate_subset, keep=False)].head(20))
print(f"\n Actual Number of TRUE Duplicate Rows (both original and copy included): {true_duplicate_count}")

rows_to_drop = df.duplicated(subset=duplicate_subset).sum()
print(f"Number of Duplicate Rows to DROP (only the second copy): {rows_to_drop}")

df = df.drop_duplicates()
print(f"Final row count: {len(df)}")

print(df.isnull().sum())

print(df[df["CustomerID"].isnull()].head(20))
print(df[df["Description"].isnull()].head(20))

df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
df['InvoiceDate'] = (df['InvoiceDate'])
df['CustomerID'] = df['CustomerID'].astype('Int64')  # This handles NaN properly


#there are neg values too in description along with nan in customer id and 1465 nan of description so like i think we would remove them all



# checking impact of missing custtomer id

missing_cust=df[df["CustomerID"].isnull()]
print(f"\n Transaction without missing customer id:{len(missing_cust)}")
print(f"\n Revenue without missing customer id:${(missing_cust["Quantity"]*missing_cust["UnitPrice"]).sum()}")
print(f"\n Transaction with missing customer id:{len(df)-len(missing_cust)}")
print(f"\n Revenue with missing cusomer id:${df["Quantity"]*df["UnitPrice"].sum()-(missing_cust["Quantity"]*missing_cust["UnitPrice"]).sum()}")


total_transactions=len(df)
total_revenue=df["Quantity"]*df["UnitPrice"].sum()

missing_cust_transactions=(135080/total_transactions)*100
missing_cust_revenue=(1447682/total_revenue)*100

print(f"\n Percentage of transactions with missing customer id:{missing_cust_transactions}%")
print(f"\n Percentage of revenue with missing customer id:{missing_cust_revenue}%")
# so we can remove missing customer id as it is only 0.5% of total transaction and revenue
df.dropna(subset=['CustomerID'], inplace=True)

df_clean=df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"]>0) &
    (df["CustomerID"].notna()) &
    (df["Description"].notna())
].copy()
df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['UnitPrice']

print(f"Cleaned rows: {len(df_clean):,}")
print(f"Removed: {len(df) - len(df_clean):,} rows ({((len(df) - len(df_clean)) / len(df) * 100):.1f}%)\n")

print(f"Unique customers: {df_clean['CustomerID'].nunique():,}")
print(f"Unique invoices: {df_clean['InvoiceNo'].nunique():,}")
print(f"\nDate range: {df_clean['InvoiceDate'].min()} to {df_clean['InvoiceDate'].max()}")
print(f"Total revenue: ${df_clean['TotalPrice'].sum():,.2f}")
#RFM
df_clean["InvoiceDate"]=pd.to_datetime(df_clean["InvoiceDate"])
snapshot_date=df_clean["InvoiceDate"].max()+pd.Timedelta(days=1)
rfm_r=df_clean.groupby("CustomerID").agg({
    "InvoiceDate":lambda x:(snapshot_date-x.max()).days,
})
rfm_r.rename(columns={"InvoiceDate":"Recency"},inplace=True)
print("\n RFM - Recency Scores")
print(rfm_r.head())

#Frequency, Monetary
rfm_fm=df_clean.groupby("CustomerID").agg({
    "InvoiceNo":"nunique",
    "TotalPrice":"sum"
})
rfm_fm.rename(columns={
    "InvoiceNo":"Frequency",
    "TotalPrice":"Monetary"
},inplace=True)
print("\n RFM - Frequency and Monetary Scores")
print(rfm_fm.head())

#combine all

rfm_df=rfm_r.join(rfm_fm)
rfm_df = rfm_df.reset_index()
print("\n Combined RFM Table")
print(rfm_df.head())
print(rfm_df.shape)

#Creating R, F M Scores

rfm_df["R_Score"]=pd.qcut(rfm_df["Recency"],5,labels=[5,4,3,2,1])
rfm_df["F_Score"]=pd.qcut(rfm_df["Frequency"].rank(method="first"),5,labels=[1,2,3,4,5])
rfm_df["M_Score"]=pd.qcut(rfm_df["Monetary"],5,labels=[1,2,3,4,5])

#combine RFM score
rfm_df["RFM_Score"]=rfm_df["R_Score"].astype(str)+rfm_df["F_Score"].astype(str)+rfm_df["M_Score"].astype(str)
print("\n RFM Scores")
print(rfm_df.head(10))

#Define Segments based on RFM Scores

def rfm_segment(row):
    r, f, m = int(row['R_Score']), int(row['F_Score']), int(row['M_Score'])
    

    if r >=4 and f >=4 and m >=4:
        return "Champions"
    elif f >=4:
        return "Loyal Customers"
    elif r<=2 and f>=3 and m>=3:
        return "At Risk"
    elif r<=2:
        return "Lost"
    elif r>=4 and f<=2:
        return "New Customers"
    elif r>=3 and f>=2:
        return "Potential Loyalist"
    else:
        return "Others"

rfm_df["Segment"]=rfm_df.apply(rfm_segment,axis=1)

#see segments
print("\n RFM Segments")
print(rfm_df["Segment"].value_counts())
print("/n Segment Summary")
segment_summary = rfm_df.groupby("Segment").agg({
    "CustomerID": "count",
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": ["mean", "sum"]
}).round(2)

print(segment_summary)

# Identify high-value At Risk customers
at_risk_high_value = rfm_df[
    (rfm_df['Segment'] == 'At Risk') & 
    (rfm_df['Monetary'] > rfm_df['Monetary'].quantile(0.75))
]

print(f"High-value At Risk customers: {len(at_risk_high_value)}")
print(f"Potential revenue recovery: ${at_risk_high_value['Monetary'].sum():,.2f}")

# Save the RFM analysis with segments
rfm_df.to_csv('customer_rfm_segments.csv', index=False)

# Save the segment summary
segment_summary.to_csv('segment_summary.csv')

print("Files saved!")

