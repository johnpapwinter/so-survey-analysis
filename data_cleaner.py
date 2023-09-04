import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def align_survey_2021():
    file_path = os.getenv("SURVEY_2021")
    df = pd.read_csv(file_path)

    df = df.replace({"Employment": {"Employed full-time": "Employed, full-time"}})
    df.to_csv(file_path, index=False)
    print(f"Successfully aligned and saved {file_path}")


def align_survey_2020():
    file_path = os.getenv("SURVEY_2020")
    df = pd.read_csv(file_path)
    aligned_column_names = {
        "LanguageWorkedWith": "LanguageHaveWorkedWith",
        "WebframeWorkedWith": "WebframeHaveWorkedWith",
        "DatabaseWorkedWith": "DatabaseHaveWorkedWith"
    }

    df = df.replace({"Employment": {"Employed full-time": "Employed, full-time"}})

    df.rename(columns=aligned_column_names, inplace=True)
    df.to_csv(file_path, index=False)
    print(f"Successfully aligned and saved {file_path}")


def align_survey_2019():
    file_path = os.getenv("SURVEY_2019")
    df = pd.read_csv(file_path)
    aligned_column_names = {
        "LanguageWorkedWith": "LanguageHaveWorkedWith",
        "WebframeWorkedWith": "WebframeHaveWorkedWith",
        "DatabaseWorkedWith": "DatabaseHaveWorkedWith"
    }

    df = df.replace({"Employment": {"Employed full-time": "Employed, full-time"}})

    df.rename(columns=aligned_column_names, inplace=True)
    df.to_csv(file_path, index=False)
    print(f"Successfully aligned and saved {file_path}")


def align_survey_2018():
    file_path = os.getenv("SURVEY_2018")
    df = pd.read_csv(file_path)
    aligned_column_names = {
        "DatabaseWorkedWith": "DatabaseHaveWorkedWith",
        "FrameworkWorkedWith": "WebframeHaveWorkedWith",
        "LanguageWorkedWith": "LanguageHaveWorkedWith"
    }

    df = df.replace({"Employment": {"Employed full-time": "Employed, full-time"}})

    df.rename(columns=aligned_column_names, inplace=True)
    df.to_csv(file_path, index=False)
    print(f"Successfully aligned and saved {file_path}")


def align_survey_2017():
    file_path = os.getenv("SURVEY_2017")
    df = pd.read_csv(file_path)
    aligned_column_names = {
        "HaveWorkedDatabase": "DatabaseHaveWorkedWith",
        "HaveWorkedFramework": "WebframeHaveWorkedWith",
        "HaveWorkedLanguage": "LanguageHaveWorkedWith",
        "EmploymentStatus": "Employment"
    }

    df = df.replace({"EmploymentStatus": {"Employed full-time": "Employed, full-time"}})

    df.rename(columns=aligned_column_names, inplace=True)
    df.to_csv(file_path, index=False)
    print(f"Successfully aligned and saved {file_path}")


def clean_data():
    align_survey_2017()
    align_survey_2018()
    align_survey_2019()
    align_survey_2020()
    align_survey_2021()
    print(f"All files aligned!")


clean_data()

