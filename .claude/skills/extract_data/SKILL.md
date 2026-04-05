---
Name: ExtractData
Description: Extract structured data from the following github repository
---

### Extract structured data from the following github repository

### Step1: 
1. don't create a new venv . use existing venv called claude
2. create the helper files under the folder skills/extract_Data/assets/
3. try to reuse the same file. if there is any issue modify the existing file but don't create a new file. if you create a new file then you will have to update the skill definition file and that is not good. so try to reuse the same file and if there is any issue then modify the existing file but don't create a new file.


#### Step1:
Go to the following URLs
https://github.com/saiprashanthts1995/Github_action_practice/blob/main/iris.csv

#### Step2:
Extract the data from above URL and do a quality check on all colummns to make sure there are no null values or missing values. If there are any null values or missing values, please fill them with the mean value of the respective column.

#### Step3:
After filling the null values, please provide a summary of the data including the mean, median, and standard deviation for each column.

#### Step4:
Finally, please provide a visualization of the data using a pair plot to show the relationships between the different columns.

#### Step5: 
save the data in a json file and store it in output/<current_date>/extracted_data_<current_timestamp>.json