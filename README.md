# Statistical Computing - Assignment 1

This project is created for **Statistical Computing Assignment 1**. It contains a Python script ([sample_data.py] designed to perform fundamental descriptive statistical computations on a sample dataset.

---

## 📌 Overview

The script demonstrates how to compute essential statistical measures directly using Python's standard library (`statistics` and `math`), requiring **no external third-party installations** (no `pip install` needed).

### What the Script Does:

1. **Defines Sample Data**: Uses a realistic dataset of 12 student exam scores.
2. **Computes Measures of Central Tendency**:
   - **Mean**: The arithmetic average of all data points ($\bar{x} = \frac{\sum x}{n}$).
   - **Median**: The middle value of the sorted dataset.
   - **Mode**: The most frequently occurring score.
3. **Computes Measures of Dispersion (Spread)**:
   - **Minimum & Maximum**: The lowest and highest values in the dataset.
   - **Range**: The difference between maximum and minimum values.
   - **Sample Variance ($s^2$)**: The average squared deviation from the mean (with degrees of freedom $n - 1$).
   - **Sample Standard Deviation ($s$)**: The square root of sample variance, indicating typical deviation from the mean.
4. **Calculates Quartiles and Five-Number Summary**:
   - **Q1 (25th percentile)**
   - **Q2 (Median / 50th percentile)**
   - **Q3 (75th percentile)**
   - **Interquartile Range (IQR)**: Difference between Q3 and Q1 ($IQR = Q_3 - Q_1$).

---

##  How to Run the Script

### Prerequisites
- Python 3.8 or higher installed on your computer.

### Execution Command
Open your terminal (PowerShell, Command Prompt, or bash) in this folder and run:

```bash
python sample_data.py
```

---

## 📊 Sample Output

```text
=======================================================
       STATISTICAL COMPUTING - ASSIGNMENT 1
=======================================================
Raw Data (Exam Scores): [78, 85, 92, 65, 74, 88, 92, 80, 95, 71, 84, 90]
Total Observations (n): 12
-------------------------------------------------------
MEASURES OF CENTRAL TENDENCY:
  - Mean   (Average) : 82.83
  - Median (Middle)  : 84.50
  - Mode   (Common)  : 92
-------------------------------------------------------
MEASURES OF SPREAD / DISPERSION:
  - Minimum Value    : 65
  - Maximum Value    : 95
  - Range            : 30
  - Sample Variance  : 87.97
  - Sample Std. Dev. : 9.38
-------------------------------------------------------
FIVE-NUMBER SUMMARY (Sorted Data):
  Sorted Array: [65, 71, 74, 78, 80, 84, 85, 88, 90, 92, 92, 95]
  - Q1 (25th Percentile)       : 75.00
  - Q2 (Median / 50th Perc.)   : 84.50
  - Q3 (75th Percentile)       : 91.50
  - Interquartile Range (IQR)  : 16.50
=======================================================
Analysis completed successfully!
```

---

## 🔑 Essential Points & Notes 

- **Zero External Dependencies**: Uses built-in Python modules (`statistics`), making it 100% portable and easy to run on any machine.
- **Customizable**: You can replace the numbers inside `data = [...]` in sample_data.py with any dataset you want to analyze.

