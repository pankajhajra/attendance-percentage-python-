

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Total_Classes": [100, 100, 100, 100],
    "Attended_Classes": [85, 92, 60, 75]
}

df = pd.DataFrame(data)

# Save data to CSV
df.to_csv("attendance.csv", index=False)

# Step 2: Read CSV file
df = pd.read_csv("attendance.csv")

# Step 3: Calculate attendance percentage
df["Attendance_Percentage"] = (df["Attended_Classes"] / df["Total_Classes"]) * 100

# Step 4: Categorize students
def category(percent):
    if percent >= 75:
        return "Good"
    elif percent >= 60:
        return "Average"
    else:
        return "Poor"

df["Category"] = df["Attendance_Percentage"].apply(category)

# Step 5: Display result
print("\nAttendance Analysis:\n")
print(df)

# Step 6: Plot attendance percentage
plt.bar(df["Name"], df["Attendance_Percentage"])
plt.xlabel("Students")
plt.ylabel("Attendance Percentage")
plt.title("Student Attendance Analysis")
plt.show()
