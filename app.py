import streamlit as st
from streamlit_option_menu import option_menu
import dataset
import activeEnrollment, home, financialAnalysis, demographics
# Define the CSS style for the iframe
iframe_style = """
    width: 1024px; 
    height: 612px;
    border: none 
"""

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Dataset", "Active Enrollment", "Financial Analysis", 'Enrollment Demographics'], 
    icons=['house', 'database', "bar-chart-line", 'currency-dollar', 'people', 'table'], 
    menu_icon="cast", default_index=0, orientation="vertical")

if selected == "Home":
    home.main(st)
elif selected == "Dataset":
    st.markdown("""
    <h3 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>DATASET: Student Information</h3>
    """, unsafe_allow_html=True)
    
    # Note to TA
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #FF3131; margin-bottom: -10px;'>PLEASE NOTE:</h4>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: justify;'>
    <strong><em>This dataset has been obtained from a real business. Student names have been removed for
            confidentiality purposes. Please feel free to click on the "Fullscreen" option to view
            the entire dataset.</em></strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=700, output_format='auto')
    st.write("\n\n")
    
    df = dataset.load_data()    
    st.write(df)
    
    dataset.describe_dataset()
    
elif selected == "Active Enrollment":
    activeEnrollment.main(st, iframe_style)
elif selected == "Financial Analysis":
    financialAnalysis.main(st, iframe_style)
elif selected == "Enrollment Demographics":
    demographics.main(st, iframe_style)

