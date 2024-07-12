import streamlit as st

st.write("""
    <span style="font-family: Arial, sans-serif; font-size: 26px;">
         <strong>
        Superstore Sales Reporting and Forecasting Dashboard
         </strong>
    </span>
""", unsafe_allow_html=True)

st.write("""
    <span style="font-family: Arial, sans-serif; font-size: 20px;">
        Our Power BI Super Store Sales Reporting and Forecasting Dashboard provides
          a comprehensive solution for analyzing sales and profit performance.
          Executives can make data-driven decisions by examining metrics across different regions, 
         categories, and segments. The dashboard includes sales analysis, profit analysis,
          and forecasting capabilities. Stakeholders gain actionable insights to drive business success!
    </span>
""", unsafe_allow_html=True)

video_file = open('output.mp4', 'rb')

video_bytes = video_file.read()
st.video(video_bytes)
