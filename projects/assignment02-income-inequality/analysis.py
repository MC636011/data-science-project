from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / 'data'
IMAGE_DIR = PROJECT_DIR / 'images'
IMAGE_DIR.mkdir(exist_ok=True)

disp = pd.read_csv(DATA_DIR / 'dispersion_summary.csv')
theil = pd.read_csv(DATA_DIR / 'theil_decomposition_summary.csv')
within = pd.read_csv(DATA_DIR / 'within_region_dispersion_2024.csv')
components = pd.read_csv(DATA_DIR / 'component_share_2024_summary.csv')

plt.figure(figsize=(9, 5))
for col in ['cv', 'gini', 'theil']:
    plt.plot(disp['year'], disp[col], marker='o', label=col.upper())
plt.xlabel('Year')
plt.ylabel('Dispersion metric value')
plt.title('UK Local-Authority GDHI Dispersion, 1997–2024')
plt.legend()
plt.grid(alpha=.3)
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'dispersion_trend.svg', format='svg')
plt.close()

x = range(len(theil))
plt.figure(figsize=(7, 5))
plt.bar(x, theil['between_share'], label='Between-region share', color='#ff6b6b')
plt.bar(x, theil['within_share'], bottom=theil['between_share'], label='Within-region share', color='#4dabf7')
plt.xticks(x, theil['year'])
plt.ylabel('Share of Theil index (%)')
plt.title('Population-Weighted Theil Decomposition')
plt.legend()
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'theil_decomposition.svg', format='svg')
plt.close()

within = within.sort_values('cv', ascending=True)
plt.figure(figsize=(9, 6))
plt.barh(within['Region'], within['cv'], color='#9b5de5')
plt.xlabel('Coefficient of variation')
plt.title('Within-Region GDHI Dispersion in 2024')
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'within_region_dispersion_2024.svg', format='svg')
plt.close()

plt.figure(figsize=(9, 5))
x = range(len(components))
plt.bar([i-.18 for i in x], components['compensation_employees'], .36, label='Compensation of employees', color='#6bcb77')
plt.bar([i+.18 for i in x], components['property_income_received'], .36, label='Property income received', color='#ff9f1c')
plt.xticks(x, components['Region'], rotation=35, ha='right')
plt.ylabel('Share of GDHI component (%)')
plt.title('Selected GDHI Components by Region, 2024')
plt.legend()
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'component_share_2024.svg', format='svg')
plt.close()

print('Charts written to', IMAGE_DIR)
