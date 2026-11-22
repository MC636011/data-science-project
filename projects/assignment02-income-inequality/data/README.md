# Assignment 02 data

This folder contains compact derived CSV outputs used to regenerate the portfolio charts. The full original ONS workbook and large intermediate tables are not committed.

## Raw source files
Download the ONS regional GDHI local-authority dataset from:
https://www.ons.gov.uk/economy/regionalaccounts/grossdisposablehouseholdincome/datasets/regionalgrossdisposablehouseholdincomelocalauthorities

The uploaded assignment also used Nomis / ONS population estimates for a consistency check:
https://www.nomisweb.co.uk/

## Included derived files
- `dispersion_summary.csv`: selected dispersion metrics for 1997, 2008, 2020, and 2024.
- `theil_decomposition_summary.csv`: population-weighted Theil decomposition endpoints.
- `within_region_dispersion_2024.csv`: top regional dispersion values in 2024.
- `component_share_2024_summary.csv`: selected regional component shares in 2024.

These files support chart regeneration and are derived from ONS data. Keep ONS attribution.
