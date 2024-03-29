import os.path

import pandas as pd
from dotenv import load_dotenv

from languages_cleaner import clean_languages_dataframe
from framework_cleaner import clean_framework_dataframe
from database_cleaner import clean_database_dataframe

load_dotenv()


def analyze_survey_language(country: str, files):
    final_df = pd.DataFrame()
    column_name_mappings = {"LanguageHaveWorkedWith": "Language"}
    excel_filename = 'languages.xlsx'

    for file in files:
        df = pd.read_csv(file)

        target_employment = 'Employed, full-time'
        df = df[(df['Country'] == country) & (df['Employment'] == target_employment)]

        total_respondents = df.shape[0]
        df = df['LanguageHaveWorkedWith'].str.split(';').explode()
        df = df.value_counts().reset_index()

        df[df.columns[-1]] = (df[df.columns[-1]] / total_respondents) * 100
        df = clean_languages_dataframe(df)
        df['LanguageHaveWorkedWith'] = df['LanguageHaveWorkedWith'].str.lower()

        filename = f"Survey_{file[-8:-4]}"

        if final_df.empty:
            final_df = df
            name_of_last_column = final_df.columns[-1]
            final_df.rename(columns={name_of_last_column: filename}, inplace=True)
        else:
            final_df = final_df.merge(df, on='LanguageHaveWorkedWith', how='outer')

            name_of_last_column = final_df.columns[-1]
            final_df.rename(columns={name_of_last_column: filename}, inplace=True)

    final_df.rename(columns=column_name_mappings, inplace=True)
    final_df.fillna(0, inplace=True)

    export_to_excel(final_df, country, excel_filename)


def analyze_survey_framework(country: str, files):
    final_df = pd.DataFrame()
    column_name_mappings = {"WebframeHaveWorkedWith": "Framework"}
    excel_filename = 'frameworks.xlsx'

    for file in files:
        df = pd.read_csv(file)

        target_employment = 'Employed, full-time'
        df = df[(df['Country'] == country) & (df['Employment'] == target_employment)]

        total_respondents = df.shape[0]
        df = df['WebframeHaveWorkedWith'].str.split(';').explode()
        df = df.value_counts().reset_index()

        df[df.columns[-1]] = (df[df.columns[-1]] / total_respondents) * 100
        df['WebframeHaveWorkedWith'] = df['WebframeHaveWorkedWith'].str.lower()
        df = clean_framework_dataframe(df)

        filename = f"Survey_{file[-8:-4]}"

        if final_df.empty:
            final_df = df
            name_of_last_column = final_df.columns[-1]
            final_df.rename(columns={name_of_last_column: filename}, inplace=True)
        else:
            final_df = final_df.merge(df, on='WebframeHaveWorkedWith', how='outer')

            name_of_last_column = final_df.columns[-1]
            final_df.rename(columns={name_of_last_column: filename}, inplace=True)

    final_df.rename(columns=column_name_mappings, inplace=True)
    final_df.fillna(0, inplace=True)

    export_to_excel(final_df, country, excel_filename)


def analyze_survey_database(country: str, files):
    final_df = pd.DataFrame()
    column_name_mappings = {"DatabaseHaveWorkedWith": "Database"}
    excel_filename = 'databases.xlsx'

    for file in files:
        df = pd.read_csv(file)

        target_employment = 'Employed, full-time'
        df = df[(df['Country'] == country) & (df['Employment'] == target_employment)]

        total_respondents = df.shape[0]
        df = df['DatabaseHaveWorkedWith'].str.split(';').explode()
        df = df.value_counts().reset_index()

        df[df.columns[-1]] = (df[df.columns[-1]] / total_respondents) * 100
        df['DatabaseHaveWorkedWith'] = df['DatabaseHaveWorkedWith'].str.lower()
        df = clean_database_dataframe(df)

        filename = f"Survey_{file[-8:-4]}"

        if final_df.empty:
            final_df = df
            name_of_last_column = final_df.columns[-1]
            final_df.rename(columns={name_of_last_column: filename}, inplace=True)
        else:
            final_df = final_df.merge(df, on='DatabaseHaveWorkedWith', how='outer')

            name_of_last_column = final_df.columns[-1]
            final_df.rename(columns={name_of_last_column: filename}, inplace=True)

    final_df.rename(columns=column_name_mappings, inplace=True)
    final_df.fillna(0, inplace=True)

    export_to_excel(final_df, country, excel_filename)


def export_to_excel(dataframe, country: str, excel_filename: str):
    if not os.path.exists(excel_filename):
        with pd.ExcelWriter(excel_filename, engine='openpyxl') as excel_writer:
            dataframe.to_excel(excel_writer=excel_writer, sheet_name=country, index=False)
    else:
        with pd.ExcelWriter(excel_filename, mode='a', engine='openpyxl') as excel_writer:
            dataframe.to_excel(excel_writer=excel_writer, sheet_name=country, index=False)


