#Final Project

#APPROACH:
##Research and structure data to import into Tableau
# * research into how data should be input into Tableau
# * specify the data analysis to be done in Tableau to better enrich and structure data

##Enrich data
# * add geographical coordinates to police station locations
# * fix "x" and checkmark symbols in the reportage 
# * check data analysis on drugarchive.ph, provide a data analysis not yet provided. 
        # -- NCR by city; nationwide by provice
        # -- chart of deaths by type incident
        # -- number of deaths by day




import csv

with open('PHdata.csv') as data_input:
    data_results = csv.reader(data_input)
    
    next(data_results)
    
    for row in data_results:
        date = row[0]
        location = row[1]
        station = row[2]
        type_killing = row[3]
        print(date)
