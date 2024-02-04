1) CrosswalksIntoTractsGeneralRaceHsg.py: Using the crosswalk data from 2010 (blockgroups) to 2020 Census tracts, the program reconstructs a geographic unit of 2010 data to the comparable unit of 2020 data and calculates the change in Census data from 2010 to 2020. 
2) householder/CrosswalkIntoTracts.py: Does the same as (1) but with renter and homeowner households by race. 
3) householder/fillhouseholderdata.py: Simply adds 2020 household data to the geojson file to make it easier to calculate the differences in (2) without needing to also open a CSV file to 2020 data, just 2010.
4) correlation_run_results/ : Results of statistical data analysis by various Bay Area geographies to determine significance in where homes are built and where racial groups change.
