## Description

Context
Space Apps Moscow was held on April 29th & 30th. 
Thank you to the 175 people who joined the International Space Apps Challenge at this location!

## Content
The dataset contains such columns as: "wind direction", "wind speed", "humidity" and temperature.
The response parameter that is to be predicted is: "Solar_radiation".
It contains measurements for the past 4 months and you have to predict the level of solar radiation.
Just imagine that you've got solar energy batteries and you want to know will it be reasonable to use them in future?


## Inspiration
Predict the level of solar radiation.
Here are some intersecting dependences that i have figured out:
Humidity & Solarradiation. 2.Temeperature & Solarradiation.
The best result of accuracy I could get using cross-validation was only 55%.


## About this file
These datasets are meteorological data from the HI-SEAS weather station from four months (September through December 2016) between Mission IV and Mission V.
For each dataset, the fields are:
A row number (1-n) useful in sorting this export's results
The UNIX time_t date (seconds since Jan 1, 1970). Useful in sorting this export's results with other export's results
The date in yyyy-mm-dd format
The local time of day in hh:mm:ss 24-hour format
The numeric data, if any (may be an empty string)
The text data, if any (may be an empty string)
The units of each dataset are:
Solar radiation: watts per meter^2
Temperature: degrees Fahrenheit
Humidity: percent
Barometric pressure: Hg
Wind direction: degrees
Wind speed: miles per hour
Sunrise/sunset: Hawaii time
## Link of the project:
https://solar-radiation-prediction.herokuapp.com/
I pushed the project on Heroku service