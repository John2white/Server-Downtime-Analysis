import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "/content/Server Downtime.xlsx"  # Ensure the file is uploaded to your Colab session
df = pd.read_excel(file_path)

# Task (a): Frequency Distribution
frequency_distribution = df['Problem Experienced'].value_counts()

print("Frequency Distribution:")
print(frequency_distribution)

# Task (b): Bar Chart
plt.figure(figsize=(8, 5))
frequency_distribution.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Frequency of Downtime Causes", fontsize=14)
plt.xlabel("Downtime Cause", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Task (c): Histogram
plt.figure(figsize=(8, 5))
df['Downtime Minutes'].plot(kind='hist', bins=10, color='orange', edgecolor='black')
plt.title("Histogram of Downtime Minutes", fontsize=14)
plt.xlabel("Downtime Duration (minutes)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Task (d): Pie Chart
total_downtime = df.groupby('Problem Experienced')['Downtime Minutes'].sum()
plt.figure(figsize=(6, 6))
total_downtime.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title("Percentage of Total Downtime by Cause", fontsize=14)
plt.ylabel("")  # Hide y-axis label
plt.tight_layout()
plt.show()

# Task (e): Short Report
print("\nShort Report:")
print(f"The frequency distribution shows the most common cause of downtime is '{frequency_distribution.idxmax()}' "
      f"with {frequency_distribution.max()} occurrences. The pie chart reveals that the largest proportion of "
      f"downtime duration is attributed to '{total_downtime.idxmax()}', accounting for "
      f"{(total_downtime.max() / total_downtime.sum()) * 100:.2f}% of the total downtime.")
