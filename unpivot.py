#
# Unpivot and merge birth_rate_per1000_population.csv  and  infant_mortality_per1000_births.csv
#
# target format:
# CountryName1, year1, mortality, birthrate
# CountryName1, year2, mortality, birthrate
# CountryName1, yearN, mortality, birthrate
# CountryName2, year1, mortality, birthrate ... etc

import csv

csv_file = "total_population_with_projections.csv"
country_list = []

# Open csv file
with open(csv_file, 'r', encoding = "ISO-8859-1") as csvf:
    csvreader = csv.reader(csvf)
    csv_list = list(csvreader)

if len(csv_list) > 0 :
    yrlist = csv_list[0]
    #print(byrlist)
else:
    print("CSV file empty!. Quitting")    
    quit()


#
# Create list of countries from both sheets
#
countrylist = []

for line in csv_list[1:]:
    countrylist.append(line[0])
    
print("Country,Year,Population")
country_index = 0

for country in countrylist:
    country_index = countrylist.index(country)
    #
    # If country exists 
    #
    if (country_index >= 0 ):
        #
        #Iterate through the list of years
        #
        for cyear in yrlist[1:]:
            #print(country + " ," + str(cyear))
            #index of year in birthrate
            yr_index = yrlist.index(cyear)

            #print (country + " ," + str(cyear) + " ," + str(byr_index)  + " ," + str(myr_index))    
            # if cyear present
            if(yr_index > 0 ):
                bdata = csv_list[country_index+1][yr_index]
            
                print(country + "," + str(cyear) + "," + str(bdata).replace(',','' ))
    
        

