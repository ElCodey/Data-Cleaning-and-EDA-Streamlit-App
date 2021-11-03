import streamlit as st
import sys
import pathlib

sys.path.append(str(pathlib.Path().absolute()).split("/src")[0])

from helpers import file_upload, drop_columns
from eda import data_eda, col_eda
from transformations import value_transform, dtype_convert, remove_null



st.set_option("deprecation.showfileUploaderEncoding", False)
st.title("Data Cleaning and Visualisation App")
st.subheader("EDA")
st.sidebar.subheader("Upload CSV/Excel file or use Example CSV")


# FKB always two empty lines between two functions, but only one line between comands


def main(df, key):
    data_eda(df, key)
    col_eda(df, key)
    df = drop_columns(df, key)  
    if st.button("Confirm Drop Column Changes", key="{}".format(key)):
        return main(df, key+1)       
    df = value_transform(df, key)
    if st.button("Confirm Value Transform Changes", key="{}".format(key)):
        return main(df, key+1)
    df = dtype_convert(df, key)
    if st.button("Confirm Data Convert Changes", key="{}".format(key)):
        return main(df, key+1)
    df = remove_null(df, key)
    if st.button("Confirm Null Changes", key="{}".format(key)):
        return main(df, key+1)


if __name__ == "__main__":
    # FKB Protector which protects imports from executing this lines
    df = file_upload()
    main(df, 1)
