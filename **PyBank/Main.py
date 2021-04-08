import os
import csv



#Find file

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

pybank_path = os.path.join(dir_path, 'PyBank','Resources' )

print(pybank_path)

print(type(pybank_path))

os.chdir(pybank_path)


total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []


#Read file
with open('budget_data.csv', newline = "") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    
    cvs_header = next(csvreader)
    

    first_row = next(csvreader)
    
    total_months += 1
    
    total_pl += int(first_row[1])
    
    value = int(first_row[1])
    
    #header & first row 
    for row in csvreader:
        #dates
        dates.append(row[0])
        
        # Calculate change
        change = int(row[1])-value
        
        profits.append(change)
        
        value = int(row[1])
        
        #Total of months
        total_months += 1

        #Total net amount
        total_pl = total_pl + int(row[1])

    #Greatest increase 
    greatest_increase = max(profits)
    
    greatest_index = profits.index(greatest_increase)
    
    greatest_date = dates[greatest_index]

    #Greatest decrease  
    greatest_decrease = min(profits)
    
    worst_index = profits.index(greatest_decrease)
    
    worst_date = dates[worst_index]

    #Average change 
    avg_change = sum(profits)/len(profits)
    

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Output
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
