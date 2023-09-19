import os

import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'databases.xlsx'
sheet_name = 'France'
df = pd.read_excel(excel_file, sheet_name=sheet_name)

databases = df['Database']
years = ['Survey_2018', 'Survey_2019', 'Survey_2020', 'Survey_2021', 'Survey_2022', 'Survey_2023']
data = df[years].astype(str).apply(lambda x: x.str.replace(',', '.', regex=False)).astype(float)
data['Database'] = df['Database']

output_directory = 'databases'
os.makedirs(output_directory, exist_ok=True)
plt.figure(figsize=(12, 8))

for database in databases:
    database_data = data[data['Database'] == database]
    plt.plot(years, database_data.values[0][:-1], label=database)


plt.title(f'Database in {sheet_name}')
plt.xlabel('Year')
plt.ylabel('Percentage (%)')
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3)
plt.tight_layout()

# plot_filename = os.path.join(output_directory, f"{sheet_name}.png")
# plt.savefig(plot_filename)
# plt.close()

plt.show()


