import streamlit as st

from src.helpers import float_regex, convert_to_int_if_error_return_zero, convert_to_float_if_error_return_zero


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