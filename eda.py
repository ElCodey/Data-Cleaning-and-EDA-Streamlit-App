import streamlit as st


def data_eda(df, key):
    # st.sidebar.selectbox("Use Example CSV", ["dummy_df", "dumm_df_2"])

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
