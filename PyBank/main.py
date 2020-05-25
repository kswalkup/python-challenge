#import csv 
import os
import csv

months = []
finData = []
plChg = []

budgetData_csv = os.path.join("Resources","budget_data.csv")

with open(budgetData_csv) as csvfile:
    next(csvfile)
    
    csvreader = csv.reader(csvfile, delimiter=",") 

    for row in csvreader:
        finData.append(int(row[1]))
        months.append(row[0])

    #calculate P&L/change
    for totals in range(1, len(finData)):
        plChg.append((int(finData[totals]) - int(finData[totals-1])))
    
    #calculate average change
    avgChg = round(sum(plChg) / len(plChg),2)
    
    #calculate total length of months
    totalMonths = len(months)

    #greatest increase $ / date
    profitIncrease = max(plChg)
    dateIncrease = (months[plChg.index(max(plChg))+1])
    
    #greatest decrease $
    profitDecrease = min(plChg)
    dateDecrease = (months[plChg.index(min(plChg))+1])

    #print to terminal

    print("Financial Analysis")
    print("======================")
    print("Total Months: " + str(totalMonths))
    print("Total : $" + str(sum(finData)))
    print("Average change: $" + str(avgChg))
    print(f'Greatest Increase in Profits {dateIncrease} ${profitIncrease}.')
    print(f'Greatest Increase in Profits {dateDecrease} ${profitDecrease}.')

    #print to file
    f = open("financial_analysis.txt", "a")
    print("Financial Analysis", file=f)
    print("======================", file=f)
    print("Total Months: " + str(totalMonths), file=f)
    print("Total : $" + str(sum(finData)), file=f)
    print("Average change: $" + str(avgChg), file=f)
    print(f'Greatest Increase in Profits {dateIncrease} ${profitIncrease}.', file=f)
    print(f'Greatest Increase in Profits {dateDecrease} ${profitDecrease}.', file=f)
    f.close()