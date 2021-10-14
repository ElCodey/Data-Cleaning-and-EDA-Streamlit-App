import pandas as pd
import streamlit as st
import re

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
  

def data_eda(df, key):
    #st.sidebar.selectbox("Use Example CSV", ["dummy_df", "dumm_df_2"])
    
    
    eda_option = st.selectbox("Select EDA Option", ["View DF", "Head", "Tail", "Column Names",
                                                    "Shape", "DF Stats", "Null Values"], key="{}".format(key))
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

    



def col_eda(df, key):
    column_names = []
    for i in df.columns:
        column_names.append(i)
    col1, col2 = st.columns(2)
    col_select = col1.selectbox("Select Columns to Explore", column_names, key="{}".format(key))
    eda_select = col2.selectbox("Select Option to Explore", ["Choose Option", "Data Types", "Value Counts", "Mean", "Median",
                                                            "Groupby & Mean", "Groupby & Median"], key="{}".format(key))
    if eda_select == "Data Types":
        st.write(df[col_select].dtypes)
    if eda_select == "Value Counts":
        st.write(df[col_select].value_counts())
    if eda_select == "Mean":
        try:
            st.write(df[col_select].mean())
        except:
            st.error("Invalid Data Type")
    if eda_select == "Median":
        try:
            st.write(df[col_select].median())
        except:
            st.error("Invalid Data Type")
    if eda_select == "Groupby & Mean":
        try:
            st.write(df.groupby(col_select).mean())
        except:
            st.error("Invalid Data Type")
    if eda_select == "Groupby & Median":
        try:
            st.write(df.groupby(col_select).median())
        except:
            st.error("Invalid Data Type")


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

def convert_to_int_if_error_return_zero(x):
    try:
        return int(x)
    except:
        return 0  

def convert_to_float_if_error_return_zero(x):
    try:
        return float(x)
    except:
        return 0  
def float_regex(x):
    return re.findall(r"[-+]?\d*\.\d+|\d+", x)

def value_transform(df, key):
    st.subheader("Value Transformations")

    column_names = ["Select Column"]
    for i in df.columns:
        column_names.append(i)
    col1, col2 = st.columns(2)
    col_transform = col1.selectbox("Select Column to Transform", column_names, key="{}".format(key))
    type_transform = col2.selectbox("Select Transformation", ["Select Option", "Replace Values", "Remove Whitespace",
                                                              "Extract Positive Ints", "Extract Float"], key="{}".format(key))
    if type_transform == "Remove Whitespace":
        df[col_transform] = df[col_transform].str.replace(" ", "")
    if type_transform == "Replace Values":
        replace_text = st.text_input("Input Values to Replace")
        replace_with_text = st.text_input("Input Value to Replace with. Press Enter in box to remove value")
        try:
            df[col_transform] = df[col_transform].str.replace(replace_text, replace_with_text)
        except:
            st.error("An error has occured.")
    if type_transform == "Extract Positive Ints":
        df[col_transform] = df[col_transform].apply(lambda x: "".join(filter(str.isdigit, x)))
    if type_transform == "Extract Float":
        df[col_transform] = df[col_transform].apply(str)
        df[col_transform] = df[col_transform].apply(lambda x: "".join(float_regex(x)))
        df[col_transform] = df[col_transform].apply(str)
    if col_transform != "Select Column":
        st.write(df[col_transform])
    
    return df

def dtype_convert(df, key):
    st.subheader("Data Type Convert")
    

    column_names = ["Select Column"]
    for i in df.columns:
        column_names.append(i)
    col1, col2 = st.columns(2)
    col_convert = col1.selectbox("Select Column to Convert Data Type", column_names, key="{}".format(key))
    type_convert = col2.selectbox("Select Type to Convert", ["Select Type", "String", "Int", "Float"], key="{}".format(key))
    if type_convert == "String":
        try:
            df[col_convert] = df[col_convert].astype(str)
        except:
            st.error("Can't Convert")
    elif type_convert == "Int":
        try:
            df[col_convert] = df[col_convert].apply(convert_to_int_if_error_return_zero)
        except:
            st.error("Can't Convert")
    elif type_convert == "Float":
        try:
            df[col_convert] = df[col_convert].apply(convert_to_float_if_error_return_zero)
        except:
            st.error("Can't Convert")
    if col_convert != "Select Column":
        st.write(df[col_convert])
    return df

def remove_null(df, key):
    st.subheader("Remove Null Values")
    st.write(df.isnull().sum())
    column_names = ["Select Column"]
    for i in df.columns:
        column_names.append(i)
    col1, col2 = st.columns(2)
    col_select = col1.selectbox("Select Column to replace Null with Mean or Median (Int or Float Only)", column_names, key="{}".format(key))
    option_select = col2.selectbox("Mean or Median", ["Select Option", "Mean", "Median"], key="{}".format(key))
    if option_select == "Mean":
        try:
            df[col_select] = df[col_select].fillna(df[col_select].mean())
        except:
            st.error("Invalid Column Type to fill with Mean")
    elif option_select == "Median":
        try:
            df[col_select] = df[col_select].fillna(df[col_select].median())
        except:
            st.error("Invalid Column Type to fill with Median")
   

    null_clean = st.selectbox("Drop All Null Values", ["Please Select Option", "Remove Null Values"], key="{}".format(key))
    if null_clean == "Remove Null Values":
        df = df.dropna()
    st.write(df.shape)

    return df



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
df = file_upload()
main(df, 1)