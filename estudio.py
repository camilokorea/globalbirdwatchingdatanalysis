import pyodbc
import os
import pandas as pd

# DEFINITIONS
size = os.get_terminal_size()
countriesList = []
countriesInLocList = []
countriesTuple = []
countriesSet = None
countriesDictionary = {}

# SQL QUERIES
sqls = {
    "countries": open('./SQL/countries.sql', 'r').read(),
    "countries_in_locs": open('./SQL/countries_in_locs.sql', 'r').read()
}

dbconn = {
    "username": "MERENDA_USER",
    "password": "b1aZ2bHtiar3Vmrw",
    "database": "MERENDADB",
    "host": "69.164.199.30"
}

# DATA BASE CONNECTION
conn = pyodbc.connect(
    'Driver={SQL Server Native Client 11.0};Server=' + dbconn['host'] + ';Database=' + dbconn['database'] + ';UID=' + dbconn['username'] + ';PWD=' + dbconn['password'])

# CURSORS
print('LOADING COUNTRIES IN DATA BASE')
cursorCountriesObject = conn.cursor()
cursorCountriesObject.execute(sqls['countries'])

# ITERATION IN RECORDSETS
for country in cursorCountriesObject:
    countriesList.append(country[0])
    countriesDictionary[country[0]] = country

print('LOADING COUNTRIES IN DATA BASE IN HOTSPOTS')
cursorObject = conn.cursor()
cursorObject.execute(sqls['countries_in_locs'])

for countryInLoc in cursorObject:
    countriesInLocList.append(countryInLoc[0])

# TUPLE CREATION
countriesTuple = tuple(countriesList)

# LIST OPERATIONS
print("LIST:\n")
print(countriesList)
print("\n")

print("Last Item:")
print(countriesList[-1])
print("\n")

print("From 20th to 30th elements:")
print(countriesList[19:29])
print("\n")

print("From beginning to N - 10:")
print(countriesList[:len(countriesList)-10])
print("\n")

print("Reverse it:")
reversedList = countriesList[::-1]
print(reversedList)
print("\n")

print("Extend list with reversed version of it:")
extendedCountriesList = countriesList + reversedList
print(extendedCountriesList)
print("\n")

print("Remove Costa Rica from the list:")
countriesList.pop(countriesList.index('CR'))
print(countriesList)
print("\n")

print("Add back Costa Rica to the list:")
countriesList.append('CR')
print(countriesList)
print("\n")

print("Sort the list:")
countriesList.sort()
print(countriesList)
print("\n")

print("*" * size[0])
print("\n" * 2)

# TUPLE OPERATIONS
print("TUPLE:\n")
print(countriesTuple)

print("Last Item:")
print(countriesTuple[-1])
print("\n")

print("From 20th to 30th elements:")
print(countriesTuple[19:29])
print("\n")

print("From beginning to N - 10:")
print(countriesTuple[:len(countriesTuple)-10])
print("\n")

print("Reverse it:")
reversedTuple = countriesTuple[::-1]
print(reversedTuple)
print("\n")

print("Extend tuple with reversed version of it:")
extendedCountriesTuple = tuple(list(countriesTuple) + list(reversedTuple))
print(extendedCountriesTuple)
print("\n")

print("Remove Costa Rica from the tuple:")
countriesListTuple = list(countriesTuple)
countriesListTuple.pop(countriesTuple.index('CR'))
countriesTuple = tuple(countriesListTuple)
print(countriesTuple)
print("\n")

print("Add back Costa Rica to the list:")
countriesListTuple.append('CR')
countriesTuple = tuple(countriesListTuple)
print(countriesTuple)
print("\n")

print("Sort the tuple:")
countriesListTuple = list(countriesTuple)
countriesListTuple.sort()
countriesTuple = tuple(countriesListTuple)
print(countriesTuple)
print("\n")

print("*" * size[0])
print("\n" * 2)

# SET OPERATIONS
print("SET:\n")
countriesSet = set(countriesList)
countriesInLocSet = set(countriesInLocList)
print("COUNTRY SETS")
print(countriesSet)
print("\n")
print("COUNTRY IN LOC SETS")
print(countriesInLocSet)
print("\n")

print("Last Item:")
print(max(countriesSet))
print(max(countriesInLocSet))
print("\n")

print("Number of items in sets:")
print(len(countriesSet))
print(len(countriesInLocSet))
print("\n")


print("Difference between country set and country_in_loc set")
differenceSet = countriesSet.difference(countriesInLocSet)
print(differenceSet)
print("\n")

print("Intersection between country set and country_in_loc set")
intersectionSet = countriesSet.intersection(countriesInLocSet)
print(intersectionSet)
print("\n")

print("IsDisJoint between country set and country_in_loc set")
isDisJointSet = countriesInLocSet.isdisjoint(countriesSet)
print(isDisJointSet)
print("\n")

print("countriesInLocSet is subset of countriesSet")
isSubSet = countriesSet.issubset(countriesInLocSet)
print(isSubSet)
print("\n")

print("countriesSet is subset of countriesInLocSet")
isSubSet = countriesInLocSet.issubset(countriesSet)
print(isSubSet)
print("\n")

print("countriesSet is superset of countriesInLocSet")
isSuperSet = countriesSet.issuperset(countriesInLocSet)
print(isSuperSet)
print("\n")

print("Symmetric_Difference between countriesSet and countriesInLocSet sets")
symmetricDifferenceSet = countriesSet.symmetric_difference(countriesInLocSet)
print(symmetricDifferenceSet)
print("\n")

print("Union between countriesSet and countriesInLocSet sets")
unionSet = countriesSet.union(countriesInLocSet)
print(unionSet)
print("\n")
print("Total of items in union of sets")
print(len(unionSet))
print("\n")

print("*" * size[0])
print("\n" * 2)

# DICTIONARY OPERATIONS
print("DICTIONARY:\n")
print(countriesDictionary)
print("\n")

print("Display Costa Rica Item:\n")
print(countriesDictionary['CR'])
print("\n")

print("Display Costa Rica Item using GET method:\n")
print(countriesDictionary.get('CR'))
print("\n")

print("Display dictionary keys:\n")
keys = countriesDictionary.keys()
print(keys)
print("\n")

print("Display dictionary values:\n")
values = countriesDictionary.values()
print(values)
print("\n")

print("*" * size[0])
print("\n" * 2)

# PANDAS DATAFRAME
print('PANDAS DATAFRAME')
table = pd.read_sql_query(sqls['countries'], conn)
print(table)
print(table.columns)
print(table.count)
print(table['ID'])
print(len(pd.unique(table['ID'])))

# CLOSE DATA BASE CONNECTION
cursorObject.close()
cursorCountriesObject.close()
conn.close()
