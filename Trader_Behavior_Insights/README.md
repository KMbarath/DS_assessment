# Data Science Intern Project: Trader Performance vs Market Sentiment

## Overview
This project analyzes how market sentiment (Fear/Greed Index) influences trader behavior and performance on the Hyperliquid platform. The analysis uncovers patterns to inform smarter trading strategies.

## Setup Instructions

1. **Environment Setup**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```

2. **Data Files**:
   - `fear_greed_index.csv`: Fear/Greed Index data
   - `historical_data.csv`: Historical trader data from Hyperliquid

3. **Run the Analysis**:
   - Open `DS_project.ipynb` in Jupyter
   - Run all cells to perform the complete analysis

4. **Run the Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```
   - **Interactive Features**: Select/deselect specific charts, apply real-time filters
   - **Customizable Views**: Choose from 10+ chart types based on your analysis needs

## Project Structure
- `DS_project.ipynb`: Main analysis notebook with advanced statistical modeling
- `dashboard.py`: **Interactive Streamlit dashboard with tabs, filters, and Plotly visualizations**
- `extract_pdf.py`: Script to extract project requirements from PDF
- `requirements.txt`: Python dependencies

## Key Findings
- Traders show higher win rates during Greed periods
- Behavioral changes occur based on market sentiment
- Different trader segments respond differently to sentiment

## Methodology
1. Data cleaning and preprocessing
2. Alignment of datasets by date
3. Creation of key trading metrics
4. Statistical analysis and visualization
5. Advanced regression modeling for sentiment impact
6. Segmentation of traders
7. Predictive modeling with cross-validation

## Key Features
- **Advanced Statistics**: OLS regression to quantify sentiment impact on PnL
- **Robust Modeling**: Cross-validated Random Forest for performance prediction
- **Interactive Dashboard**: 
  - **Customizable Chart Selection**: Users can choose which charts to display from 10+ options
  - Real-time filters for trader selection and date ranges
  - Attractive Plotly charts with hover details
  - Custom styling for professional appearance
  - Easy navigation and customer-friendly design
  - All project requirements integrated in one interactive interface
- **Interactive Dashboard**: Filters by sentiment, trader segments, and date ranges
- **Comprehensive Analysis**: From basic EDA to actionable trading strategies

## Strategy Recommendations
- Adjust leverage based on sentiment and trader segment
- Optimize trade frequency according to market conditions
- Implement segment-specific risk management

## Technologies Used
- Python, Pandas, NumPy
- Matplotlib, Seaborn for visualization
- Scikit-learn for modeling and cross-validation
- Statsmodels for regression analysis
- Streamlit for interactive dashboard

## Repository
This project is version controlled using Git and hosted on GitHub.
- **Repository**: https://github.com/KMbarath/DS_assessment
- **Main Branch**: All code is pushed to the `main` branch
- **.gitignore**: CSV data files are excluded from version control to reduce repository size

### Git Setup
```bash
# Clone the repository
git clone https://github.com/KMbarath/DS_assessment.git

# Install dependencies
pip install -r requirements.txt
```

**Note**: Data files (CSV files) are not included in the repository. You'll need to provide your own data files in the project directory.