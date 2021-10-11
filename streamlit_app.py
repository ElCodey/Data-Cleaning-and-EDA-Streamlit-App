import pandas as pd
import streamlit as st
import io


st.set_option("deprecation.showfileUploaderEncoding", False)
st.title("Data Cleaning and Visualisation App")
st.subheader("EDA")
st.sidebar.subheader("Upload CSV/Excel file or use Example CSV")

def file_upload():
    df = pd.read_csv("bikes.csv")
    return df
###
    file_upload = st.sidebar.file_uploader(label="Upload CSV or Excel file", type=["csv", "xlsx"])

    if file_upload is not None:
        try:
            df = pd.read_csv(file_upload)
            return df
        except Exception as e:
            print(e)
            df = pd.read_excel(file_upload)
            return df
###
  

def data_eda():
    #st.sidebar.selectbox("Use Example CSV", ["dummy_df", "dumm_df_2"])
    df = file_upload()
    eda_option = st.selectbox("Select EDA Option", ["View DF", "Head", "Tail", "Column Names",
                                                    "Shape", "DF Stats", "Null Values"])
    if eda_option == "View DF":
        st.write(df)
    elif eda_option == "Head":
        st.write(df.head(5))
    elif eda_option == "Tail":
        st.write(df.tail(5))
    elif eda_option == "Column Names":
        st.write(df.columns)
    elif eda_option == "Shape":
        st.write(df.shape)
    elif eda_option == "DF Stats":
        st.write(df.describe())
    elif eda_option == "Null Values":
        st.write(df.isnull().sum())

    return df

df = data_eda()

def col_eda(df):
    column_names = []
    for i in df.columns:
        column_names.append(i)
    col_select = st.selectbox("Select Columns to Explore", column_names)
    eda_select = st.selectbox("Select Option to Explore", ["Choose Option", "Data Types", "Value Counts", "Mean", "Median",
                                                            "Groupby & Mean", "Groupby & Median"])
    if eda_select == "Data Types":
        st.write(df[col_select].dtypes)
    if eda_select == "Value Counts":
        st.write(df[col_select].value_counts())
    if eda_select == "Mean":
        try:
            st.write(df[col_select].mean())
        except:
            st.write("Invalid Data Type")
    if eda_select == "Median":
        try:
            st.write(df[col_select].median())
        except:
            st.write("Invalid Data Type")
    if eda_select == "Groupby & Mean":
        try:
            st.write(df.groupby(col_select).mean())
        except:
            st.write("Invalid Data Type")
    if eda_select == "Groupby & Median":
        try:
            st.write(df.groupby(col_select).median())
        except:
            st.write("Invalid Data Type")

col_eda(df)
def drop_columns(df):
    column_names = []
    for i in df.columns:
        column_names.append(i)
    drop_cols = st.multiselect("Select Columns to be dropped.", column_names)
    try:
        df = df.drop(drop_cols, axis=1)
    except:
        st.write("Invalid column names, please try again.")
    st.write(df.head(5))
    return df

df = drop_columns(df)

def rename_cols(df):
    column_names = []
    for i in df.columns:
        column_names.append(i)
    

def data_clean(df):
    st.subheader("Removing Null Values")
    st.write(df.isnull().sum())
    
    column_names = ["Select Column"]
    for i in df.columns:
        column_names.append(i)

    col_convert = st.selectbox("Select Column to Convert Data Type", column_names)
    type_convert = st.selectbox("Select Type to Convert", ["Select Type", "String", "Int", "Float"])
    if type_convert == "String":
        try:
            df[col_convert] = df[col_convert].astype(str)
        except:
            st.write("Can not convert")
    elif type_convert == "Int":
        try:
            df[col_convert] = df[col_convert].astype(int)
        except:
            st.write("Can not convert")
    elif type_convert == "Float":
        try:
            df[col_convert] = df[col_convert].astype(float)
        except:
            st.write("Can not convert")
    col_select = st.selectbox("Select Column to replace Null with Mean or Median", column_names)
    option_select = st.selectbox("Mean or Median", ["Select Option", "Mean", "Median"])
    if option_select == "Mean":
        try:
            df[col_select] = df[col_select].fillna(df[col_select].mean())
        except:
            st.write("Invalid Column Type to fill with Mean")
    elif option_select == "Median":
        try:
            df[col_select] = df[col_select].fillna(df[col_select].median())
        except:
            st.write("Invalid Column Type to fill with Median")
   

    null_clean = st.selectbox("Drop All Null Values", ["Please Select Option", "Remove Null Values"])
    if null_clean == "Remove Null Values":
        df = df.dropna()
    st.write(df.shape)
    return df
    

data_clean(df)