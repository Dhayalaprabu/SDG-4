# EX08 Visualizing SDG 4 Data Using Python



---

## AIM:

To visualize the growth of education metrics over a 10-year period using Python and represent SDG 4 (Quality Education) through graphical analysis.

---

## DESIGN STEPS:

### Step 1:

Import the required library (matplotlib).

### Step 2:

Prepare the dataset for a 10-year period.

### Step 3:

Define variables for literacy rate and school enrollment.

### Step 4:

Create a plotting figure using matplotlib.

### Step 5:

Plot line graphs for both datasets.

### Step 6:

Enhance visualization using markers and line styles.

### Step 7:

Highlight growth using shaded regions.

### Step 8:

Add titles and axis labels.

### Step 9:

Include grid and legend for clarity.

### Step 10:

Display the graph.

---

## PROGRAM:

```python id="sdg904"
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

# Annotate last values
plt.text(years[-1], literacy_rate[-1], f"{literacy_rate[-1]}%", fontsize=10)
plt.text(years[-1], school_enrollment[-1], f"{school_enrollment[-1]}%", fontsize=10)

# Layout
plt.tight_layout()

# Show graph
plt.show()
```

---

## OUTPUT:

<img width="1233" height="834" alt="image" src="https://github.com/user-attachments/assets/cfdd26ac-9b8f-4fc0-a0e2-c825c91b816a" />


---

## RESULT:

The program successfully visualizes the 10-year growth of education indicators using Python. The graph clearly represents SDG 4 (Quality Education) by showing improvements in literacy rate and school enrollment.
