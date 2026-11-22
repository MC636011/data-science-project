from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / 'data' / 'Airline_Delay_Cause-selected-columns.csv'
IMAGE_DIR = PROJECT_DIR / 'images'
IMAGE_DIR.mkdir(exist_ok=True)

if not DATA_PATH.exists():
    raise FileNotFoundError('Download the dataset first; see data/README.md')

df = pd.read_csv(DATA_PATH)
for col in ['arr_flights', 'arr_del15', 'carrier_ct', 'weather_ct']:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

carrier = df.groupby('carrier_name').agg(arr_flights=('arr_flights','sum'), arr_del15=('arr_del15','sum'), carrier_ct=('carrier_ct','sum'), weather_ct=('weather_ct','sum')).reset_index()
carrier['delay_rate'] = carrier['arr_del15'] / carrier['arr_flights'] * 100
carrier['weather_pct'] = np.where(carrier['arr_del15'] > 0, carrier['weather_ct'] / carrier['arr_del15'] * 100, 0)
carrier['carrier_pct'] = np.where(carrier['arr_del15'] > 0, carrier['carrier_ct'] / carrier['arr_del15'] * 100, 0)

airport = df.groupby('airport_name').agg(arr_flights=('arr_flights','sum'), arr_del15=('arr_del15','sum')).reset_index()
airport['delay_rate'] = airport['arr_del15'] / airport['arr_flights'] * 100
airport = airport[airport['arr_flights'] >= 500].sort_values('delay_rate', ascending=False)

monthly = df.groupby('month').agg(arr_flights=('arr_flights','sum'), arr_del15=('arr_del15','sum')).reset_index()
monthly['delay_rate'] = monthly['arr_del15'] / monthly['arr_flights'] * 100
monthly['month_name'] = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

major = carrier[carrier['arr_flights'] > 10000].sort_values('delay_rate', ascending=False)
plt.figure(figsize=(12, 8))
plt.barh(major['carrier_name'], major['delay_rate'], color='#ff9f1c')
plt.xlabel('Delay Rate (%)')
plt.title('Airline Delay Rate Ranking')
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'carrier_delay_ranking.svg', format='svg')
plt.close()

plt.figure(figsize=(12, 7))
plt.barh(airport.head(15)['airport_name'].str.split(',').str[0], airport.head(15)['delay_rate'], color='#ff6b6b')
plt.xlabel('Delay Rate (%)')
plt.title('Top 15 High-Delay U.S. Airports')
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'top_delay_airports.svg', format='svg')
plt.close()

monthly = monthly.sort_values('month')
plt.figure(figsize=(10, 5))
plt.plot(monthly['month_name'], monthly['delay_rate'], marker='o', color='#4dabf7')
plt.ylabel('Delay Rate (%)')
plt.title('Monthly Delay Rate Trend')
plt.grid(alpha=.3)
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'monthly_trend.svg', format='svg')
plt.close()

top10 = carrier.nlargest(10, 'arr_del15')
x = np.arange(len(top10))
plt.figure(figsize=(12, 7))
plt.bar(x-.18, top10['weather_pct'], .36, label='Weather', color='#4dabf7')
plt.bar(x+.18, top10['carrier_pct'], .36, label='Carrier', color='#ff6b6b')
plt.xticks(x, top10['carrier_name'].str.slice(0,15), rotation=45, ha='right')
plt.ylabel('Share of delayed flights (%)')
plt.title('Weather vs Carrier-Operational Delay Shares')
plt.legend()
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'weather_vs_carrier.svg', format='svg')
plt.close()

print('Overall delay rate:', df['arr_del15'].sum() / df['arr_flights'].sum() * 100)
print('Figures written to', IMAGE_DIR)
