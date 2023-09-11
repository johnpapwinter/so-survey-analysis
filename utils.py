import pandas as pd
from collections import Counter


def clean_languages_dataframe(dataframe):
    dataframe = _handle_html_and_css(dataframe)
    dataframe = _handle_shell(dataframe)
    dataframe = _handle_delphi(dataframe)
    dataframe = _handle_vb_net(dataframe)

    return dataframe


def _handle_html_and_css(dataframe):
    if 'HTML' in dataframe['LanguageHaveWorkedWith'].values:
        dataframe.replace('HTML', 'HTML/CSS', inplace=True)

    if 'CSS' in dataframe['LanguageHaveWorkedWith'].values:
        index = dataframe[dataframe['LanguageHaveWorkedWith'] == 'CSS'].index[0]
        dataframe.drop(labels=[index], inplace=True)

    return dataframe


def _handle_shell(dataframe):
    if 'PowerShell' in dataframe['LanguageHaveWorkedWith'].values:
        index = dataframe[dataframe['LanguageHaveWorkedWith'] == 'PowerShell'].index[0]
        dataframe.drop(labels=[index], inplace=True)

    if 'Bash/Shell' in dataframe['LanguageHaveWorkedWith'].values:
        dataframe.replace('Bash/Shell', 'Bash/Shell (all shells)', inplace=True)

    if 'Bash/Shell/PowerShell' in dataframe['LanguageHaveWorkedWith'].values:
        dataframe.replace('Bash/Shell/PowerShell', 'Bash/Shell (all shells)', inplace=True)

    return dataframe


def _handle_delphi(dataframe):
    if 'Delphi/Object Pascal' in dataframe['LanguageHaveWorkedWith'].values:
        dataframe.replace('Delphi/Object Pascal', 'Delphi', inplace=True)

    return dataframe


def _handle_vb_net(dataframe):
    if 'VB.NET' in dataframe['LanguageHaveWorkedWith'].values:
        dataframe.replace('VB.NET', 'Visual Basic (.Net)', inplace=True)

    return dataframe

