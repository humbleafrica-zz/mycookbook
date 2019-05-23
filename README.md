
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

The project idea is to match Artist (both Audio and Visual) to contribute to a project. We all like art in one form or another whether it’s music, drawing, architecture etc. Imagine your favourite music, it’s video choreographed by your favourite choreographer, it’s album cover designed by your favourite grafittist, artist or graphic designer. The above are all forms of art however there is no such community where these artist like each others work and submit a public appraisal to work with one another. The idea is fans can witness the requests but cannot interact with comments. They can only like with their social media accounts. This gives new talent a chance to blossom due to recognised artists picking their work. The signup will be free for artists, they can comment on other artists’ works as well as request to use other artists’ work in their work (observing copyright rules).

Artists can request for features to be added as well as top up earnings for a feature to rise to the top of most requested feature. At the same time artists can request for a bug fix.
## REASONING

It will qualify the following categories in the assignment brief

- Users can sign up to the site for free
- The can report bugs (ticket creation)
- They can also suggest features / updates (ticket creation)
- Issue Trackers (ticket tracker)
- Comment on tickets

    - *added extras - could be an about page (time dependant)*

### FEATURES

#### Sign Up and Artist Profiles

 - Sign up will include Art profiles where Art
 - Upload their work to be considered by other Art
 - Their work can be voted on by fellow Art

#### Bug Requests

 - Artist can also post bug resolution requests
 - All Art having the same issue can click on a tag to signal 
 the instance of the same issue

#### Feature Requests

 - Art can request a feature to be added to the page at a minimum cost of £3.
 - This can be voted on as well as funding topped up by other Art
 - The first feature request to cross the threshold of £250 will 
    trigger an immediate attention flag (moved to to-do list)

#### Issue Trackers

 - I intend to use charts and graphs visible to all users to track progress 
    of requests and bug updates

#### Developers

- Can mark tickets/ tasks as working on to move tickets into work in progress.

- [ ] An uncompleted task 
- [x] A completed task
- tasks will using traffic lighting system for the stages of development
- Pages will have a standard menu across the site. 
- A default homepage - Then extra menu options after login

### PAGES

All pages below are .html unless specified. They will be mixed withing the python django framework to allow secure transactions and no leak of code. The frame work will give resilliance to the page through the use of default built-in administrator, groups and user configurations

#### Login (login)

The login page will be pulled from the django framework default forms. This will be configured with the signup page to allow less time to configure user credentials

#### Signup (signup)

The signup page will be pull d from the django framework default forms as explained above. django deals with teh backend security whilst I concentrate on the troubleshooting.

Base Template (base)

The base template is the page that will hold the frame of each page. It will hld the footer, header, titles description etc. This approach allows the header and fooeter to be changed rapidly without affecting

the individual page contents. It is someting like builing an external HTML form template to insert into a PHP

#### Bugs (bugs)

The bugs page as the name suggests will be the page where the artists can report bugs with the application, their user area etc. It will carry properties of the base template above.

#### Features (features)

The features page will be where the artists request features to be added to the application, their user area etc. to be able to interact better with teir colleagues. It will also carry properties of the base template. The reason for this page is that each artist despite the commonalities to transmit a message in a category of art, within the same group, still have a unique style, and therefore may have customisation requests. Other users may want similar features with or without added extras.

#### Index (index)

The index page as we all know is the default users are referred to when they enter a traditional url of a website. The index of this project

will show the latest most viewed or listened uploaded work

#### About (about)

The about is self explanatory but will give an idea of what the focus of teh site is about this will be done if time permits because the project idea is a huge tasking

### TECHNOLOGY TO BE USED

The technologies to be used in this project are HTML, CSS via Bootstrap CDN, PythonDjango.

<a href="https://www.djangoproject.com/">*Django*</a> is to allow me to build a website in smaller feature chunks with little effort at a faster rate.

<a href="https://www.w3.org/html/">*HTML*</a> HTML will be used for the structuring of the pages view to users

<a href="https://getbootstrap.com/">*Bootstrap*</a> Bootstrap brings baout some more flexibily in terms of styling and at time structuring of HTML5 pages. bootstrap ensures the visaul scalability of the same page on mobiles, tablets, desktops and laptops

<a href="https://www.w3.org/Style/CSS/Overview.en.html">*CSS*</a> now known buy it’s most recent version CCS3 will be used to add an extra beautificatin strategy to the pages. Bootstrap offers many styles out of the box but just like the artists I am working for each page can be made unique with a simple change of colours, making the structure stand out with the different colours.

<a href="https://www.mozilla.org/en-GB/firefox/developer/">*Firefox Developers Edition*</a>  The Mozilla Firefox Developers Edition browser was used in the development of this project because it has firebug built-in for live debugging, editing, and monitoring of the website’s CSS, HTML, DOM, XHR, and JavaScript. This allowed easy troubleshooting.

### LIBRARIES

The following libraries will be used || link to libraries

bootstrap ccs || https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css

minified Jquery || https://code.jquery.com/jquery-3.3.1.slim.min.js

https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js

font awesome icons || https://fontawesome.com/icons?d=gallery

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

No Capability testing could be conducted on this project as it is incomplete. The IDE mostly flagged up issues with the code and wouldn’t run if the issue was severe. Most errors seemed to be 500 error but there was no further details being shown in the C9IDE

### BACK UP

#### GitHub

the main back up used for the project were on github The project commits on github are stored at the link below:

https://github.com/humbleafrica/artmatch

#### Hosting

An attempt to host the page on heroku caused and error. the link to the heroku hosting and git pages are below:

Host URL : https://artisth.herokuapp.com/

Heroku Git URL : https://git.heroku.com/artisth.git

### MEDIA

The photos used in this project were obtained from unsplash

Background Image : https://unsplash.com/photos/Y2dHx5H-zmk

#### Logo

https://logomakr.com/

The logo was created using four images from Unsplash using the keywords artist, video, music, and match

### CONCLUSION

The project idea is without a doubt phenomenal. The implementation could have been better researched in terms o fteh technology used. Inexperience with the chosen scripting language caused the project to not be 
completed. The same project could have been completed in PHP with much reasonable results.

I have not had a great exposure to Django. The exposure I’ve had from sonline tutorials listed in my support section shows its a versatile programming language however very confusing and requires experience to 
create projects of teh magnitude envisioned. Users will need several weeks of practice to become fully acquainted with the views, urls and models. I found the django framework useful in many ways but complicated 
compared to PHP and MySQL. I had to restart the project due to the view showing the same page over and over again in navigation. The error notifications were extremely unclear and unless you’ve encounted the challenge 
before it was another few hours of debugging researching and hair pulling (if you had any left). The python code sometimes wouldn’t work in C9 IDE but would work fine locally. In all it was hairy experience but a learning curve.

I have taken the possitive out of this and refined some of my PHP and limited the sourcecode for my website to 20% of the original content. In all I think Python and Django are great framework to work with however
developers used to developing iwth PHP will appreciate the easy to debug aspect of PHP. Nonetheless I will attempt some of teh project on teh django website to polish my django knowledge for my up coming projects. 

### ACKNOWLEDGEMENTS

Many thanks to Anthony @ prettyprinted for his help with django. I’ve managed to limit the file size of some of my websites by applying some of the skills learn in django on my PHP scripts.

Thank you to Neil McEwan for sending through the assignment brief to get me started on this project.
