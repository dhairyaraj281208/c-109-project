import pandas as pd
import statistics
import csv

df = pd.read_csv("C:\\Users\\\Dhairya\\Desktop\\python\\c 109\\project\\c 109 project\\StudentsPerformance.csv")
reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()

# Mean for reading and writing
reading_mean = statistics.mean(reading_list)
writing_mean = statistics.mean(writing_list)
# Median for reading and writing
reading_median = statistics.median(reading_list)
writing_median = statistics.median(writing_list)
# Mode for reading and writing
reading_mode = statistics.mode(reading_list)
writing_mode = statistics.mode(writing_list)
# Printing mean, median and mode to validate
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(
    reading_mean, reading_median, reading_mode))
print("Mean, Median and Mode of writing is {}, {} and {} respectively".format(
    writing_mean, writing_median, writing_mode))
# Standard deviation for reading and writing
reading_std_deviation = statistics.stdev(reading_list)
writing_std_deviation  = statistics.stdev(writing_list)

# 1, 2 and 3 Standard Deviations for reading
reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean - \
    reading_std_deviation , reading_mean+reading_std_deviation 
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean - \
    (2*reading_std_deviation ), reading_mean+(2*reading_std_deviation )
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean - \
    (3*reading_std_deviation ), reading_mean+(3*reading_std_deviation )
# 1, 2 and 3 Standard Deviations for writing
writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean - \
    writing_std_deviation , writing_mean+writing_std_deviation 
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean - \
    (2*writing_std_deviation ), writing_mean+(2*writing_std_deviation )
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean - \
    (3*writing_std_deviation ), writing_mean+(3*writing_std_deviation )
# Percentage of data within 1, 2 and 3 Standard Deviations for reading
reading_list_of_data_within_1_std_deviation = [
    result for result in reading_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading_list if result >
                                              reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [
    result for result in reading_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]
# Percentage of data within 1, 2 and 3 Standard Deviations for writing
writing_list_of_data_within_1_std_deviation = [
    result for result in writing_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing_list if result >
                                              writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [
    result for result in writing_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]
# Printing data for reading and writing (Standard Deviation)
print("{}% of data for reading lies within 1 standard deviation".format(
    len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 2 standard deviations".format(
    len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 3 standard deviations".format(
    len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))
print("{}% of data for writing lies within 1 standard deviation".format(
    len(writing_list_of_data_within_1_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing lies within 2 standard deviations".format(
    len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing lies within 3 standard deviations".format(
    len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing_list)))
