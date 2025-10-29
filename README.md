# eve-market-planner
Get best deals between stations and added value for industry in EvE online game

----
## Step 1
Create new app here:

https://developers.eveonline.com/applications/create

Finish esi.py with new app creds

----
## App logic

##### Town hall
1) Asks all denizens their primary functions 
2) Daily, weekly 
3) Connect different denizens between them

##### Peasant
Checks planetary industry <br>
Planet type, then:
1) Time left for a character-> planet-> extractor
2) Time left for a character-> planet-> T1 components volume
3) Projected output vs real output

#### Blacksmith
Checks jobs:
1) Industry. Available materials, runs
2) Science. Cores, runs
3) Chem. Station availability! Materials, logistics, jobs
4) WTB list - for items and cores

#### Trader
1) Checks the market value of items
2) Your orders - check if first sale/buy 
3) Croston, Holt-Winters and similar models for forecasting/investing

#### Hauler
1) Gets data from Amake trader and create the best trip value for hub 1->hub 2. Items, price_1 price_2 - tax * volume

#### Coin keeper
1) Track money flow. Items value, wallet value
2) All income vs spending
3) PLEX goals

#### Scribe
1) Write denizens activity into a database (free tier but with backup)
2) Select data from database on request from denizens

----
## How to use the app:
Automate EvE time
