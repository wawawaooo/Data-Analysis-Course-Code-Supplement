# COVID-19 Vaccination Data Analysis Dashboard

## Overview
This project is a web-based interactive dashboard for analyzing national COVID-19 vaccination trends in the United States. Using Dash and Plotly, the dashboard visualizes vaccination progress, highlights key insights, and enables users to explore data interactively. The analysis focuses on vaccination completion rates across different age groups and examines relationships between vaccine administration and series completion.

## Features
- **Introduction Tab:** Overview of the project's goals, methodology, and research questions.
- **Interactive Charts:**
  - Vaccination series completion by age group.
  - Average vaccination rates by age group.
  - Correlation between daily vaccine doses administered and series completions.
- **Summary Takeaways:** Key findings and recommendations based on the analysis.
- **Data Source Links:** Datasets from [data.gov](https://data.gov/) used for this project.

## Project Structure
- **`app.py`:** The main application file containing the Dash layout and callback functions for interactivity.
- **`wrangling_df.csv`:** The cleaned dataset used for visualization and analysis.
- **`style.py`:** Custom styles for UI elements to enhance user experience.

## Installation and Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```
   By default, the app will run at [http://localhost:8050](http://localhost:8050).

Alternatively, you can access the hosted version of the application here: [COVID-19 Vaccination Dashboard](https://data-analysis-course-code-supplement.onrender.com/).

## How to Use
1. Open the application in your browser.
2. Navigate through tabs to explore various visualizations.
3. Use dropdown menus to filter data by month and year.
4. Hover over charts to view detailed data points.

## Data Sources
- [COVID-19 Vaccination and Case Trends by Age Group, United States](https://catalog.data.gov/dataset/covid-19-vaccination-and-case-trends-by-age-group-united-states-e81b4)
- [COVID-19 Vaccination Trends in the United States, National and Jurisdictional](https://catalog.data.gov/dataset/covid-19-vaccination-trends-in-the-united-statesnational-80d4f)

## Key Findings
1. Vaccination completion rates are highest among individuals aged 65+ due to greater health awareness and vulnerability.
2. Younger age groups have the lowest vaccination completion rates, highlighting a need for targeted awareness campaigns.
3. A positive correlation exists between daily vaccine doses administered and series completions, emphasizing the importance of robust distribution strategies.

## Authors
This dashboard was developed as part of a data analysis project focused on improving public understanding of COVID-19 vaccination trends.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Special thanks to [data.gov](https://data.gov/) for providing the datasets used in this analysis.

