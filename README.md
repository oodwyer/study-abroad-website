# Penn-Study-Abroad
A web-app for students to share information and recommendations about popular study abroad locations. 

## Running the program
Navigate to the root directory of the project

`pip install whoosh django-haystack`

Run `python manage.py runserver` in the command line

## Requirements 
__Class definition:__ **Place** is the model for the study abroad locations on the website. It has the magic method __ge__, which is a used to compare two locations so that they can be sorted in alphabetical order, and the magic method __str__ for easier use of the database. 

__First-Party Packages:__ The package **os** was used to join paths in order to access the Whoosh directory and the package **datetime** was used for organizing dates in the haystack search index

__Third-Party Packages:__ **Django** was used for web development and **Whoosh** was used for the search engine. 
