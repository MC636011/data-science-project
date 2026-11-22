# U.S. Domestic Flight Delay Pattern Analysis

**Project type:** Group Assignment 01  
**Team:** MC636087 ZHOU ZHUO; MC636011 WANG YU MENG  
**Status:** Completed

## Research question
What drives U.S. domestic flight delays — carriers, airports, time of year, or causal factors — and how can travelers, airlines, and policy makers use these insights to improve on-time performance?

## Dataset source and usage permissions
- Official source: U.S. Bureau of Transportation Statistics, TranStats On-Time Performance: https://www.transtats.bts.gov/
- Convenient mirror used for the assignment: https://www.kaggle.com/datasets/daryaheyko/airline-on-time-statistics-and-delay-causes-bts
- Coverage: 398,233 aggregated records from June 2003 to January 2025, representing more than 140 million domestic flights.
- The raw CSV is approximately 38 MB and is not committed. Download instructions are in `data/README.md`.
- Use the data under BTS/Kaggle terms and keep source attribution.

## Methods and tools
- Python, pandas, NumPy, Matplotlib, and Jupyter-style reproducible analysis.
- Missing operational values were filled with zero where no delay was recorded or reported.
- Metrics: delay rate, carrier-operational share, weather share, and monthly aggregation.

## Key findings
1. Overall delay rate is approximately **19.2%**.
2. Aloha Airlines has the lowest carrier delay rate at about **7.1%**.
3. Peninsula Airways has the highest overall carrier delay rate at about **31.5%**; among carriers with more than 10,000 flights, Frontier Airlines is highest at about **26.2%**.
4. Unalaska has the highest airport delay rate at about **37.1%** among airports with at least 500 flights.
5. Carrier-operational delays account for about **29.5%** of delays; direct weather delays account for about **3.6%**.
6. June is the worst month at about **23.1%**, while September is best at about **14.9%**.

## Visualizations
- `images/carrier_delay_ranking.svg`
- `images/top_delay_airports.svg`
- `images/weather_vs_carrier.svg`
- `images/monthly_trend.svg`

## Limitation
The data is aggregated by carrier, airport, and month. It can identify patterns and rankings but cannot prove passenger-level causality or fully explain systemic “other” delays. Historical patterns may not generalize to future schedules or weather.

## How to run
```bash
python projects/assignment01-flight-delay/analysis.py
```
Before running, place the downloaded CSV at `projects/assignment01-flight-delay/data/Airline_Delay_Cause-selected-columns.csv`.
