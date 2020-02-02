Small program for getting SpaceX stats about launches per year. 

Usage: run main.py from Python IDE or using cmd: 
python main.py 

Expected result:
 - two CSV files generated:
   - One with success/failure launches stats per years (SpaceX_stats.csv),
   - Second with SpaceX stats per flight number - it shows status (Success/Failure) per flight number (SpaceX_stats_per_flight_number.csv).
 - bar plot generated, based on launches stats per years.
 
 Requirements:
 - Python 3.7 (or newest) with following packages:
    - requests,
    - collections,
    - datetime,
    - matplotlib.
  