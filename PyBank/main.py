import os
import csv

budget_csv = os.path.join("budget_data.csv")

with open(budget_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    number_month=0
    total=0
    increase=0
    loss=0
    month_great_increase=""
    month_great_loss=""
    for row in csvreader:
        number_month+=1
        total+=float(row[1])
        if float(row[1])>=float(increase):
           increase=float(row[1])
           month_great_increase=row[0]
        if float(row[1])<=float(loss):
           loss=float(row[1])
           month_great_loss=row[0]


average_change=total/number_month

print("Financial Analysis")
print("-------------------------")
print("Total Months: "+str(number_month))
print("Total: "+"$"+str(total))
print("Average Change: "+"$"+str(average_change))
print("Great Increase in Profits:"+month_great_increase+"(" + "$"+str(increase)+")")
print("Great Decrease in Profits:"+month_great_loss+"(" + "$"+str(loss)+")")

text_file = open("Output.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("-------------------------\n")
text_file.write("Total Months: "+str(number_month)+"\n")
text_file.write("Total: "+"$"+str(total)+"\n")
text_file.write("Average Change: "+"$"+str(average_change)+"\n")
text_file.write("Great Increase in Profits:"+month_great_increase+"(" + "$"+str(increase)+")\n")
text_file.write("Great Decrease in Profits:"+month_great_loss+"(" + "$"+str(loss)+")\n")
text_file.close()
