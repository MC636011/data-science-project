# Wine Quality Analysis: What Factors Affect Red Wine Quality?

**Project type:** Individual work  
**Owner:** WANG YU MENG (MC636011)  
**Status:** Completed

## Research question
Which physicochemical properties most influence the quality rating of red wine? This project analyzes the relationship between alcohol, volatile acidity, citric acid, sulphates, and other features with the quality score.

## Dataset source and usage permissions
- Source: UCI Machine Learning Repository, Wine Quality Data Set
- Link: https://archive.ics.uci.edu/dataset/186/wine+quality
- File used: `winequality-red.csv` with 1,599 records and 11 chemical features plus one quality score.
- License: CC BY 4.0, allowing sharing and adaptation with attribution.
- Citation: Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Wine Quality [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T
- The raw CSV is not committed. The analysis script downloads it automatically from the public UCI link.

## Methods and tools
- Python, pandas, NumPy, Matplotlib, and Seaborn-style plotting workflows.
- Data cleaning, descriptive statistics, correlation analysis, and grouped comparisons.
- Visualizations: correlation heatmap, mean alcohol by quality, and mean volatile acidity by quality.

## Key findings
1. Alcohol content is positively correlated with quality rating, with correlation approximately **0.48**.
2. Volatile acidity is negatively correlated with quality rating, with correlation approximately **-0.39**.
3. Mean alcohol increases from **9.96** for quality 3 to **12.09** for quality 8.
4. Mean volatile acidity decreases from **0.88** for quality 3 to **0.42** for quality 8, confirming the negative relationship.

## Visualizations
- `images/fig1_correlation_heatmap.svg`
- `images/fig2_alcohol_by_quality.svg`
- `images/fig3_volatile_acidity_by_quality.svg`

## Limitation
The dataset only covers Portuguese Vinho Verde red wine, and quality ratings are subjective expert scores. The sample is limited and cannot be generalized to all red wines. Correlation does not imply causation.

## How to run
```bash
python projects/personal-wine-quality/analysis.py
```
The script downloads the dataset if needed, calculates the results, and writes SVG figures into `projects/personal-wine-quality/images/`.
