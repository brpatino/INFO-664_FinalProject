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

with open('Caloocan_police.csv') as caloocan_police_data_input:
    caloocan_police_results = csv.reader(caloocan_police_data_input)
    
    next(caloocan_police_results)
    
    for row in caloocan_police_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]
        station = row[3]
        type_killing = row[4]
        print(date)
        
with open('Caloocan_unidentified.csv') as caloocan_unidentified_data_input:
    caloocan_unidentified_results = csv.reader(caloocan_unidentified_data_input)
    
    next(caloocan_unidentified_results)
    
    for row in caloocan_unidentified_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]
        station = row[3]
        type_killing = row[4]
        print(date)

with open('QuezonCity_police.csv') as QuezonCity_police_data_input:
    QuezonCity_police_results = csv.reader(QuezonCity_police_data_input)
    
    next(QuezonCity_police_results)
    
    for row in QuezonCity_police_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]
        station = row[3]
        type_killing = row[4]
        print(date)
        
with open('QuezonCity_unidentified.csv') as QuezonCity_unidentified_data_input:
    QuezonCity_unidentified_results = csv.reader(QuezonCity_unidentified_data_input)
    
    next(QuezonCity_unidentified_results)
    
    for row in QuezonCity_unidentified_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]
        station = row[3]
        type_killing = row[4]
        print(date)
        
with open('Manila_police.csv') as Manila_police_data_input:
    Manila_police_results = csv.reader(Manila_police_data_input)
    
    next(Manila_police_results)
    
    for row in Manila_police_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]
        station = row[3]
        type_killing = row[4]
        print(date)
        
with open('Manila_unidentified.csv') as Manila_unidentified_data_input:
    Manila_unidentified_results = csv.reader(Manila_unidentified_data_input)
    
    next(Manila_unidentified_results)
    
    for row in Manila_unidentified_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]
        station = row[3]
        type_killing = row[4]
        print(date)
