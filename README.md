# Heart Attack Risk Analysis — EDA & Power BI Dashboard

An end-to-end data analysis project on the UCI Cleveland Heart Disease dataset: Python-based exploratory data analysis, a 3-page interactive Power BI dashboard, and a written findings report.

**Dashboard:** `HeartAttack.pbix` (Power BI Desktop)
**Report:** `Heart_Attack_Analysis_Report.md`

---

## Overview

Heart disease remains one of the leading causes of death globally, and early identification of high-risk patients depends on recognizing patterns across a handful of clinical measurements — chest pain type, exercise response, blood pressure, cholesterol, and more. This project explores the Cleveland Heart Disease cohort to answer:

- What share of this cohort is diagnosed positive, and how does that vary by age, sex, and symptoms?
- Which individual measurements separate positive from negative patients most clearly?
- Can a filterable Power BI report let a non-technical viewer explore these patterns in seconds, not minutes?

## Dataset

- **Source:** UCI Machine Learning Repository — Cleveland Heart Disease dataset (also hosted on Kaggle)
- **Size:** 303 patient records, 13 features + 1 target column, zero missing values
- **Target:** `target` — 1 = heart disease present, 0 = absent

| Column | Description |
|---|---|
| age | Age in years |
| sex | 1 = male, 0 = female |
| cp | Chest pain type (0 = typical angina, 1 = atypical angina, 2 = non-anginal, 3 = asymptomatic) |
| trestbps | Resting blood pressure (mm Hg) |
| chol | Serum cholesterol (mg/dl) |
| fbs | Fasting blood sugar > 120 mg/dl (1 = true) |
| restecg | Resting ECG results (0–2) |
| thalach | Maximum heart rate achieved |
| exang | Exercise-induced angina (1 = yes) |
| oldpeak | ST depression induced by exercise relative to rest |
| slope | Slope of the peak exercise ST segment (0–2) |
| ca | Number of major vessels colored by fluoroscopy (0–4) |
| thal | Thalassemia type (0–3) |
| target | Diagnosis outcome (1 = positive, 0 = negative) |

## Key Insights

From the EDA and dashboard exploration:

- **Typical angina is the least reliable warning sign in this cohort.** Only 27.3% of patients presenting with typical angina were diagnosed positive — the lowest rate of any chest pain category. Atypical angina (82.0%), non-anginal pain (79.3%), and asymptomatic patients (69.6%) all had substantially higher positive-diagnosis rates.
- **Exercise-induced angina strongly predicts a negative outcome.** Patients without exercise-induced angina were diagnosed positive 69.6% of the time, versus just 23.2% for those who experienced angina during exercise.
- **Vessels blocked (ca) shows a mostly monotonic relationship with diagnosis** — positive-diagnosis rate drops steadily from 74.3% at ca=0 down to 15.0% at ca=3 (the ca=4 group breaks this pattern but is only 5 patients, likely noise).
- **Sex shows a wide, counterintuitive gap** — female patients had a 75.0% positive-diagnosis rate versus 44.9% for male patients in this sample, running against the common perception of heart disease as a predominantly male condition.
- **Exercise response outweighs resting measurements** — max heart rate, ST depression, and exercise angina separated positive/negative patients far more clearly than resting blood pressure or cholesterol.

Full write-up with methodology and limitations: see [`Heart_Attack_Analysis_Report.md`](./Heart_Attack_Analysis_Report.md).

## Power BI Dashboard

A 3-page interactive Power BI report (`HeartAttack.pbix`) built on top of the cleaned dataset with custom DAX measures.

| Page | Contents |
|---|---|
| **1. Overview** | KPI cards (Total Patients, Positive Rate, Average Age, Average Cholesterol), diagnosis split donut chart, age distribution column chart |
| **2. Risk Factors by Category** | Chest pain type vs diagnosis, exercise angina vs diagnosis, vessels blocked (ca) vs diagnosis, sex vs diagnosis — with slicers for sex, age band, chest pain type, and diagnosis |
| **3. Numeric Relationships** | Average resting blood pressure by diagnosis, age vs. max heart rate scatter plot (colored by diagnosis), average ST depression (oldpeak) by diagnosis — with an age-band slicer |

**DAX measures used:**
```
Total Patients      = COUNTROWS(Heart)
Positive Count       = CALCULATE(COUNTROWS(Heart), Heart[target]=1)
Negative Count       = CALCULATE(COUNTROWS(Heart), Heart[target]=0)
Positive Rate        = DIVIDE([Positive Count], [Total Patients])
Average Age          = AVERAGE(Heart[age])
Average Cholesterol  = AVERAGE(Heart[chol])
```

**To open:** open `HeartAttack.pbix` in Power BI Desktop (free download from Microsoft).

## Repo Structure

```
├── README.md
├── Heart_Attack_Analysis_Report.md
├── data/
│   └── Heart_Attack_Data_Set.csv
├── powerbi/
│   └── HeartAttack.pbix
└── notebook/
    └── eda_feature_engineering.ipynb
```

## Tech Stack

- **Analysis:** Python (pandas)
- **BI/dashboard:** Power BI Desktop, DAX
- **Data:** UCI Heart Disease (Cleveland) dataset, 303 records

## Author

Built as a personal data analysis / BI portfolio project. Feedback and forks welcome — open an issue or connect on LinkedIn.

