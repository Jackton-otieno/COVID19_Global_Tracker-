# COVID19_Global_Tracker-

1) Project Description
The COVID-19 Global Tracker project analyzes synthetic COVID-19 data to track the progression of cases, deaths, and vaccinations across India, USA, and Canada from January 2020 to December 2022. It includes exploratory data analysis (EDA) in a Jupyter Notebook (COVID19_Global_Tracker.ipynb) and an interactive Streamlit dashboard (dashboard.py) for visualizing trends over time.


2) Objectives

Data Cleaning and Preparation: Clean and filter the synthetic dataset to focus on India, USA, and Canada, handling missing values and converting data types.
Exploratory Data Analysis (EDA): Visualize trends in total cases, deaths, vaccinations, and vaccination rates (% of population) over time, and analyze correlations between key metrics.
Interactive Dashboard: Build a Streamlit dashboard to allow users to select countries and view dynamic plots of COVID-19 metrics.
Insights and Reporting: Summarize key findings, such as vaccination rollout speeds, mortality trends, and healthcare burden, while identifying anomalies or interesting patterns.

3) Tools and Libraries Used

Python 3.8+: Core programming language.
Pandas: Data manipulation and cleaning.
Matplotlib: Plotting for EDA (e.g., line plots, heatmaps).
Seaborn: Visualization of correlation matrices.
Plotly: Interactive plots in the Streamlit dashboard.
Streamlit: Framework for building the interactive dashboard.
Jupyter Notebook: Environment for EDA and reporting.


4) How to Run/View the Project
   
Prerequisites

Install Python 3.8 or higher.
Install required libraries:pip install pandas matplotlib seaborn plotly streamlit


For PDF export (optional), install nbconvert and LaTeX:pip install nbconvert
sudo apt-get install texlive-full  # On Ubuntu/Debian



5) Running the Jupyter Notebook

Clone or download the repository.
Ensure the dataset (synthetic_covid19_data.csv) is in the same directory as the notebook.
Launch Jupyter Notebook:jupyter notebook


Open COVID19_Global_Tracker.ipynb and run all cells to view the EDA, visualizations, and insights.

6) Running the Streamlit Dashboard

Ensure the dataset (synthetic_covid19_data.csv) is in the same directory as dashboard.py.
Run the Streamlit app:streamlit run dashboard.py


Open the provided URL (e.g., http://localhost:8501) in your browser to interact with the dashboard.

7) Exporting the Notebook (Optional)

To PDF:jupyter nbconvert --to pdf COVID19_Global_Tracker.ipynb


To PowerPoint: Take screenshots of key cells and manually create slides, or use python-pptx for automation (see notebook instructions).

8) Insights and Reflections
Key Insights

Canada’s Rapid Vaccination Rollout: Canada exhibited the fastest vaccination rollout, reaching an apparent rate of over 4000% by early 2023, though this was due to a calculation error (not accounting for multiple doses). Even corrected, Canada’s trajectory suggests a highly effective campaign.
USA’s Steady Vaccination Progress: The USA showed consistent vaccination growth, peaking at ~500% (also reflecting the same calculation issue) by mid-2022, indicating a sustained effort despite a larger population.
India’s Slower Vaccination Uptake: India’s vaccination rate grew gradually, reaching ~100% by 2023, reflecting challenges in scaling efforts across its 1.39 billion population.
Anomaly - Unrealistic Vaccination Rates: The vaccination rate plot showed rates up to 4000%, an anomaly due to total_vaccinations including multiple doses without normalization. Correcting this (e.g., capping at 200% for two doses) provides a more realistic view.
Delayed Vaccination Start: All countries showed a delayed start (mid-2021), aligning with global vaccine availability timelines, highlighting early deployment challenges.

9) Reflections

Data Quality: Working with synthetic data revealed challenges, such as exaggerated vaccination numbers, which required careful interpretation. Real-world data would provide more reliable insights, especially for anomalies like India’s late-2021 death spike.
Calculation Adjustments: The vaccination rate anomaly underscores the importance of normalizing metrics (e.g., accounting for doses per person). Future iterations should include a population column in the dataset or adjust for dose counts.
Visualization Clarity: Filtering issues in earlier plots (e.g., cluttered vaccination trends) highlighted the need for rigorous data checks. The Streamlit dashboard mitigated this by allowing dynamic country selection, improving usability.
Healthcare Implications: The strong correlation between cases, hospital patients, and ICU patients (from Cell 7) emphasizes the need for healthcare capacity planning during surges, a critical takeaway for policymakers.

This project provided a solid foundation for analyzing pandemic trends, but refining calculations and using real data would enhance its practical impact.
