
#This code merges my CSV files, such that each city's info is now in a single file.
#Output is 3 new csvs, one per city.




import os
import glob
import pandas 
os.chdir("/home/brp/Desktop/664_ClassCode/INFO-664_FinalProject")

extension = 'csv'

#CALOOCAN
all_filenames_caloocan = [i for i in glob.glob('Caloocan_*.{}'.format(extension))]

caloocan_csv = pandas.concat([pandas.read_csv(f) for f in all_filenames_caloocan])

caloocan_csv.to_csv("caloocan_complete.csv", index=False, encoding='utf-8-sig')

output_caloocan = pandas.read_csv('caloocan_complete.csv')
print(output_caloocan)

#QUEZON CITY
all_filenames_quezoncity = [i for i in glob.glob('QuezonCity_*.{}'.format(extension))]

quezoncity_csv = pandas.concat([pandas.read_csv(f) for f in all_filenames_quezoncity])

quezoncity_csv.to_csv("quezoncity_complete.csv", index=False, encoding='utf-8-sig')

output_quezoncity = pandas.read_csv('quezoncity_complete.csv')
print(output_quezoncity)

#MANILA
all_filenames_manila = [i for i in glob.glob('Manila_*.{}'.format(extension))]

manila_csv = pandas.concat([pandas.read_csv(f) for f in all_filenames_manila])

manila_csv.to_csv("manila_complete.csv", index=False, encoding='utf-8-sig')

output_manila = pandas.read_csv('manila_complete.csv')
print(output_manila)