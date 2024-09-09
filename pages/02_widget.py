import streamlit as st

name = st.text_input("Enter your name:")
# 输入框的类型为text_input，可以输入单行文字
if name:
    st.write(f"Hello, {name}")

st.divider()

password = st.text_input("Enter your password", type="password")
# 输入框的类型为text_input，可以输入单行文字，且输入内容会被隐藏

st.divider()

paragraph = st.text_area("Enter your message:")
# 输入框的类型为text_area，可以输入多行文字

st.divider()

age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25, step=1)
# 输入框的类型为number_input，可以输入数字。默认精度为2位小数

st.write(f"Your age is {age}")

st.divider()

checked = st.checkbox("I agree to the terms and conditions")
# 输入框的类型为checkbox，可以勾选或不勾选
if checked:
    st.write("Thank you for agreeing to the terms and conditions.")

st.divider()

submitted = st.button("Submit")
if submitted:
    st.write("Form submitted successfully!")