import os

import pandas as pd
import matplotlib.pyplot as plt


def visualize_data(excel_file_name: str, tech_to_visualize: str):
    dataframes = pd.read_excel(excel_file_name, sheet_name=None)

    for sheet_name, df in dataframes.items():
        technologies = df[tech_to_visualize]
        years = ['Survey_2018', 'Survey_2019', 'Survey_2020', 'Survey_2021', 'Survey_2022', 'Survey_2023']
        data = df[years].astype(str).apply(lambda x: x.str.replace(',', '.', regex=False)).astype(float)
        data[tech_to_visualize] = df[tech_to_visualize]

        output_directory = excel_file_name.split('.')[0]
        os.makedirs(output_directory, exist_ok=True)
        plt.figure(figsize=(12, 8))

        for technology in technologies:
            technology_data = data[data[tech_to_visualize] == technology]
            plt.plot(years, technology_data.values[0][:-1], label=technology)

        plt.title(f'{tech_to_visualize} in {sheet_name}')
        plt.xlabel('Year')
        plt.ylabel('Percentage (%)')
        plt.ylim(0, 100)
        plt.xticks(rotation=45)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3)
        plt.tight_layout()

        plot_filename = os.path.join(output_directory, f"{sheet_name}.png")
        plt.savefig(plot_filename)
        plt.close()


