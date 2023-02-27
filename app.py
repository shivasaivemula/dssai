import streamlit as st

st.title("Shivasai vemula ")
st.write("check out this github[link](https://github.com/shivasaivemula)")
st.write("check out this linkedin[link](https://www.linkedin.com/in/shivasai-vemula-306169264)")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()
