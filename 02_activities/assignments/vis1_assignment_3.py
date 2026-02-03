import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset.
df = pd.read_csv('major-crime-indicators.csv')

# Extract year and type of incident.
df = df.loc[:,['REPORT_YEAR','MCI_CATEGORY']]

# Rename "Theft Over" to "Theft Over $5000" to make it easily understandable.
mci_rename = {'Theft Over': 'Theft Over $5,000'}
df['MCI_CATEGORY'] = df['MCI_CATEGORY'].replace(mci_rename)

# Get total counts by year and type.
yearly_inc = df.groupby(['REPORT_YEAR','MCI_CATEGORY']).size().reset_index(name='TOTAL_MCI')

# Get years to plot every year.
years = sorted(yearly_inc['REPORT_YEAR'].unique())

# Generate line plot plotting the report year by the number of incidents, colored
# by incident type and save it.
sns.set_style('whitegrid') # Add guide lines.
plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_inc,x='REPORT_YEAR',y='TOTAL_MCI',hue='MCI_CATEGORY',
             palette='colorblind', # Set categorical colors for accessibility, red and green here differ in lightness and saturation.
             linewidth=4) # Make thick to better perceive contrast.
plt.xticks(years) # Plot every year.
plt.ylim(bottom=0) # Set bottom to 0.
plt.title('Trends in Toronto Major Crime Over Time',fontweight='bold',loc='left')
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
leg = plt.legend(title='Major Crime Type',
                loc='center left',
                bbox_to_anchor=(1.02, 0.5),
                frameon=False) # Move legend outside to the middle.
leg.get_title().set_fontweight('bold')
leg.get_title().set_ha('left')
leg._legend_box.align = 'left' # Customize legend.
plt.figtext(0.99,-0.05,
    'Source: Toronto Police Services – Major Crime Indicators (Toronto Open Data)',
    ha='right',
    va='bottom',
    fontweight='bold') # Add source of information.
plt.savefig('vis_1_assignment_3.png',bbox_inches='tight') # Save.
