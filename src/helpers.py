import re

import pandas as pd
import streamlit as st


def convert_to_int_if_error_return_zero(x):
    return _convert_to_type_if_error_return_zero(x, int)


def convert_to_float_if_error_return_zero(x):
    return _convert_to_type_if_error_return_zero(x, float)


def _convert_to_type_if_error_return_zero(x, type_):
    # FKB Underscore to avoid the same naming as the builtin function "type"
    try:
        return type_(x)
    except:
        return 0


def file_upload():
    df = pd.read_csv("./bikes.csv")
    return df
    file_upload = st.sidebar.file_uploader(label="Upload CSV or Excel file", type=["csv", "xlsx"])

    if file_upload is not None:
        try:
            df = pd.read_csv(file_upload)
            return df
        except Exception as e:
            print(e)
            df = pd.read_excel(file_upload)
            return df


def drop_columns(df, key):
    st.subheader("Drop Columns")
    column_names = []
    for i in df.columns:
        column_names.append(i)
    drop_cols = st.multiselect("Select Columns to be dropped.", column_names, key="{}".format(key))
    try:
        df = df.drop(drop_cols, axis=1)
    except:
        st.error("Invalid column names, please try again.")
    st.write(df.head(5))

    return df


def rename_cols(df):
    column_names = []
    for i in df.columns:
        column_names.append(i)


def float_regex(x):
    return re.findall(r"[-+]?\d*\.\d+|\d+", x)


