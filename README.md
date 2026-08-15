
 Overview

Heart disease remains one of the leading causes of death globally, and early identification of high-risk patients depends on recognizing patterns across a handful of clinical measurements — chest pain type, exercise response, blood pressure, cholesterol, and more. This project explores the Cleveland Heart Disease cohort to answer:

- What share of this cohort is diagnosed positive, and how does that vary by age, sex, and symptoms?
- Which individual measurements separate positive from negative patients most clearly?
- Can a filterable dashboard let a non-technical viewer explore these patterns in seconds, not minutes?

Dataset

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

 Key Insights

From correlation analysis against `target` across the full cohort:

- **Strongest positive predictors:** chest pain type (`cp`, r ≈ 0.43), maximum heart rate (`thalach`, r ≈ 0.42), and ST slope (`slope`, r ≈ 0.35) — higher values associate with a positive diagnosis.
- **Strongest negative predictors:** exercise-induced angina (`exang`, r ≈ -0.44), ST depression (`oldpeak`, r ≈ -0.43), and number of blocked vessels (`ca`, r ≈ -0.39) — presence of these associates with a positive diagnosis (inverse-coded).
- **Weakest predictors:** fasting blood sugar (`fbs`, r ≈ -0.03) and cholesterol (`chol`, r ≈ -0.09) show almost no linear relationship with diagnosis in this cohort, despite being commonly assumed risk factors.
- Patients presenting with **asymptomatic chest pain** show a disproportionately high positive-diagnosis rate compared to typical angina — a counterintuitive pattern worth flagging for clinical review.



## Dashboard 1: Power BI Report

A 5-page Power BI report replicating the same analysis for users who prefer a native BI tool.

| Page | Contents |
|---|---|
| 1. Overview | KPI cards, diagnosis split donut, age distribution by diagnosis |
| 2. Risk Factors by Category | Chest pain type, exercise angina, sex, and vessels-blocked vs diagnosis, with slicers |
| 3. Numeric Relationships | Age-vs-max-heart-rate scatter, resting BP and ST depression by diagnosis |
| 4. Feature Signal | Average of each numeric field by diagnosis, as a correlation proxy |
| 5. Patient Detail Table | Full sortable/filterable patient-level table |

**DAX measures used:**
```
Total Patients   = COUNTROWS(Heart)
Positive Count   = CALCULATE(COUNTROWS(Heart), Heart[target]=1)
Positive Rate    = DIVIDE([Positive Count], [Total Patients])
Avg Age          = AVERAGE(Heart[age])
Avg Cholesterol  = AVERAGE(Heart[chol])
Avg Max HR       = AVERAGE(Heart[thalach])
```

**To open:** load `Heart_Attack_Data_Set.csv` into Power BI Desktop, add the calculated columns and measures listed in the build guide, and recreate the visuals page by page as documented in this repo's wiki / project notes.

## Repo Structure

```
├── README.md
├── data/
│   └── Heart_Attack_Data_Set.csv
├── dashboard/
│   └── cardiac_risk_atlas.html
├── powerbi/
│   └── cardiac_risk_atlas.pbix
└── notebook/
    └── eda_feature_engineering.ipynb
```

## Tech Stack

- **Analysis:** Python (pandas)
- **BI report:** Power BI Desktop, DAX
- **Data:** UCI Heart Disease (Cleveland) dataset, 303 records

## Author

Built as a personal data analysis / BI portfolio project. Feedback and forks welcome — open an issue or connect on LinkedIn.

## License

Dataset: UCI Machine Learning Repository, publicly available for research and education. Code in this repository is provided under the MIT License unless noted otherwise.
