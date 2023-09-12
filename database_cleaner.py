import pandas as pd


def clean_database_dataframe(dataframe):
    dataframe = _handle_ms_sql_server(dataframe)
    dataframe = _handle_dynamodb(dataframe)
    dataframe = _handle_bigquery(dataframe)
    dataframe = _handle_firebase(dataframe)
    dataframe = _handle_couchdb(dataframe)
    dataframe = _handle_cosmosdb(dataframe)

    return dataframe


def _handle_ms_sql_server(dataframe):
    if 'sql server' in dataframe['DatabaseHaveWorkedWith'].values:
        dataframe.replace('sql server', 'microsoft sql server', inplace=True)

    return dataframe


def _handle_dynamodb(dataframe):
    if 'amazon dynamodb' in dataframe['DatabaseHaveWorkedWith'].values:
        dataframe.replace('amazon dynamodb', 'dynamodb', inplace=True)

    return dataframe


def _handle_cosmosdb(dataframe):
    if 'microsoft azure (tables, cosmosdb, sql, etc)' in dataframe['DatabaseHaveWorkedWith'].values:
        dataframe.replace('microsoft azure (tables, cosmosdb, sql, etc)', 'cosmos db', inplace=True)

    return dataframe


def _handle_firebase(dataframe):
    if 'firebase' in dataframe['DatabaseHaveWorkedWith'].values:
        dataframe.replace('firebase', 'firebase realtime database', inplace=True)

    return dataframe


def _handle_bigquery(dataframe):
    if 'google bigquery' in dataframe['DatabaseHaveWorkedWith'].values:
        dataframe.replace('google bigquery', 'bigquery', inplace=True)

    return dataframe


def _handle_couchdb(dataframe):
    if 'couch db' in dataframe['DatabaseHaveWorkedWith'].values:
        dataframe.replace('couch db', 'couchdb', inplace=True)

    return dataframe
