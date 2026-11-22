"""Reproducible analysis for U.S. domestic flight delay patterns.

Expected data path: data/Airline_Delay_Cause-selected-columns.csv
The script reads the CSV, calculates metrics, and writes SVG figures to images/.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / 'data' / 'Airline_Delay_Cause-selected-columns.csv'
IMAGE_DIR = ROOT / 'images'
IMAGE_DIR.mkdir(exist_ok=True)

if not DATA_PATH.exists():
    raise FileNotFoundError('Download the dataset first; see data/README.md')

df = pd.read_csv(DATA_PATH)
for col in ['arr_flights', 'arr_del15', 'carrier_ct', 'weather_ct']:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

carrier = df.groupby('carrier_name').agg(
    arr_flights=('arr_flights', 'sum'),
    arr_del15=('arr_del15', 'sum'),
    carrier_ct=('carrier_ct', 'sum'),
    weather_ct=('weather_ct', 'sum'),
).reset_index()
carrier['delay_rate'] = carrier['arr_del15'] / carrier['arr_flights'] * 100
carrier['weather_pct'] = np.where(carrier['arr_del15'] > 0, carrier['weather_ct'] / carrier['arr_del15'] * 100, 0)
carrier['carrier_pct'] = np.where(carrier['arr_del15'] > 0, carrier['carrier_ct'] / carrier['arr_del15'] * 100, 0)

airport = df.groupby(['airport', 'airport_name']).agg(
    arr_flights=('arr_flights', 'sum'),
    arr_del15=('arr_del15', 'sum'),
).reset_index()
airport['delay_rate'] = airport['arr_del15'] / airport['arr_flights'] * 100
airport = airport[airport['arr_flights'] >= 500].sort_values('delay_rate', ascending=False)

monthly = df.groupby('month').agg(
    arr_flights=('arr_flights', 'sum'),
    arr_del15=('arr_del15', 'sum'),
).reset_index()
monthly['delay_rate'] = monthly['arr_del15'] / monthly['arr_flights'] * 100
monthly['month_name'] = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

major = carrier[carrier['arr_flights'] > 10000].sort_values('delay_rate', ascending=False)
plt.figure(figsize=(12, 8))
plt.barh(major['carrier_name'], major['delay_rate'], color='#ff9f1c')
plt.xlabel('Delay Rate (%)')
plt.title('Airline Delay Rate Ranking, 2003–2025\nCarriers with more than 10,000 recorded flights')
for i, value in enumerate(major['delay_rate']):
    plt.text(value + 0.4, i, f'{value:.1f}%', va='center', fontsize=8)
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'carrier_delay_ranking.svg', format='svg')
plt.close()

plt.figure(figsize=(12, 7))
plt.barh(airport.head(15)['airport_name'].str.split(',').str[0], airport.head(15)['delay_rate'], color='#ff6b6b')
plt.xlabel('Delay Rate (%)')
plt.title('Top 15 High-Delay U.S. Airports, 2003–2025\nAirports with at least 500 recorded flights')
for i, value in enumerate(airport.head(15)['delay_rate']):
    plt.text(value + 0.4, i, f'{value:.1f}%', va='center', fontsize=8)
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'top_delay_airports.svg', format='svg')
plt.close()

month_order = monthly.sort_values('month')
plt.figure(figsize=(10, 5.5))
plt.plot(month_order['month_name'], month_order['delay_rate'], marker='o', linewidth=2, color='#4dabf7')
plt.xlabel('Month')
plt.ylabel('Delay Rate (%)')
plt.title('Monthly U.S. Domestic Flight Delay Rate, 2003–2025')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'monthly_trend.svg', format='svg')
plt.close()

top10 = carrier.nlargest(10, 'arr_del15')
x = np.arange(len(top10))
width = 0.36
plt.figure(figsize=(12, 7))
plt.bar(x - width / 2, top10['weather_pct'], width, label='Weather-related share', color='#4dabf7')
plt.bar(x + width / 2, top10['carrier_pct'], width, label='Carrier-operational share', color='#ff6b6b')
plt.xlabel('Airline')
plt.ylabel('Share of delayed flights (%)')
plt.title('Weather vs Carrier-Operational Delay Shares\nTop 10 carriers by total delayed flights')
plt.xticks(x, top10['carrier_name'].str.slice(0, 15), rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'weather_vs_carrier.svg', format='svg')
plt.close()

total_flights = df['arr_flights'].sum()
total_delayed = df['arr_del15'].sum()
print(f'Records: {len(df):,}')
print(f'Total flights: {total_flights:,.0f}')
print(f'Overall delay rate: {total_delayed / total_flights * 100:.1f}%')
print('Figures written to images/.')
