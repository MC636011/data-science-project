from pathlib import Path
import urllib.request

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / 'data'
IMAGE_DIR = PROJECT_DIR / 'images'
DATA_DIR.mkdir(exist_ok=True)
IMAGE_DIR.mkdir(exist_ok=True)
DATA_PATH = DATA_DIR / 'winequality-red.csv'
URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

if not DATA_PATH.exists():
    urllib.request.urlretrieve(URL, DATA_PATH)

df = pd.read_csv(DATA_PATH, sep=';')
corr = df[['alcohol', 'volatile acidity', 'quality']].corr()
by_quality = df.groupby('quality')[['alcohol', 'volatile acidity']].mean()

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
ax.set_xticks(range(3), ['Alcohol', 'Volatile acidity', 'Quality'])
ax.set_yticks(range(3), ['Alcohol', 'Volatile acidity', 'Quality'])
for i in range(3):
    for j in range(3):
        ax.text(j, i, f'{corr.iloc[i, j]:.2f}', ha='center', va='center')
fig.colorbar(im, ax=ax)
ax.set_title('Correlation Matrix: Wine Quality Predictors')
fig.tight_layout()
fig.savefig(IMAGE_DIR / 'fig1_correlation_heatmap.svg', format='svg')
plt.close(fig)

by_quality['alcohol'].plot(kind='bar', figsize=(8, 5), color='#4dabf7')
plt.xlabel('Quality score')
plt.ylabel('Mean alcohol (%)')
plt.title('Mean Alcohol Content by Wine Quality')
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'fig2_alcohol_by_quality.svg', format='svg')
plt.close()

by_quality['volatile acidity'].plot(kind='bar', figsize=(8, 5), color='#ff6b6b')
plt.xlabel('Quality score')
plt.ylabel('Mean volatile acidity (g/dm³)')
plt.title('Mean Volatile Acidity by Wine Quality')
plt.tight_layout()
plt.savefig(IMAGE_DIR / 'fig3_volatile_acidity_by_quality.svg', format='svg')
plt.close()

print('Rows:', len(df))
print(corr.round(3))
print(by_quality.round(3))
print('Figures written to', IMAGE_DIR)
