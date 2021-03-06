![header](Resources/header.jpg)

# *Overview*

This project consists on performing database analysis for climate data using SQLAlchemy. After performing a series of complex queries data analysis is performed on the results

# *Application Breakdown*
- The application uses SQLAlchemy to perform a series of queries to a SQLlite database
- After the queries it performs some Data Analysis, all queries and analysis are contained in the [climate_starter.ipynb](climate_starter.ipynb) jupyter notebook
![temp_frequency](Resources/temp_freq.jpg)
- [app.py](app.py) contains a Flask script that while running creates an API with several endpoints to obtain data from the database. All results are returned as json files
- [temp_analysis_bonus_1_starter.ipynb](temp_analysis_bonus_1_starter.ipynb) contains calculations focused on measurement stations
- [temp_analysis_bonus_2_starter.ipynb](temp_analysis_bonus_2_starter.ipynb) contains normal temperature calculations for a given date range
![normal_temp](Resources/normal_temp.jpg)

# *Repository structure*
````bash
│   .gitignore
│   app.py
│   climate_starter.ipynb
│   commits.md
│   hawaii.sqlite
│   LICENSE
│   README.md
│   temp_analysis_bonus_1_starter.ipynb
│   temp_analysis_bonus_2_starter.ipynb
│
└───Resources
        hawaii.sqlite
        hawaii_measurements.csv
        hawaii_stations.csv
        header.jpg
        normal_temp.jpg
        temp_freq.jpg
````



# *Task List*
## Step 1 - Climate Analysis and Exploration
### Preparation
- [X] Use SQLAlchemy create_engine to connect to your sqlite database.
- [X] Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.
- [X] Link Python to the database by creating an SQLAlchemy session.

### Precipitation Analysis
- [X] Start by finding the most recent date in the data set.
- [X] Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data.
- [X] Select only the date and prcp values.
- [X] Load the query results into a Pandas DataFrame and set the index to the date column.
- [X] Sort the DataFrame values by date.
- [X] Plot the results using the DataFrame plot method.
- [X] Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis
- [X] Design a query to calculate the total number of stations in the dataset.
- [X] Design a query to find the most active stations (i.e. which stations have the most rows?).
- [X] List the stations and observation counts in descending order.
- [X] Which station id has the highest number of observations?
- [X] Using the most active station id, calculate the lowest, highest, and average temperature.
- [X] Design a query to retrieve the last 12 months of temperature observation data (TOBS).
- [X] Filter by the station with the highest number of observations.
- [X] Query the last 12 months of temperature observation data for this station.
- [X] Plot the results as a histogram with bins=12.

## Step 2 - Climate App
- [X] Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.
- [X] Use Flask to create your routes.
- [X] Routes
    - /
        - Home page.
        - List all routes that are available.
    - /api/v1.0/precipitation
        - Convert the query results to a dictionary using date as the key and prcp as the value.
        - Return the JSON representation of your dictionary.
    - /api/v1.0/stations
        - Return a JSON list of stations from the dataset.
    - /api/v1.0/tobs
        - Query the dates and temperature observations of the most active station for the last year of data.
        - Return a JSON list of temperature observations (TOBS) for the previous year.
    - /api/v1.0/<start> and /api/v1.0/<start>/<end>
        - Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
        - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
        - When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

## Temperature Analysis I
- [X] Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
- [X] Convert the date column format from string to datetime.
- [X] Set the date column as the DataFrame index
- [X] Drop the date column
- [X] Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
- [X] Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

## Temperature Analysis II
- You are looking to take a trip from August first to August seventh of this year, but are worried that the weather will be less than ideal. Using historical data in the dataset find out what the temperature has previously looked like.
- The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.
- [X] Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year (i.e., use "2017-08-01").
- [X] Plot the min, avg, and max temperature from your previous query as a bar chart.
- [X] Use "Trip Avg Temp" as the title.
- [X] Use the average temperature as the bar height (y value).
- [X] Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).
- [X] Daily Rainfall Average
    - Now that you have an idea of the temperature lets check to see what the rainfall has been, you don't want a when it rains the whole time!
    - Calculate the rainfall per weather station using the previous year's matching dates.
    - Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.
- [X] Daily Temperature Normals
    - Calculate the daily normals for the duration of your trip. Normals are the averages for the min, avg, and max temperatures. You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic TOBS that match that date string.
    - Set the start and end date of the trip.
    - Use the date to create a range of dates.
    - Strip off the year and save a list of strings in the format %m-%d.
    - Use the daily_normals function to calculate the normals for each date string and append the results to a list called normals.
    - Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
    - Use Pandas to plot an area plot (stacked=False) for the daily normals.
