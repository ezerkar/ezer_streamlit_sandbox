
import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 Streamlit in Snowflake!")

user_input = st.text_input("Enter your name:", "")

if user_input:
    st.write(f"Hello, {user_input}! 👋")

df = pd.DataFrame({
    "x": range(10),
    "y": [i**2 for i in range(10)]
})

st.write("Sample DataFrame:")
st.dataframe(df)

st.write("Sample Chart:")
chart = alt.Chart(df).mark_line().encode(x="x", y="y")
st.altair_chart(chart, use_container_width=True)
