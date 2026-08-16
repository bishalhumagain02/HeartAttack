# Heart Disease Risk Analysis — Report

**Dataset:** Cleaned Cleveland Heart Disease Dataset (303 patients, 13 clinical features)
**Tools:** Python (pandas) for EDA, Power BI for the dashboard (`HeartAttack.pbix`, 3 report pages)
**Author:** [Your Name]

---

## Executive Summary

This report looks at 303 patient records to understand which clinical factors are associated with a recorded heart disease diagnosis. Python was used to explore the data, while Power BI was used to create an interactive dashboard showing the main patterns.

One of the interesting findings is that chest-pain type does not always follow the pattern we might expect. Patients with typical angina had the lowest positive-diagnosis rate at **27.3%**, while atypical angina, non-anginal pain, and asymptomatic patients had much higher rates, ranging from about **70% to 82%**. Other exercise-related measurements, such as maximum heart rate and ST depression, also showed noticeable differences between patients with positive and negative diagnoses.

These results describe patterns found in this particular cleaned Cleveland dataset and should be treated as **associations rather than clinical predictions or causes**.

## Objective

The main goal of this analysis is to explore the clinical variables in the dataset and see which ones show the biggest differences between patients with positive and negative heart disease diagnoses. Python was used for the exploratory analysis, and Power BI was used to present the findings through a three-page interactive dashboard.

## Methodology

The cleaned dataset contains **303 records and 13 clinical features plus the target variable**. Python and pandas were used to examine the data and calculate diagnosis rates and average values for different groups.

Categorical variables such as sex, chest-pain type, and exercise-induced angina were given readable labels before being used in the Power BI dashboard. DAX measures such as Total Patients, Positive Rate, Average Age, Average Cholesterol, and Positive/Negative Count were used to create the main KPIs and visualizations.

## Dashboard Structure

| Page                                  | Contents                                                                                                                                  |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Page 1 — Overview**                 | KPI cards for Total Patients, Positive Rate, Average Age, and Average Cholesterol, along with diagnosis distribution and age distribution |
| **Page 2 — Risk Factors by Category** | Chest pain type, exercise-induced angina, major vessels identified by fluoroscopy (`ca`), and sex compared with diagnosis                 |
| **Page 3 — Numeric Relationships**    | Resting blood pressure by diagnosis, age vs. maximum heart rate, and average ST depression (`oldpeak`) by diagnosis                       |

The dashboard also includes slicers that allow users to explore the results by sex, age band, chest-pain type, and diagnosis.

## Key Findings

**1. Typical angina had the lowest positive-diagnosis rate.**
Only **27.3%** of patients with typical angina had a positive diagnosis. In comparison, the rates were **82.0%** for atypical angina, **79.3%** for non-anginal pain, and **69.6%** for asymptomatic patients. *(See: Chest Pain Type vs Diagnosis, Page 2.)* This is an interesting result because it does not follow the pattern we might normally expect. However, it should be viewed as a finding from this dataset rather than evidence that typical angina is clinically unreliable.

**2. Exercise-induced angina showed an unexpected pattern.**
Patients without exercise-induced angina had a positive-diagnosis rate of **69.6%**, compared with **23.2%** among patients who experienced angina during exercise. *(See: Exercise Angina vs Diagnosis, Page 2.)* This is an unexpected relationship in the dataset and should not be interpreted as meaning that exercise-induced angina protects against heart disease.

**3. The `ca` variable showed a generally decreasing trend.**
The positive-diagnosis rate decreased from **74.3% at `ca=0` to 15.0% at `ca=3`**. The `ca=4` category had an 80.0% positive rate, but it contains only **5 patients**, so this result can be strongly affected by a very small number of observations. *(See: Major Vessels vs Diagnosis, Page 2.)*

**4. There was a noticeable difference between male and female patients.**
Female patients had a positive-diagnosis rate of **75.0%**, compared with **44.9%** for male patients. *(See: Sex vs Diagnosis, Page 2.)* However, the dataset contains **207 male patients and 96 female patients**, so the difference should be interpreted carefully and should not be generalized without testing it on a larger dataset.

**5. Exercise-related measurements showed noticeable differences.**
Patients with a positive diagnosis had an average maximum heart rate (`thalach`) of **158.5 bpm**, compared with **139.1 bpm** for patients with a negative diagnosis. Resting blood pressure showed a smaller difference, with averages of **129.3 mmHg** and **134.4 mmHg**, respectively. ST depression (`oldpeak`) also showed a clear difference, averaging **0.58** for positive patients and **1.59** for negative patients. *(See: Numeric Relationships, Page 3.)*

## Limitations

* **Association does not mean causation.** The findings show relationships within the dataset and do not prove that one factor causes heart disease.
* **Limited dataset size.** The analysis is based on only 303 patients, so some smaller groups may not give stable percentages.
* **Dataset representativeness.** This is a cleaned Cleveland Heart Disease dataset, so the results may not represent other populations.
* **Small subgroups.** Categories such as `ca=4` contain very few patients and should be interpreted with caution.
* **No predictive model was developed.** This project focuses on EDA and visualization rather than testing a machine-learning classifier.

## Recommendations / Next Steps

* Develop and evaluate a classification model using the available clinical features and measure its performance using accuracy, precision, recall, F1-score, and ROC-AUC.
* Investigate the unexpected chest-pain and exercise-angina patterns using statistical analysis and a larger dataset.
* Check whether the difference between male and female diagnosis rates remains consistent in a larger and more balanced dataset.
* Use feature-importance methods in a future machine-learning model to better understand which variables contribute most to the predictions.

---

*Dashboard file:* `HeartAttack.pbix` *(Power BI, 3 pages).*
*Source data:* `Heart_Attack_Data_Set.csv`.
