#
# Unpivot and merge birth_rate_per1000_population.csv  and  infant_mortality_per1000_births.csv
#
# target format:
# CountryName1, year1, mortality, birthrate
# CountryName1, year2, mortality, birthrate
# CountryName1, yearN, mortality, birthrate
# CountryName2, year1, mortality, birthrate ... etc

import csv

birthrate_file = "birth_rate_per1000_population.csv"
mortality_file = "infant_mortality_per1000_births.csv"
country_list = []

# Open Birth rate file
with open(birthrate_file, 'r', encoding = "ISO-8859-1") as brf:
    brfreader = csv.reader(brf)
    brf_list = list(brfreader)

if len(brf_list) > 0 :
    byrlist = brf_list[0]
    #print(byrlist)
else:
    print("Birth rate file empty!. Quitting")    
    quit()

# Open Mortality rate file
with open(mortality_file, 'r', encoding = "ISO-8859-1") as mrf:
    mrfreader = csv.reader(mrf)
    mrf_list = list(mrfreader)

if len(mrf_list) > 0 :
    myrlist = mrf_list[0]
    #print(myrlist)
else:
    print("Mortality rate file empty!. Quitting")    
    quit()

#
# Create list of countries from both sheets
#
brf_countrylist = []
mrf_countrylist = []

for line in brf_list[1:]:
    brf_countrylist.append(line[0])
    
for line in mrf_list[1:]:
    mrf_countrylist.append(line[0])

print("Country,Year,BirthRatePer1000Population,MortalityRatePer1000Births")
brf_country_index = 0
mrf_country_index = -1
for country in brf_countrylist:
    brf_country_index = brf_countrylist.index(country)
    if (country in mrf_countrylist):
        mrf_country_index = mrf_countrylist.index(country)
    else:
        mrf_country_index = -1
    #
    # If country exists in both sheets
    #
    if (mrf_country_index >= 0 and brf_country_index >= 0):
        #
        #Iterate through the list of years
        #
        for cyear in byrlist[1:]:
            #print(country + " ," + str(cyear))
            #index of year in birthrate
            byr_index = byrlist.index(cyear)
            #index of year in mortalityrate 
            if(cyear in myrlist):
                myr_index = myrlist.index(cyear)
            else:
                myr_index = -1
            #print (country + " ," + str(cyear) + " ," + str(byr_index)  + " ," + str(myr_index))    
            # if both sheets have the cyear,
            if(byr_index > 0 and myr_index > 0):
                bdata = brf_list[brf_country_index+1][byr_index]
                mdata = mrf_list[mrf_country_index+1][myr_index]
            
                print(country + "," + str(cyear) + "," + str(bdata) + "," + str(mdata))
    
        
#print(final_list)
