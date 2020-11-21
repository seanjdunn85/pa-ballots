# PA Mail in Ballots
This repo requires the following to operate:
* python 2.x
* pip 
* MySQL

Steps:
Download the Ballot data in .csv format. ASAIK this is the correct link:

https://data.pa.gov/Government-Efficiency-Citizen-Engagement/2020-Primary-Election-Mail-Ballot-Requests-Departm/853w-ecfz

In the root directory, run: 

`pip install -r requirements.txt`

Save `example.env` as `.env` nad set each SQL connection variable to those of you database.

run `python init.py`