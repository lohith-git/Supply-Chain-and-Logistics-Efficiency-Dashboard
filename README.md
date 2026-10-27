# Supply Chain and Logistics Efficiency Dashboard

## Project Description

The Supply Chain and Logistics Efficiency Dashboard is a Python-based analytical application built using Streamlit. It helps organizations analyze supply chain operations, monitor key performance indicators (KPIs), evaluate transportation costs, and identify opportunities to improve logistics efficiency.

The dashboard processes CSV datasets and presents interactive visualizations to support data-driven decision-making.

### Key Features

- Interactive dashboard with supply chain KPIs.
- Automated data cleaning and preprocessing.
- Revenue, manufacturing cost, and transportation cost analysis.
- Supplier performance and defect-rate analysis.
- Lead-time and delivery efficiency analysis.
- Product profitability and inventory insights.
- Interactive filters and data exploration.
- CSV dataset upload and analysis.
- Data export and reporting capabilities.

## Technology Stack

- **Programming Language:** Python 3.10
- **Dashboard Framework:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn, Plotly
- **Excel Integration:** OpenPyXL
- **Dataset Format:** CSV

## Project Requirements

### Software Requirements

- Windows 10/11 (64-bit recommended).
- Python 3.10 (recommended by the project documentation).
- pip package manager.
- Git (for cloning the repository).
- VS Code or PyCharm.
- Google Chrome or Microsoft Edge.

### Hardware Requirements

- **Processor:** Intel Core i3 or equivalent minimum.
- **RAM:** 4 GB minimum; 8 GB recommended.
- **Storage:** 2 GB minimum free space; 5 GB recommended.

## Dataset Setup

The project uses CSV datasets containing product, supplier, manufacturing cost, transportation cost, order quantity, lead time, revenue, profit, and regional information.

The following files are described in the project documentation:

- `supply_chain_data.csv` — Original dataset.
- `cleaned_supply_chain_data.csv` — Cleaned dataset used for analysis.

Place the dataset files in the project root directory alongside the Python scripts.

Example:

```text
Supply-Chain-Management-Dashboard/
├── main.py
├── supply_chain_dashboard.py
├── requirements.txt
├── supply_chain_data.csv
└── cleaned_supply_chain_data.csv
```

Ensure the dataset column names match those expected by the application.

## How to Run the Project Locally

### 1. Clone the Repository

Replace the placeholder with your GitHub repository URL.

```bash
git clone https://github.com/lohith-git/Supply-Chain-and-Logistics-Efficiency-Dashboard
cd your-repository
```

### 2. Create a Virtual Environment

Using Python 3.10:

```bash
py -3.10 -m venv venv
```

### 3. Activate the Environment

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Dashboard

```bash
streamlit run supply_chain_dashboard.py
```

### 6. Open the Application

Open the following URL in your browser:

```text
http://localhost:8501
```

## Future Enhancements

- Live supply chain data integration through APIs.
- Machine learning-based predictive analytics.
- Automated inventory alerts.
- Improved demand forecasting.
- Enterprise-level scalability.

## Conclusion

The Supply Chain and Logistics Efficiency Dashboard transforms raw supply chain data into actionable insights through interactive visualizations and KPI analysis. It helps businesses identify operational bottlenecks, monitor supplier performance, control costs, and improve logistics efficiency.
