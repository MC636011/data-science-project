# Dataset download guide

The notebook expects this file:

```text
data/Airline_Delay_Cause-selected-columns.csv
```

The raw CSV is approximately 38 MB and is not committed to this repository. Keep the repository lightweight and follow the source terms by downloading the data separately.

## Option 1 — Download from Kaggle
1. Open the dataset page: https://www.kaggle.com/datasets/daryaheyko/airline-on-time-statistics-and-delay-causes-bts
2. Sign in if required and review the dataset usage terms.
3. Download the CSV file.
4. Rename the downloaded file, if necessary, to:
   ```text
   Airline_Delay_Cause-selected-columns.csv
   ```
5. Place it in the `data/` folder.

Optional command-line method after configuring Kaggle credentials:

```bash
kaggle datasets download -d daryaheyko/airline-on-time-statistics-and-delay-causes-bts
```

Then extract/copy the selected-columns CSV into `data/`.

## Option 2 — Download from BTS TranStats
1. Open https://www.transtats.bts.gov/
2. Use the On-Time Performance reporting section.
3. Export/download the airline delay-cause table.
4. Retain only the fields used by the analysis or rename columns to match `analysis.py`.

## Responsible sharing check
- Do not commit Kaggle API credentials.
- Do not upload personal information.
- Keep the dataset attribution in `README.md` and `CITATION.md`.
- Use the dataset in accordance with BTS and Kaggle terms.
