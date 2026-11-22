# Income Inequality Across UK Local Authorities

**Project type:** Group Assignment 02  
**Team:** MC636087 ZHOU ZHUO; MC636011 WANG YU MENG  
**Status:** Completed

## Research question
In the United Kingdom, between 1997 and 2024, is inequality in Gross Disposable Household Income (GDHI) per head across local authorities converging or diverging? In 2024, which GDHI components mainly drive differences between and within regions?

## Dataset source and usage permissions
- ONS official dataset: https://www.ons.gov.uk/economy/regionalaccounts/grossdisposablehouseholdincome/datasets/regionalgrossdisposablehouseholdincomelocalauthorities
- Nomis / ONS population estimates: https://www.nomisweb.co.uk/
- Alternative ONS population page: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates
- The original raw Excel workbook and large intermediate tables are not committed because of file size. Compact exported metrics used for the charts are stored in `data/`.
- Use ONS and Nomis data under their stated terms and keep attribution.

## Methods and tools
- Python, pandas, NumPy, and Matplotlib.
- GDHI per-head analysis across 361 local authorities from 1997 to 2024.
- Dispersion measures: CV, Gini, Theil, P90/P10, P75/P25, and log standard deviation.
- Population-weighted Theil decomposition into between-region and within-region components.
- Regional component analysis for 2024 and within-region dispersion comparison.

## Key findings
1. Equal-weighted dispersion across local authorities shows mild convergence: CV falls from **0.4497 in 1997** to **0.3551 in 2024**, and Theil falls from **0.0560** to **0.0450**.
2. Population-weighted Theil rises from **0.0278 in 1997** to **0.0388 in 2024**.
3. The between-region share of population-weighted Theil rises from **31.96%** to **43.13%**, so weighting changes the conclusion.
4. London has the largest within-region dispersion in 2024, with CV about **0.551** and Gini about **0.242**.
5. Compensation of employees is a major positive GDHI component across regions, while property income and social benefits shape regional differences.

## Visualizations
- `images/dispersion_trend.svg`
- `images/theil_decomposition.svg`
- `images/within_region_dispersion_2024.svg`
- `images/component_share_2024.svg`

## Limitation
The project analyzes aggregate local-authority GDHI, not individual household income. Unweighted and population-weighted inequality can show different trends, and the Nomis population file is a partial consistency check rather than an independent validation source.

## How to run
```bash
python projects/assignment02-income-inequality/analysis.py
```
The script reads the compact CSV files in `data/` and regenerates the SVG figures in `images/`.
