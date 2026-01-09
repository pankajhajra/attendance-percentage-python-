import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.title("📊 Attendance Percentage Analyzer")

st.write("This app analyzes student attendance and visualizes attendance percentage.")

# Step 1: Create attendance data
data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Total_Classes": [100, 100, 100, 100],
    "Attended_Classes": [85, 92, 60, 75]
}

df = pd.DataFrame(data)

# Step 2: Calculate attendance percentage
df["Attendance_Percentage"] = (df["Attended_Classes"] / df["Total_Classes"]) * 100

# Step 3: Categorize students
def category(percent):
    if percent >= 75:
        return "Good"
    elif percent >= 60:
        return "Average"
    else:
        return "Poor"

df["Category"] = df["Attendance_Percentage"].apply(category)

# Step 4: Display table
st.subheader("📋 Attendance Data")
st.dataframe(df)

# Step 5: Plot bar chart
st.subheader("📈 Attendance Percentage Chart")

fig, ax = plt.subplots()
ax.bar(df["Name"], df["Attendance_Percentage"])
ax.set_xlabel("Students")
ax.set_ylabel("Attendance Percentage")
ax.set_title("Student Attendance Analysis")

st.pyplot(fig)
