# accessibilityMiner
Main goal is to shed light on the part of the web that is still inaccessible to a set of users that often get ignored by the mainstream, users with disabilities. To do this, the code looks for accessibility errors in the highly used websites today, and checks if the number and type of error have a relationship with the type of industry. 
###  `/src/main.py`
Entry point. Scrapes the urls from a URL database and travels to each of the urls to get the meta information (keywords and description) then feeds the info into the datumbos API to get a topic classification to classify the urls topic. It also uses the accessibility checker found in achecker.py to retrieve the accessibility errors found in the URL.
###  `/src/model.py`
Uses a mongodb dataset to create a machine learning model. This is somewhat redundant as I added the DatumBox API , but left it in place for future needs that DatumBox would not provide.

###  `/src/achecker.py`
Accessibility checker. Checks a url for accessibility issues and returns the number and type of errors.
