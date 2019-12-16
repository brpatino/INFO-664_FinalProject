#First download the data from here (link below) and saved each tab of data as a CSV file. https://github.com/HRDAG/PH-drug-related-killings/tree/master/import/input
#This code adds a column for "assailant" in each of the six CSV files. this information is crucial for the analysis.
#This data rewrites 6 csv files to include the new "assailant" comumn.

import csv
import pandas

#Adding column so that type of killing is in the CSV

#CALOOCAN DATA - POLICE
output_Caloocan_police = pandas.read_csv('Caloocan_police.csv')
output_Caloocan_police['Assailant'] = 'Police'

output_Caloocan_police.to_csv('Caloocan_police.csv', index=False)

#CALOOCAN DATA - UNIDENTIFIED
output_Caloocan_unidentified = pandas.read_csv('Caloocan_unidentified.csv')
output_Caloocan_unidentified['Assailant'] = 'Unidentified'

output_Caloocan_unidentified.to_csv('Caloocan_unidentified.csv', index=False)

#QUEZON CITY DATA - POLICE
output_QuezonCity_police = pandas.read_csv('QuezonCity_police.csv')
output_QuezonCity_police['Assailant'] = 'Police'

output_QuezonCity_police.to_csv('QuezonCity_police.csv', index=False)

#QUEZON CITY DATA - UNIDENTIFIED
output_QuezonCity_unidentified = pandas.read_csv('QuezonCity_unidentified.csv')
output_QuezonCity_unidentified['Assailant'] = 'Unidentified'
output_QuezonCity_unidentified.to_csv('QuezonCity_unidentified.csv', index=False)


#MANILA DATA - POLICE
output_Manila_police = pandas.read_csv('Manila_police.csv')
output_Manila_police['Assailant'] = 'Police'
output_Manila_police.to_csv('Manila_police.csv', index=False)
        
#MANILA DATA - UNIDENTIFIED       
output_Manila_unidentified = pandas.read_csv('Manila_unidentified.csv')
output_Manila_unidentified['Assailant'] = 'Unidentified'
output_Manila_unidentified.to_csv('Manila_unidentified.csv', index=False)


