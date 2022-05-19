# importing pandas package
import pandas as pandasForSortingCSV
  
# assign dataset
csvData = pandasForSortingCSV.read_csv("NewPlayerRanks.csv")
                                         
# displaying unsorted data frame
print("\nBefore sorting:")
print(csvData)
  
# sort data frame
csvData.sort_values(csvData.columns[0], 
                    axis=0,
                    inplace=True)
  
# displaying sorted data frame
print("\nAfter sorting:")
print(csvData)