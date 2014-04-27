#Reduce the Noise#

This was created as a final project in my [TAM](http://tam.colorado.edu) capstone course. See the final product here: [reducenoise.herokuapp.com](http://reducenoise.herokuapp.com). This README serves more of a 'What I learned...' instead of a 'How-to'. With my source code and the resources below, you should be able to figure it out pretty quickly.

Project idea: Common media websites are too busy and the average news consumer doesn’t want to wade through all of the noise to get to the important stories. These Python scripts allow a news consumer to customize what news they want to receive from the news sites that matter to them.  By default it is setup to scrape the top story of the day from news sites that may be interesting to the average CU student: [CU Independent](http://www.cuindependent.com), [Boulder Daily Camera](http://www.dailycamera.com) and [The Denver Post](http://www.denverpost.com).

Then, a Django web application, deployed via [Heroku](http://www.heroku.com), displays the latest headlines in a blog-roll format, with the each day’s top stories at the top.

###The structure###

In broad strokes, here's how this project works, from start to finish.

My local machine runs a daily cron job and executes a python script that scrapes three media websites for the top stories of the day.

Those stories are then concatenated into a python dictionary that is written to a postgresql database courtesy Heroku.

Those stories, along with past top stories are written out online at [reducenoise.herokuapp.com](http://reducenoise.herokuapp.com) thanks to a Django application.

###My build story###

I knew zero Python before I started this project three weeks ago, but I did have some programming experience.

Building this started with my interest in web scrapers and hearing Django tossed around at a few conferences. I started with the scraper, because if that didn’t work, there would be no way to get the information in the first place.

As many projects do, I started the scraper with a Google search for python scraper tutorials. There were three that really allowed me to get familiar with the process.

1. [Scrape the Gibson: Python skills for data scrapers](http://brianabelson.com/open-news/2013/12/17/scrape-the-gibson.html)

2. [Python Recipe: Grab page, scrape table, download file - Palewire](http://palewi.re/posts/2008/04/20/python-recipe-grab-a-page-scrape-a-table-download-a-file/)

Getting the scraper to work taught me a lot about the syntax and requirments of python. Out of the box I learned about installing and importing various libraries. The print function became my friend real quick and I got familiar with python's data types. I wrote two or three different working versions of the scraper with different methods, trying to get as efficient as possible, but it's a long way from perfect.

The script uses requests to go out and get the HTML, BeautifulSoup in parsing the HTML and dataset for sqlite OR psycopg2 for postgres (I'll get to postgres later).

I used a dictionary to write into the sqlite db.

Once that wrote to a sqlite db properly I focused on getting familiar with Django. Here too, I started with online tutorials. The 'Netmag' tutorial was especially helpful in creating a blogroll from a sqlite db. These other resources were helpful as well:

1.[Netmag -- Get started with Django](http://www.creativebloq.com/netmag/get-started-django-7132932)

2. [Django basics - Installing Django and Setting up a project and app](http://mherman.org/blog/2012/12/30/django-basics/#.U106W61dWiq)

Working with Django I quickly learned about Model-View-Controller. I also quickly became familiar with designing using templates and Django's local server functionality.

I learned a lot about accessing db's form django, sqecifically writing my own models. Here, the inspectdb function was super helpful. This knowledge was extremely helpful later on when I was deploying.

###Connecting the two (locally)###

Once I had a Django app running locally on my machine I attempted connecting the two. Besides some model issues, this process was actually fairly easy. The biggest problem was passing in properly formatted slugs for django to use in the post url. It for loop to be able to catch every foreseeable character that may mess up a slug. Single and double quotes were especially painful.

After a few inspectdb's and reformatting the temlate HTML files, the scraper was able to write to the sqlite db that the Django app reads from. Locally speaking, all I had to do was set up a cron job to get it running. That's not something I had ever done before. I learned a lot about cron and Apple's launch control.

But it worked. Locally.

###Deployment###

Ugh... Coming from the HTML/CSS/JavaScript world, deploying Django to a server was a bit more tricky.

I knew that for my first project I didn't want to spin up/spend money on AWS. Since I had heard of Heroku and Google searches confirmed that it was pretty popular, I decided to try it out.

Throughout the process I learned that the two Django-specific tutorials for deploying with Heroku I found online weren't very helpful. One was too deep, the other was slightly outdated and neither fully explained what needed to happen, from my noob perspective.

One of my big hurdles was making the scraper and Django app work with postgres. It's a long story, but my computer had traces of postgres left over from previous projects and psycopg2 would not install properly. That whole thing probably took me six hours to figure out. I ended up having to remove every trace of postgres on my computer and brew install postgres from scratch. After that it started up ok and it was fairly simple getting a local postgres instance working.

Some of the sqlite/postgres syntax differences were a pain, but simple to fix. Specifically, setting published to 'true' in postgres but '1' in sqlite.

With the help of both Heroku tutorials and Django's debug feature, I was able to spin up a Heroku app. There were A LOT of errors because I mis-labeled my Procfile or put in the wrong version number in requirements.txt. Once I fixed the error messages the instance worked. 

But I had to get my data on the Heroku postgres.

Once I found the connection info on the Heroku db writing to it from my box was easy enough. Same with writing to it from the scraper and reading from it from Django.

Then, voila! Three weeks of hard work paid off. Actually, funny story, I got it to work at the exact moment the Colorado Avalanche scored a goal to win in OT over the Minnesota Wild in the playoffs. So that was cool.

Anyway, if you would like more information regarding how I did anything, feel free to contact me at robert [dot] denton9 [at] gmail [dot] com.

###License###
See LICENSE.md but take what you want, attribute what you can.