"""
Statistical Computing - Assignment 1
Script: sample_data.py
Description: A script demonstrating fundamental descriptive 
             statistics (measures of central tendency and dispersion) on sample data.
"""

import math
import statistics

def main():

    # 1. Sample Data

    # A list representing student exam scores out of 100
    data = [78, 85, 92, 65, 74, 88, 92, 80, 95, 71, 84, 90]
    
    print("=" * 55)
    print("       STATISTICAL COMPUTING - ASSIGNMENT 1")
    print("=" * 55)
    print(f"Raw Data (Exam Scores): {data}")
    print(f"Total Observations (n): {len(data)}")
    print("-" * 55)

    
    # 2. Measures of Central Tendency

    # Mean: The arithmetic average of all data points
    mean_value = statistics.mean(data)

    # Median: The middle value when data is sorted in ascending order
    median_value = statistics.median(data)

    # Mode: The most frequently occurring value in the dataset
    mode_value = statistics.mode(data)

    print("MEASURES OF CENTRAL TENDENCY:")
    print(f"  - Mean   (Average) : {mean_value:.2f}")
    print(f"  - Median (Middle)  : {median_value:.2f}")
    print(f"  - Mode   (Common)  : {mode_value}")
    print("-" * 55)

 
    # 3. Measures of Spread / Dispersion
  
    # Minimum and Maximum values
    min_val = min(data)
    max_val = max(data)

    # Range: Difference between highest and lowest value
    data_range = max_val - min_val

    # Sample Variance (s^2): Average of squared differences from the mean
    variance_value = statistics.variance(data)

    # Sample Standard Deviation (s): Square root of sample variance
    stdev_value = statistics.stdev(data)

    print("MEASURES OF SPREAD / DISPERSION:")
    print(f"  - Minimum Value    : {min_val}")
    print(f"  - Maximum Value    : {max_val}")
    print(f"  - Range            : {data_range}")
    print(f"  - Sample Variance  : {variance_value:.2f}")
    print(f"  - Sample Std. Dev. : {stdev_value:.2f}")
    print("-" * 55)

    # 4. Five-Number Summary & Quartiles

    sorted_data = sorted(data)
    print("FIVE-NUMBER SUMMARY (Sorted Data):")
    print(f"  Sorted Array: {sorted_data}")
    
    # Quartiles divide sorted data into 4 equal quarters
    # statistics.quantiles requires Python 3.8+ (n=4 for quartiles)
    q1, q2, q3 = statistics.quantiles(data, n=4)
    iqr = q3 - q1

    print(f"  - Q1 (25th Percentile)       : {q1:.2f}")
    print(f"  - Q2 (Median / 50th Perc.)   : {q2:.2f}")
    print(f"  - Q3 (75th Percentile)       : {q3:.2f}")
    print(f"  - Interquartile Range (IQR)  : {iqr:.2f}")
    print("=" * 55)
    print("Analysis completed successfully!")

if __name__ == "__main__":
    main()
