# Best Hollywood Actors Flask App

## What I built

I created a web app using flask that enables users to search for Hollywood's best actors and find out information about their birthday, birthplace, best movie, worst movie, and data regarding the selected actor's top 10 filmography. The purpose of this app is to combine the most useful data from Rotten Tomatoes with the most useful data from IMDb so users don't have to visit multiple websites and go through several webpages to find Hollywood's best actors and their best movies.

The database contains a total of 300 actors. Data comes from IMDb and Rotten Tomatoes.

## How it was built (Scraper)

I began by first scraping all the information I needed for my web app from Rotten Tomatoes and IMDb. The file titled "scrape_bot1" is the code that was used to gather all the data I needed from both IMDb and Rotten Tomatoes.

My scraper first began by visiting an IMDb webpage that listed Hollywood's top 1000 actors. The code grabbed the url link (first 300) to each of the actor's individual IMDb webpage. The code then visited each webpage and recorded the actor's name and awards or nominations.

The scraper code then turned the names of each actor into a live Rotten Tomatoes url link. Example: "Robert De Niro" turned into ```"https://www.rottentomatoes.com/celebrity/robert_de_niro"```, or "Jack Nicholson" turned into ```"https://www.rottentomatoes.com/celebrity/jack_nicholson"```.

This url was then used by a selenium function in my code which visited each webpage for each actor on Rotten Tomatoes and recorded the actor's highest ranked movie, lowest ranked movie, birthdate and birth place. The scraper then collected the actor's top 10 best ranking movie urls and visited each of those movie webpages to collect the title, Tomato Meter score, audience score, release date, and director for each of those 10 movies.

All of the data was then written into a CSV file. Each CSV row contains one actor for a total of 56 data points for each row (6 data cells for the actor info and 50 data cells for the actor's top movies).

### Redundancy

The method I used to turn an actor's name into a Rotten Tomatoes url worked well but it was not fool-proof. Certain actors that had special characters in their name could not be successfully turned  into Rotten Tomatoes link and therefore could not be loaded by selenium automatically.
All the failed link were collected in a list to be fixed and run again.

The file 'scrape_bot2' is almost an exact copy of 'scrape_bot1'. The only difference is that in 'scrape_bot2' the Rotten Tomatoes urls for the failed actors were manually provided in a list instead of being automatically generated using the collected actor names. This was was run to collect the remaining actor data that could not be previously recorded.

## How it was built (App)

The web app was built using Flask. A total of three templates were used for three different webpages. A python function is used to turn the CSV file into a dictionary. That dictionary data is then used to feed the template. Bootstrap and wtforms were used for the search field on the home page. 
