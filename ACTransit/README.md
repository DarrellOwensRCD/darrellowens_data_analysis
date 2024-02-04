1) CreateMultipleACTLineFiles.py: Makes individual geojson files for every AC Transit line with routes and shapes so they can be toggled individually
2) MakeARecipeWithACTLines: Uploads each individual AC Transit geojson to a recipe system for the Mapbox Tiling Service when sending files via POST request
3) RemoveRepetitiveACTLines.py: Self-explanatory. Data cleaning.
4) realtimetracker.py: Testing the GTFS feed
