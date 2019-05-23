
# The Recipe Diary Milestone Project

## Project Requirements

In this project I’ll be building a web application using the django python framework for called The Recipe Diary (TRD). The assignment briefing for the project is shown below :

Create a web application that allows users to store and easily access cooking recipes
Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data
Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course)
Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation
Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large
Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions
Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages
Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure)

## PROJECT THESIS

This project takes a guidance from the project requirements 

## REASONING

It will qualify the following categories in the assignment brief

- Add, delete and edit recipes
- like or favorite recipes
- create django models to fit the scenario
- add user registration

- *added extras - could be an about page (time dependant)*

### FEATURES

#### Add, Delete and Edit Recipes

the app has been created in such that users will have to sign up to be able to add, delete or edit recipes. There wasn't a means I could find that allow users to sign up without a password to login.


### PAGES

There are 11 pages all together. The menu shows 4 menu tabs with the logo on the left and the on the right is the option to sign in or sign out depeneding on whether the user is signed in or out.

Most of the pages auto populate the category selected and and lists them in a bootsrap table, except the detail page which shows more details of the chosen recipe. with the options to cook, delete, add or edit a recipe. The cook option expands and 
shows the cooking method and time taken.

#### Login (login)

Users are able to login with a chosen username and password

#### Signup (signup)

Users are able signup with an email address, username and password


#### Index (index)


### TECHNOLOGY TO BE USED

The technologiesused in this project are HTML, CSS via Bootstrap CDN, PythonDjango.

<a href="https://www.djangoproject.com/">*Django*</a> is to allow me to build a website in smaller feature chunks with little effort at a faster rate.

<a href="https://www.w3.org/html/">*HTML*</a> HTML will be used for the structuring of the pages view to users

<a href="https://getbootstrap.com/">*Bootstrap*</a> Bootstrap brings about some more flexibily in terms of styling and at time structuring of HTML5 pages. bootstrap ensures the visaul scalability of the same page on mobiles, tablets, desktops and laptops

<a href="https://www.w3.org/Style/CSS/Overview.en.html">*CSS*</a> now known buy it’s most recent version CCS3 will be used to add an extra beautificatin strategy to the pages. Bootstrap offers many styles out of the box but just like the artists I am working for each page can be made unique with a simple change of colours, making the structure stand out with the different colours.

<a href="https://www.mozilla.org/en-GB/firefox/developer/">*Firefox Developers Edition*</a>  The Mozilla Firefox Developers Edition browser was used in the development of this project because it has firebug built-in for live debugging, editing, and monitoring of the website’s CSS, HTML, DOM, XHR, and JavaScript. This allowed easy troubleshooting.

### LIBRARIES

The following libraries were used || links to libraries

bootstrap ccs || https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css

minified Jquery || https://code.jquery.com/jquery-3.3.1.slim.min.js

https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js

font awesome icons || https://fontawesome.com/icons?d=gallery

Free Code Camp || https://www.codingforentrepreneurs.com/

### SUPPORT NETWORKS

I have relied heavily on the following networks in this project

- Stackoverflow

- Code Institutes Slack Environment

- Youtube Channels (Pretty Printed, Isaac Grey)

- https://tutorial.djangogirls.org/en/

- https://logomakr.com/

### TESTING

Device Compatibility Testing

This test was conducted using firefox developers edition browser is has built in rendering of pages on different smartphone devices, tablets, Laptops, PCs and TV sets for the frontend.
Capability Testing

The tests conducted were mostly front. The debugger was relied for the most part of debuging errors. At first it was a mine field but after some time of breaking and fixing I learnt the hard way with what to do and what not to do.
The advantage is that I got the hang of working on github and backing up the code I hade written.

### BACK UP

#### GitHub

the main back up used for the project were on github The project commits on github are stored at the link below:

https://github.com/humbleafrica/tcookbook and https://github.com/humbleafrica/thecookbook. thecookbook was the initial project, I broke it a number of times and had to clone, delete and rebuild.

#### Hosting

The app hosting would build succesfully after removing more than half the packages in the requirements list for heroku but the app never run succesfully.

There were two packages that raised errors during debuging and they were egg_info and DistUitils. After the cloning and managing to get it runnning in cloud9 the AWS boto3 storage package was showing errors when the 'collectstatic' command was run.

Below is the link to the app. It always displayed application error on upload but run fine on c9.

https://tcookbook.herokuapp.com/


### MEDIA

The photos used in this project were obtained from unsplash

Background Image : https://unsplash.com/photos/Y2dHx5H-zmk

#### Logo

https://logomakr.com/

The logo was created using  images from Unsplash using the keywords in the project requirements

### CONCLUSION

I really enjoyed this project despite the many painful breaking scenarios of yes yes yes and oh **** . It gave me a better understanding of the djnago framework python coming from a php and css background. I have lots to add to the next project. I like the templating aspected of django to keep all pages uniform. It reminded me of PHP a littleand made me improve some
of teh PHP codes i have written in the past. I also applied some things i've done with PHP. No one can possibly master any programming language but I think having a good understanding of django will eliminate some database woes chasing a career in fullstack. 
I will be making some side projects toimprove my django knowledge.

some commands wouldn't work for uploading to heroku but worked fine locally. The experience has been an eye opener to a new worl of possibilities


### ACKNOWLEDGEMENTS

Many thanks to Anthony @prettyprinted for his help with django. I’ve managed to limit the file size of some of my websites by applying some of the skills learnt in django on  PHP scripts.

Thank you to Neil McEwan for sending through the assignment briefs and also regular responses to my querries durring the debug .
