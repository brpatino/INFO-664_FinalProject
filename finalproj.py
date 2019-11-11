#Final Project

#APPROACH:
##Research and structure data to import into Tableau
# * research into how data should be input into Tableau
# * specify the data analysis to be done in Tableau to better enrich and structure data

##Enrich data
# * add geographical coordinates to police station locations
# * check data analysis on drugarchive.ph, provide a data analysis not yet provided. 
        # -- NCR by city; nationwide by provice
        # -- chart of deaths by type incident
        # -- number of deaths by day
        
#UPDATES DONE:
#INSTALLED PANDAS!
#UPDATED DATA TO INCLUDE TYPE OF KILLING FOR ALL DATASETS! BASICALLY ADDED A COLUMN!



import csv
import pandas

#CALOOCAN DATA
with open('Caloocan_police.csv') as caloocan_police_data_input:
    caloocan_police_results = csv.reader(caloocan_police_data_input)
    
    next(caloocan_police_results)
    
    for row in caloocan_police_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]

#Adding column so that type of killing is in the CSV
output_Caloocan_police = pandas.read_csv('Caloocan_police.csv')
output_Caloocan_police['Assailant'] = 'Police'
print(output_Caloocan_police)


with open('Caloocan_unidentified.csv') as caloocan_unidentified_data_input:
    caloocan_unidentified_results = csv.reader(caloocan_unidentified_data_input)
    
    next(caloocan_unidentified_results)
    
    for row in caloocan_unidentified_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]

output_Caloocan_unidentified = pandas.read_csv('Caloocan_unidentified.csv')
output_Caloocan_unidentified['Assailant'] = 'Unidentified'
print(output_Caloocan_unidentified)

#QUEZON CITY DATA

with open('QuezonCity_police.csv') as QuezonCity_police_data_input:
    QuezonCity_police_results = csv.reader(QuezonCity_police_data_input)
    
    next(QuezonCity_police_results)
    
    for row in QuezonCity_police_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]

output_QuezonCity_police = pandas.read_csv('QuezonCity_police.csv')
output_QuezonCity_police['Assailant'] = 'Police'
print(output_QuezonCity_police)
        
with open('QuezonCity_unidentified.csv') as QuezonCity_unidentified_data_input:
    QuezonCity_unidentified_results = csv.reader(QuezonCity_unidentified_data_input)
    
    next(QuezonCity_unidentified_results)
    
    for row in QuezonCity_unidentified_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]

output_QuezonCity_unidentified = pandas.read_csv('QuezonCity_unidentified.csv')
output_QuezonCity_unidentified['Assailant'] = 'Unidentified'
print(output_QuezonCity_unidentified)

#MANILA DATA
with open('Manila_police.csv') as Manila_police_data_input:
    Manila_police_results = csv.reader(Manila_police_data_input)
    
    next(Manila_police_results)
    
    for row in Manila_police_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]
        
output_Manila_police = pandas.read_csv('Manila_police.csv')
output_Manila_police['Assailant'] = 'Police'
print(output_Manila_police)
        
with open('Manila_unidentified.csv') as Manila_unidentified_data_input:
    Manila_unidentified_results = csv.reader(Manila_unidentified_data_input)
    
    next(Manila_unidentified_results)
    
    for row in Manila_unidentified_results:
        id_victim = row[0]
        date = row[1]
        location = row[2]
        
output_Manila_unidentified = pandas.read_csv('Manila_unidentified.csv')
output_Manila_unidentified['Assailant'] = 'Unidentified'
print(output_Manila_unidentified)

#NEXT STEPS
#pandas to add new row and populate rows with type of killing (police) (assailant)
#do this with rest of data -- DONE
#export all this stuff as a JSON file of data that I need for Tableau!
