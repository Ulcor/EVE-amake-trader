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
Asks all denizens their primary functions

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

#### Amake trader
1) Checks the market value of items
2) Your orders - check if first sale/buy

#### Hauler
1) Gets data from Amake trader and create the best trip value for hub 1->hub 2. Items, price_1 price_2 - tax * volume

### Coin keeper
1) Track money flow. Items value, wallet value
2Croston, Holt-Winters and similar models for forecasting/investing

----
## How to use the app:
Automate EvE time
