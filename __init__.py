import os
import pandas as pd
import constants
from dotenv import load_dotenv
from data_processor import analyze_survey_language, analyze_survey_framework, analyze_survey_database
from excel_service import export_to_excel

load_dotenv()

list_of_countries = constants.COUNTRIES_LIST
files = [os.getenv('SURVEY_2023'),
         os.getenv('SURVEY_2022'),
         os.getenv('SURVEY_2021'),
         os.getenv('SURVEY_2020'),
         os.getenv('SURVEY_2019'),
         os.getenv('SURVEY_2018')]

# for country in list_of_countries:
#     print(f"RESULTS FOR {country.upper()}")
#     # analyze_survey_language(country, files)
#     analyze_survey_framework(country, files)
#     analyze_survey_database(country, files)
#     print('----------------------')
#     print('----------------------')
#     print('----------------------')

analyze_survey_database(country='Japan', files=files)
