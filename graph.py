import matplotlib.pyplot as plt

# 10-year data (example trend)
years = list(range(2013, 2023))

literacy_rate = [60, 62, 64, 67, 69, 72, 75, 77, 80, 83]
school_enrollment = [55, 58, 60, 63, 66, 69, 72, 74, 77, 81]

# Create figure
plt.figure(figsize=(10,6))

# Plot lines
plt.plot(years, literacy_rate, marker='o', linewidth=2, label='Literacy Rate (%)')
plt.plot(years, school_enrollment, marker='s', linewidth=2, linestyle='--', label='School Enrollment (%)')

# Highlight growth area
plt.fill_between(years, literacy_rate, alpha=0.1)
plt.fill_between(years, school_enrollment, alpha=0.1)

# Titles and labels
plt.title("10-Year Growth in Education (SDG 4)", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Percentage (%)")

# Grid
plt.grid(True, linestyle='--', alpha=0.5)

# Legend
plt.legend()

# Annotate last values (to show growth clearly)
plt.text(years[-1], literacy_rate[-1], f"{literacy_rate[-1]}%", fontsize=10)
plt.text(years[-1], school_enrollment[-1], f"{school_enrollment[-1]}%", fontsize=10)

# Layout
plt.tight_layout()

# Show graph
plt.show()