# INFO-664 Final Project Description

## Overview

This project examines data provided by the Columbia University School of Journalism's Stabile Center for Investigative Journalism.Compelled by the lack of available information on EJKs by the Philippine government, Stabile Center attempted to verify deaths under the anti-drug campaign and released their data and research as a downloadable Microsoft excel files for three cities, Manila, Caloocan, and Quezon City. This dataset contains information on 2,320 individuals killed in three municipalities in the capital in the first 18 months of the antidrug campaign. Their data examines twenty-three different sources across six different types of information sources (police records, Philippine Commission on Human Rights, independent journalists, international human rights organizations, etc.), covering the period of July 2016-2017.

## The Code
For this project, I downloaded the Microsoft excel files from https://github.com/HRDAG/PH-drug-related-killings/tree/master/import/input
I saved each tab of data from the excel file and saved them as a CSV file. From here, I imported all six CSV files and used python in order to manipulate the CSV files for import and use in visualization for Tableau. With the raw data, the first python file to run is "data_csvcolumn_export.py", which adds the column "assailant" in each of the six CSV files. This information is crucial for the analysis. This code rewrites 6 csv files to include the new "assailant" comumn. The second python file "data_mergingCSVs.py" merges my CSV files, such that each city's info is now in a single file.  It outputs is 3 new csvs, one per city. Once these are run, the CSVs are ready for input into Tableau.
