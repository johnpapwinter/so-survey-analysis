import pandas as pd


def clean_framework_dataframe(dataframe):
    dataframe = _handle_angular(dataframe)
    dataframe = _handle_react(dataframe)
    dataframe = _handle_angular(dataframe)
    dataframe = _handle_asp_net_core(dataframe)

    return dataframe


def _handle_angular(dataframe):
    if 'angular/angular.js' in dataframe['WebframeHaveWorkedWith'].values:
        dataframe.replace('angular/angular.js', 'angular', inplace=True)

    if 'angular.js' in dataframe['WebframeHaveWorkedWith'].values:
        index = dataframe[dataframe['WebframeHaveWorkedWith'] == 'angular.js'].index[0]
        dataframe.drop(labels=[index], inplace=True)

    if 'angularjs' in dataframe['WebframeHaveWorkedWith'].values:
        index = dataframe[dataframe['WebframeHaveWorkedWith'] == 'angularjs'].index[0]
        dataframe.drop(labels=[index], inplace=True)

    return dataframe


def _handle_react(dataframe):
    if 'react.js' in dataframe['WebframeHaveWorkedWith'].values:
        dataframe.replace('react.js', 'react', inplace=True)

    return dataframe


def _handle_spring(dataframe):
    if 'spring' in dataframe['WebframeHaveWorkedWith'].values:
        dataframe.replace('spring', 'spring boot', inplace=True)

    return dataframe


def _handle_asp_net_core(dataframe):
    if 'asp.net core ' in dataframe['WebframeHaveWorkedWith'].values:
        dataframe.replace('asp.net core ', 'asp.net core', inplace=True)

    return dataframe

