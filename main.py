import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Total_Classes": [100, 100, 100, 100],
    "Attended_Classes": [85, 92, 60, 75]
}

df = pd.DataFrame(data)

df.to_csv("attendance.csv", index=False)
df = pd.read_csv("attendance.csv")
df["Attendance_Percentage"] = (df["Attended_Classes"] / df["Total_Classes"]) * 100
def category(percent):
    if percent >= 75:
        return "Good"
    elif percent >= 60:
        return "Average"
    else:
        return "Poor"

df["Category"] = df["Attendance_Percentage"].apply(category)
print("\nAttendance Analysis:\n")
print(df)
plt.bar(df["Name"], df["Attendance_Percentage"])
plt.xlabel("Students")
plt.ylabel("Attendance Percentage")
plt.title("Student Attendance Analysis")
plt.show()
