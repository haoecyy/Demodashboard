import streamlit as st

st.title("Retail business dashboard")
st.header("Manager input Section")
st.subheader("Please enter the data below.")
sales = st.number_input("Monthly sales target(in USD)", value=0)
region = st.selectbox("Select Region:", ["North", "East", "West", "South"])
if st.button("Submit"):
  if sales >= 100000:
    st.write("good job, great target")
st.success(f"your target is {sales} in {region}")


