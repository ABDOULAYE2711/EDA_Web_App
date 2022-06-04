import numpy as np
import pandas as pd
import streamlit as st
import xlrd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#Web App Title
st.markdown('''
***The EDA App***

This is the **EDA App** created in streamlit using **pandas_profiling** library
''')

#Upload CSV data
with st.sidebar.header('1. Upload your excel data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input excel")
    st.sidebar.markdown("""
    [ABDOULAYE BADJI ]
    """)

# Pandas Profiling report
if uploaded_file is not None:
    @st.cache
    def load_excel():
        excel = pd.read_csv(uploaded_file, encoding='latin-1')
        return excel
    df = load_excel()
    pr=ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for csv file to be uploaded')
    if st.button('Press to use Example Dataset'):
        # Example Dataset
        @st.cache
        def load_data():
            a=pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a','b','c','d','e']
            )
            return a
        df=load_data()
        pr=ProfileReport(df,explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
        

