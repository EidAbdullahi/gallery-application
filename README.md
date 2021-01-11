#Title
Eid_Gallery

#Description
gallery-application(Eid_Gallery) is a personal gallery application that displays my photos for other people to see 
just as one of the way of building social intelligence.! You can visit the live site on ''/

#Author
Eid Abdullahi

eidabdullahi1@gmail.com

#Features
As a user of the web application you will be able to: See all posted photos View photos by location See each photo’s description and location on hover.
Be able to copy a photo’s url to the clipboard Click on view image to expand a photo Search for a photo by category e.g. outdoor, photoshoot

#Specifications
Behavior	Input	Output
View all posted photos	Hover over a photo	Shown details about the photo
Details about the photo	Click on Copy Link	Pop up that shows that the image link has been copied appears
Details about the photo	Click on View Image	Photo expands
Search in the search field	Input keywords to be searched then press ENTER	Search page is loaded and displays with the searched results
Getting started
Prerequisites python3.6 virtual environment pip Cloning In your terminal:
$ git clone https://github.com/EidAbdullahi/gallery-application.git $ cd gallery-application

#Running the Application
Install virtual environment using $ python3.6 -m venv virtual Activate virtual environment using $ source virtual/bin/activate 
Download pip in our environment using $ curl https://bootstrap.pypa.io/get-pip.py | python Install all the dependencies 
from the requirements.txt file by running python3.6 pip install -r requirements.txt Create a database and edit the database configurations in settings.py 
to your own credentials. 
Make migrations $ python manage.py makemigrations photos $ python3.6 manage.py migrate To run the application,
in your terminal: $ python3.6 manage.py runserver

#Testing the Application
To run the tests for the class file: $ python3.6 manage.py test photos

#CODEBEAT
codebeat badge

#Technologies Used
Python3.8 Eid-Gallery is a personal gallery application that displays my photos for other people to see just as one of the way of building
social intelligence.! You can visit the live site on 'https://eid-gallery.herokuapp.com/'
Django HTML Bootstrap This application is developed using Python3.8.5, Django, HTML and Bootstrap

#Support and Team
Eid Abdullahi Slack Me! @eidabdullahi10

#LICENSE AND COPY RIGHT INFO.
MIT License

Copyright (c) 2021 Eid_Gallery.

