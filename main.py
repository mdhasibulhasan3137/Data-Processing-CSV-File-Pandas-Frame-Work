# importing pandas library 
import pandas as pd 
  
# creating and initializing a nested list 
nobab = [['Shuvo', 24, 'SanFrancisco', 'United States'], 
            ['Sagor', 23, 'London', 'United Kingdom'], 
            ['Jamil', 22, 'Rome', 'Italy'], 
            ['Imtiaj', 21, 'New York', 'United States'], 
            ['Rafi', 20, 'Las Vegas', 'United States'], 
            ['Hasan', 19, 'Berlin', 'Germany']] 
  
# Create a DataFrame object 
df = pd.DataFrame(nobab, 
                  columns=['Name', 'Age', 'City', 'Country'], 
                  ) 
  
# Creating 2 lists 'marks' and 'gender' 
marks = [69.5,98.9,97.2,96.2,95.5,94.5] 
gender = ['M','M','M','M','M','M'] 
  
# adding lists as new column to dataframe df 
df['Marks'] = marks 
df['Gender'] = gender 

# Creating 1 lists 'status'
status=['Married','Married','Single','Divorce','Single','Pure Single']

# adding lists as new column to dataframe df 
df['Status'] = status
  
#Creating CSV file
df.to_csv('die.csv') 

# Displaying the Data frame 
df


#Updating CSV File

df = pd.read_csv("die.csv") 
  
# updating the column value/data 
df.loc[1, 'Marks'] = '70.9'
  
# Displaying the Data frame 
df


#Delete Data From CSV File Row Wise
df = pd.read_csv("die.csv", index_col ="Name" ) 

  
# dropping passed values 
df.drop(["Hasan"], inplace = True) 

# display 
df

#Delete Data From CSV File Column Wise  
df = pd.read_csv("die.csv", index_col ="Name" ) 

# dropping passed columns 
df.drop(["Status"], axis = 1, inplace = True) 
  
# display 
df

