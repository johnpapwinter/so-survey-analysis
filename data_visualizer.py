import os

import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'databases.xlsx'
sheet_name = 'France'
df = pd.read_excel(excel_file, sheet_name=sheet_name)

databases = df['Database']
years = ['Survey_2023', 'Survey_2022', 'Survey_2021', 'Survey_2020', 'Survey_2019', 'Survey_2018']
data = df[years].astype(str).apply(lambda x: x.str.replace(',', '.', regex=False)).astype(float)
data['Database'] = df['Database']

# output_directory = 'databases'
# os.makedirs(output_directory, exist_ok=True)

for database in databases:
    database_data = data[data['Database'] == database]
    plt.figure(figsize=(10, 6))
    plt.bar(years, database_data.values[0][:-1], color='b', alpha=0.7)
    plt.title(f'Survey data for: {database}')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.ylim(0, 100)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # plot_filename = os.path.join(output_directory, f"{database}.png")
    # plt.savefig(plot_filename)
    # plt.close()

    plt.show()


