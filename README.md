# Sales Analysis Project – From Python Data Cleaning to Power BI Dashboard

## Project Overview
This project demonstrates the full workflow of working with sales data: from preprocessing raw CSV data in Python to creating a professional Power BI dashboard for business insights.  
The goal is to show both **data engineering skills** and **data visualization skills** in one cohesive project.

---

## Project Structure

portfolio_project_sales/ <br>
│
├── data/ <br>
│ └── Sales.csv # Raw dataset <br>
│
├
│ └── data_cleaning_sales.py # Python script for preprocessing <br>
│
├── power_bi_dashboard/ <br>
│ ├── In_a_nutshell.png <br>
│ ├── Zoom_on_Category.png <br>
│ └── Sales_mngr_perf.png <br>
|
├── images/ <br> # Power BI dashboard screenshots <br>
│ └── readme_1.png/ 
│ └── readme_2.png/ 
│
└── README.md # Project description <br>


---

## Steps Performed

### 1. Data Cleaning in Python
- Loaded raw CSV dataset (`Sales.csv`) using `pandas`  
- Converted date columns to proper datetime format  
- Checked and handled missing values, duplicates, and invalid entries  
- Cleaned and normalized text fields (`Customer Group`, `Data source`, `ReturnFlag`)  
- Converted numerical columns to correct data types (`Total Sales`, `Total Cost`)  
- Saved the cleaned dataset as `Sales_Data_cleaned.csv` for further analysis  

### 2. Data Analysis and Dashboard in Power BI
- Imported `Sales_Data_cleaned.csv` into Power BI  
- Created key performance indicators (KPIs):
  - Total Revenue  
  - Total Profit / Margin  
  - Year-over-Year Growth  
  - Percentage of Returned Items  
- Built visualizations:
  - Revenue trends over time  
  - Customer and product segmentation  
  - Interactive overview dashboard for management  
- Exported dashboard screenshots to include in the portfolio  

---

## Technologies Used
- Python (`pandas`) for data cleaning  
- Power BI for dashboard creation and visualization  

---

## How to Run the Python Code
1. Navigate to the `src/` folder:
Run the data cleaning script: python data_cleaning_sales.py
cd src

This will generate Sales_Data_cleaned.csv in the same folder or specified output path, ready for Power BI.
