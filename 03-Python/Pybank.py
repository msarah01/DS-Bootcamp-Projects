import os
import csv
file_csv= "Resources/budget_data.csv"
file_output= "output.csv"
Total_months= 0
Monthly_change= []
Net_change_list= []
Greatest_increase_profit= ["",0]
Greatest_decrease_loss=["",10000000]
Total_net= 0
with open(file_csv) as file_df:
    reader= csv.reader(file_df)
    header=next(reader) 
    first_row= next(reader)
    Total_months= Total_months+1
    Total_net= Total_net + int(first_row[1])
    Previous_net= int(first_row[1])
    for row in reader:
        Total_months= Total_months+1
        Total_net= Total_net + int(row[1])
        Net_change= int(row[1])- Previous_net
        Previous_net= int(row[1])
        Net_change_list= Net_change_list +[Net_change]
        Monthly_change= Monthly_change+[row[0]]
        if Net_change>Greatest_increase_profit[1]:
            Greatest_increase_profit[0]= row[0]
            Greatest_increase_profit[1]= Net_change
        if Net_change<Greatest_decrease_loss[1]:
            Greatest_decrease_loss[0]=row[0]
            Greatest_decrease_loss[1]= Net_change
Monthly_average=sum(Net_change_list)/ len(Net_change_list)
output= (
    f'Total months: {Total_months}\n'
    f'Total net: {Total_net}\n'
    f'Average: {Monthly_average}\n'
    f'Greatest Increase in Profits: {Greatest_increase_profit}\n'
    f'Greatest Decrease in Losses:{Greatest_decrease_loss}\n'
    )
print(output)
            

