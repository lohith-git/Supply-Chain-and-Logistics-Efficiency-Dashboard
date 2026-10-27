import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration to wide mode
st.set_page_config(layout="wide")

# Load the cleaned dataset
df = pd.read_csv('cleaned_supply_chain_data.csv')

# Title of the app
st.title(" Supply Chain Analytics Dashboard")
st.markdown("""
This dashboard provides insights into the supply chain data of a Fashion and Beauty startup, focusing on product performance, shipping performance, and more.
""")

# Add collapsible dataset viewer
with st.expander("Click to view the dataset", expanded=False):
    st.dataframe(df.head(10), use_container_width=True)

# Sidebar filters
st.sidebar.header("Filter Data")
product_filter = st.sidebar.multiselect("Select Product Type", df['Product type'].unique())
supplier_filter = st.sidebar.multiselect("Select Supplier", df['Supplier name'].unique())
location_filter = st.sidebar.multiselect("Select Location", df['Location'].unique())
carrier_filter = st.sidebar.multiselect("Select Carrier", df['Shipping carriers'].unique())

# Apply filters
if product_filter:
    df = df[df['Product type'].isin(product_filter)]
if supplier_filter:
    df = df[df['Supplier name'].isin(supplier_filter)]
if location_filter:
    df = df[df['Location'].isin(location_filter)]
if carrier_filter:
    df = df[df['Shipping carriers'].isin(carrier_filter)]

# Key Metrics Row
st.header("Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total Revenue", f"${df['Revenue generated'].sum():,.2f}")
with col2:
    st.metric("Total Orders", f"{df['Order quantities'].sum():,.0f}")
with col3:
    st.metric("Average Lead Time", f"{df['Lead times'].mean():.2f} days")
with col4:
    st.metric("Average Price", f"${df['Price'].mean():.2f}")
with col5:
    st.metric("Total Costs", f"${df['Costs'].sum():,.2f}")

# First Row of Visualizations
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.subheader("Product Sales")
    fig1 = px.bar(df, x='Product type', y='Number of products sold', title='Product Sales by Type')
    st.plotly_chart(fig1)

with row1_col2:
    st.subheader("Revenue by Product Type")
    fig2 = px.bar(df, x='Product type', y='Revenue generated', title='Revenue by Product Type')
    st.plotly_chart(fig2)

with row1_col3:
    st.subheader("Revenue Over Time")
    fig3 = px.line(df, x='Lead times', y='Revenue generated', title='Revenue Over Time (Lead Times)')
    st.plotly_chart(fig3)

# Second Row of Visualizations
row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.subheader("Revenue by Location")
    fig4 = px.bar(df, x='Location', y='Revenue generated', title='Revenue by Location')
    st.plotly_chart(fig4)

with row2_col2:
    st.subheader("Revenue by Demographics")
    fig5 = px.pie(df, names='Customer demographics', values='Revenue generated', title='Revenue by Demographics')
    st.plotly_chart(fig5)

with row2_col3:
    st.subheader("Price Distribution")
    fig6 = px.histogram(df, x='Price', title='Price Distribution')
    st.plotly_chart(fig6)

# Third Row of Visualizations
row3_col1, row3_col2, row3_col3 = st.columns(3)

with row3_col1:
    st.subheader("Lead Times vs. Order Quantities")
    fig7 = px.scatter(df, x='Lead times', y='Order quantities', title='Lead Times vs Order Quantities', trendline="ols")
    st.plotly_chart(fig7)

with row3_col2:
    st.subheader("Shipping Costs by Carrier")
    fig8 = px.bar(df, x='Shipping carriers', y='Shipping costs', title='Shipping Costs by Carrier')
    st.plotly_chart(fig8)

with row3_col3:
    st.subheader("Manufacturing Efficiency")
    fig9 = px.scatter(df, x='Manufacturing lead time', y='Manufacturing costs', title='Manufacturing Efficiency')
    st.plotly_chart(fig9)

# Fourth Row of Visualizations
row4_col1, row4_col2, row4_col3 = st.columns(3)

with row4_col1:
    st.subheader("Defect Rates")
    fig10 = px.bar(df, x='Supplier name', y='Defect rates', title='Defect Rates by Supplier')
    st.plotly_chart(fig10)

with row4_col2:
    st.subheader("Customer Demographics Distribution")
    fig11 = px.pie(df, names='Customer demographics', title='Distribution of Customer Demographics')
    st.plotly_chart(fig11)

with row4_col3:
    st.subheader("Profit Margin by Product Type")
    fig12 = px.bar(df, x='Product type', y='Profit Margin', title='Profit Margin by Product Type')
    st.plotly_chart(fig12)

# Fifth Row of Visualizations
row5_col1, row5_col2, row5_col3 = st.columns(3)

with row5_col1:
    st.subheader("Price to Revenue Ratio")
    fig13 = px.scatter(df, x='Price', y='Revenue generated', color='Product type', title='Price to Revenue Ratio by Product Type')
    st.plotly_chart(fig13)

with row5_col2:
    st.subheader("Cost to Revenue Ratio")
    fig14 = px.scatter(df, x='Costs', y='Revenue generated', color='Product type', title='Cost to Revenue Ratio by Product Type')
    st.plotly_chart(fig14)

with row5_col3:
    st.subheader("Profit Margin vs Price to Revenue Ratio")
    fig15 = px.scatter(df, x='Price to Revenue Ratio', y='Profit Margin', color='Product type', title='Profit Margin vs Price to Revenue Ratio')
    st.plotly_chart(fig15)

# Sixth Row of Visualizations
row6_col1, row6_col2, row6_col3 = st.columns(3)

with row6_col1:
    st.subheader("Defect Rate per Production Volume")
    fig16 = px.scatter(df, x='Production volumes', y='Defect rates', color='Supplier name', title='Defect Rate per Production Volume by Supplier')
    st.plotly_chart(fig16)

with row6_col2:
    st.subheader("Manufacturing Cost per Unit")
    fig17 = px.bar(df, x='Product type', y='Manufacturing costs', title='Manufacturing Cost per Unit by Product Type')
    st.plotly_chart(fig17)

with row6_col3:
    st.subheader("Manufacturing Lead Time by Supplier")
    fig18 = px.bar(df, x='Supplier name', y='Manufacturing lead time', title='Manufacturing Lead Time by Supplier')
    st.plotly_chart(fig18)

# Seventh Row of Visualizations
row7_col1, row7_col2, row7_col3 = st.columns(3)

with row7_col1:
    st.subheader("Lead Time Efficiency by Supplier")
    fig19 = px.scatter(df, x='Lead times', y='Lead Time Efficiency', color='Supplier name', title='Lead Time Efficiency by Supplier')
    st.plotly_chart(fig19)

with row7_col2:
    st.subheader("Days in Inventory")
    fig20 = px.area(df, x='Product type', y='Days in Inventory', title='Days in Inventory by Product Type')
    st.plotly_chart(fig20)

with row7_col3:
    st.subheader("Stock Turnover Rate by Product Type")
    fig21 = px.line(df, x='Product type', y='Stock Turnover Rate', title='Stock Turnover Rate by Product Type')
    st.plotly_chart(fig21)

# Eighth Row of Visualizations
row8_col1, row8_col2, row8_col3 = st.columns(3)

with row8_col1:
    st.subheader("Average Shipping Time by Carrier")
    fig22 = px.bar(df, x='Shipping carriers', y='Shipping times', color='Product type', barmode='group', title='Average Shipping Time by Carrier')
    st.plotly_chart(fig22)

with row8_col2:
    st.subheader("Shipping Cost per Unit by Carrier")
    shipping_cost_per_unit = df.pivot_table(index='Shipping carriers', values='Shipping costs')
    fig23, ax = plt.subplots()
    sns.heatmap(shipping_cost_per_unit, annot=True, cmap='YlGnBu', ax=ax)
    st.pyplot(fig23)

with row8_col3:
    st.subheader("Transportation Modes Distribution")
    fig24 = px.pie(df, names='Transportation modes', hole=0.3, title='Distribution of Transportation Modes')
    st.plotly_chart(fig24)


