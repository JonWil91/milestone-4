Full Stack Milestone Project 4 - Code Institute

# JW Photography 

This is my fourth Milestone project of the Full Stack Frameworks with Django module from Code Institute. This project was designed to demonstrate all the knowledge and skills I have developed throughout the Code Institute Fullstack Web Developer course. This project will pull together the HTMl, CSS, JavaScript and Python skills learnt in previous modules and add using Django 3 to develop an e-commerce website.

## Project Purpose

The primary purpose of this project is to allow a user to navigate across the different pages within a visually appealing and user friendly website and purchase photo products. The products displayed on the site are photos I have taken in various countries whilst travelling and they provide a good range of photo types that would be able to appeal to a broad user base. This pulls together all skills that have been learnt throughout the Code Insitute course. The project is an e-commerce website that has the purpose of displaying products for the user to browse, add to a shopping cart and purchase. In addition to this were two custom models for the project which were used in the blog section where users can add comments to a blog and use the contact page to send a message to the Superuser admin panel.

This website would provide value to a user as it provides a number of different style photos available to purchase and enjoy. There is also a blog section to learn a little bit more about the website owners and about certain photos.

## Table of Contents

* [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Colour Scheme**](#colour-scheme)
    - [**Wireframes**](#wireframes)
* [**Features**](#features)
    - [**Additional Features to be Implemented**](#additional-features-to-be-implemented)
* [**Technologies Used**](#technologies-used)
* [**Testing**](#testing)
    - [**Code Validation**](#code-validation)
    - [**Compatability**](#compatability)
* [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)
* [**Credits**](#credits)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

## UX

The user is able to peruse all available products in the gallery page, this could be achieved by viewing all products as initially displayed, filerting by price/rating/category, or selecting the a specific category of interest. This allows the user to filter the products in a broad sense or to narrow down the field to a particular type of product. A user has the ability to register as a user, or login if a previous account has been created, and then add items to a bag and  proceed to checkout to make the purchase.

User's also have the ability to use the contact page to send a message to the admin panel, or to view the blog page to read, comment and like various blog posts, as long as they are logged in.

## User stories:

As a user on a mobile/tablet or desktop device I would:

* Want to have a clear idea of the website purpose after visiting the home page
* Want to click the Blog link in the navbar and visit the blog page
* Want to click the Gallery button in the navbar and visit the Gallery page
* Want to click the user Account button in the navbar and have an option
to view the user account if signed in or sign out
* Want the user Account button to provide an option to sign in or register as a new user if one has not already been created
* Want the user profile button to take me to a user profile page
* Want the sign out button to give me the option to sign out as a user


* Want the blog page to have blogs laid out in a clear structure and to span
multiple pages if needed
* Want to click individual blogs and view their content
* Want to be able to comment or like individual blog posts and have the 
input displayed clearly and added to the post


* Want the Gallery page to have all existing products displayed in a clear format
* Want the All Products dropdown button to give an option to filter the total range of 
products by price/category/rating
* Want to be able to view a set of products by category by clicking each individual
category link
* Want to be able to click each product for additional details
* Want the product details page to have a larger image, the location link
to show in a separate page the location of the image on Google Maps, to be able to 
choose a size or quantity of the product, to view the product with different coloured
frames and finally to be able to add the product to a shopping cart


* Want the contact page to have a clear and simple form to fill in
* Want the contact form to confirm that the message has been submitted and received
via a responsive message


* Want to be able to update personal information on the user profile page
* Want updated personal information to be reflected in the checkout page
* Want to be able to update quantity/remove products from shopping cart
* Want the secure checkout button on the shopping cart to direct to a checkout page
* Want the checkout page to give a clear form to fill in before making a purchase
* Want a clear confirmation that the order has been received upon completing an order

As a site owner I:

* Want to be able to add blog posts to the site from within the Account button
* Want to be able to edit/delete blog posts from either the main blog page or from individual blog posts
* Want to be able to edit/delete blog posts from either the main blog page or from individual blog posts

## Colour Scheme



### Wireframes

I decided to use handrawn wireframes for this project, as there is a lot on features on certain pages which would be easier to reflect by hand. For the most part the wireframes match up with the final product, with the exception of the introduction to pagination and an alteration to the product details pages, which were introduced during the production process.

## Features

The 'CRUD' operations are featured throughout the website as it is possible for Superusers to create, read, update and delete product and blog data. The app also uses Django's register/login/logout feature for ease of use in creating new profiles.


### Existing Features:

* **Navbar** - On all devices the navbar has a brand logo in the top left hand corner which takes the user to the home page. The navigational links are contained within a burger menu on tablet and mobile devices in the top right hand corner. Rather than these links dropping down in a vertial list as is the norm, on tablet the 6 navigational links are displayed in a row, and on mobile they are displayed as two rows of three as this looks clear and appealing for the user. There is a search bar which is used to search for names or descriptions of products in the Gallery page. This search bar is displayed next to the brand logo on desktop, and on tablet and mobile is displayed central and below the brand logo and burger menu. There is also a link to the user's cart, which is presented with a cart logo and a number demonstrating the current value added to the cart, starting at £0.00.
-- The Account button in the navbar will display differently depending on the user's log in status. If a user is not logged in the Account button will drop down to provide the user the option to regiser or log in. If a user is logged in, the Account button will change from 'Account' to the user's username. The button will also dropdown with an option to view their profile or log out. If a Superuser is logged in, the Account dropdown will also include Product Management and Blog management, in which new products or blog posts can be added to the site.

* **Messages** - When a user makes various actions, or actions fail to execute a message appears at the top right corner of the screen.

* **Register** - When a user clicks the Account dropdown and selects register, they are presented with a form to fill out. They have to fill in their email address two separate times, ensuring they match, a username, and a password twice, again ensuring they match.

* **Log in** - When the user clicks the Account dropdown and selects log in, they have to fill in a form with a recognised username and associated password.

* **Log out** - When a user is already logged in and clicks the Account dropdown link, they can click sign out, and then have to confirm this action on a new page.

* **Blog Comments** - On each individual blog post, provided a user is logged in they are able to add a comment. Clicking the add comment button takes them to a form on a separate page, and then after filling in a comment and submitting it they are redirected to the post with the comment below. 
-- If a user is not logged in and tries to add a comment they are directed to the log in page, as a user needs to be logged in for this feature. Once a user has added a comment, their comment will be displayed with an option to delete the comment. This only appears next to comments created by that user.

* **Blog Likes** - On each individual blog post, provided a user is logged in they are able to like it by clicking the like button. This will change the blue 'like' button to a red 'unlike' button if they wish to reverse this decision. Each additional is displayed as a total number next to the like button.
-- If a user is not logged in and tries to add a comment they are directed to the log in page, as a user needs to be logged in for this feature.

* **Pagination** - The Blogs page uses a pagination feature, only displaying 4 blog posts on a single page. If there are additional blog posts a next button is available to click. After clicking the next button, there is then an option to click previous to return to the previous page, or next again if there are additional pages. In the middle of the next and previous buttons is a box highlighting how many pages there are in total and what page number the user is on.

* **Superuser** - If a user is logged in as a Superuser they will have a different display to regular users. On the Account button they have access to the Product and Blog Management pages. They also have access to the CRUD operations on the blog, blog details, gallery and gallery details pages to update and delete blog posts or products from the store.

* **Contact**  - The contact page has a simple contact form, the user is required to fill in each field. Once submitted the user is redirected to the home page, a confirmation message appears in the top corner of the screen. This message is then saved in the admin panel.

* **Gallery**: - All Products - On the gallery page there is a All Products dropdown link which gives the user to filter the total number of products by price/rating or category
            - On the gallery page there is a link for each category which once selected displays products solely from the category selected.

* **Frame Colour** - A simple frame colour selector on the product details page allows the user to see what the selected photo product would look like with different coloured frames

### Additional features to be implemented:

* I would like to enable the search bar in the navbar to search for data in the blog page as well as the products page
* I would like to add a functional email system in which the user receives an actual email confirmation after registering
* I would like to add a functional email system where a buisness email could receive emails submitted from the contact form

## Technologies Used

* [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the content and basic elements displayed on the page
* [CSS](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
    - The project uses **CSS** to apply custom styles and colours to the content
* [Python](https://www.python.org/)
    - The project uses **Python** as the back-end programming language
* [Django](https://www.djangoproject.com/)
    - The project uses **Django** in association with Python as a web framework
* [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating the Python and Django code into the HTML files
* [Stripe API](https://stripe.com/gb)
    - The project uses **Stripe** to make secure payments
* [SQlite](https://www.sqlite.org/index.html)
    - The project uses **SQlite** as a database to hold the backend information from the models used within the Python files
* [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** for it's responsive, mobile-first approach to front-end web development. It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components. 
* [JQuery](https://jquery.com)
    - The project uses **JQuery** as the primary JavaScript functionality and to simplify DOM manipulation.
* [Google Fonts](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text throughout the site
* [Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome** to provide various icons throughout the site
* [GitPod](https://www.gitpod.io)
    - The project uses **GitPod** as the IDE for development which can be launched from any GitHub page
* [GitHub](https://github.com/)
    - The project uses **GitHub** as a remote repository to push each meaningful change to
* [Git](https://git-scm.com/)
    - The project uses **Git** as version control
* [Heroku](https://dashboard.heroku.com/apps)
    - The project uses **Heroku** as the hosting platform

## Testing

All of the testing for this project was done manually, however online validators were used to check the code used. These will be detailed below under the Code Validation heading. Testing always focussed on ensuring that the User Stories were being adhered to, that the website is responsive across all desktop, tablet and mobile devices and that the develoment was following the guidance of the wireframes where appropriate.

* Navbar - Each link from the navbar has been tested extensively across all devices to ensure each page loads regardless of which page it is being directed from. This has been done as a superuser, logged in user and a user who is not signed in.

* Search Bar - The search bar is situated next to the brand logo on desktop devices, and on tablet and mobile it is central on a row beneath the brand logo and the burger menu dropdown icon. The search bar is used to find any associated words on the Gallery page for product name or product descriptions. This feature works correctly.

* Product / Blog Management - When a Superuser is logged in, the Account dropdown link allows the user to add a Product or Blog to the site. This has been tested and confirmed that each field of the form functions correctly.

## Code Validation

* I used the W3C HTML Validator tool to validate my HTML code. The W3C Validator tool doesn't recognise the Jinja templating, which resulted in it showing a lot of errors in relation to the Jinja code. This meant carefully going through such html files to ensure that they were formatted correctly.
* I used the W3C CSS Validator tool to validate my CSS code.
* I used the JSHint tool to validate my JavaScript syntax.
* I used the Pep8 Online tool to validate my Python syntax. Had to update a number of lines that were too long and blank spaces I had initially missed.

## Compatability

To ensure that the website is accessible and runs across different devices and browsers, I have tested it on the following:

* Chrome
* Safari
* Firefox
* Opera
* Microsoft Edge

## Deployment

This project was developed using the GitPod IDE, committing to Git for every meaningful change and pushing commits to GitHub via the terminal Git commands. On GitHub I was able to view the Code Institute template reccomended for GitPod use, clone it, and then create my own repository with the template. After this it was possible to create a new workspace using GitPod.

### Local Deployment

In order for this project to be run locally, the user would require an IDE such as GitPod and the following features to be installed:

* Python3
* Django
* PIP
* Git would be required for version control throughout

Once you have met the above criteria you would be ready to clone this project to run locally. 

* At the top of the page clicking the green 'Clone or Download' gives you two otions to clone this GitHub repository. You can download the file as a zip-file and upload it into your new workspace, please ensure that you unzip the file first. Or alternatively you can copy the repository web URL, open the Git CLI terminal and type: git clone https://github.com/JonWil91/Milestone-4.git.
* Ensure you have navigated to the correct file location using the 'cd' command
* The next step would be to create a file named 'env.py', this will be an important file for safely storying your credentials. 
* The next required step would be ensuring you have an up to date requirements.txt file. This can be initialised by typing 'sudo -H pip3 -r requirements.txt' into the terminal, the syntax may differ slightly between IDE's as for use in GitPod the 'sudo' element was not required.

Once these steps have been completed you have everything ready to run the application. If you are using the GitPod IDE you would run the command python3 manage.py runserver which will initialise the app and give you the prompt to expose the local host you are running and open it on a browser.

### Remote Deployment

This website has been deployed on Heroku using the master branch on GitHub. To host the project on Heroku the following steps were taken:

1. Sign up and create a free Heroku account and create a new app for later deployment
2. Create a requirements.txt file so that Heroku can install the necessary dependencies to run the app. In the CLI terminal type 'pip3 freeze --local > requirements.txt'
3. Create a Procfile which will tell Heroku what type of application is being deployed and how to run it. In the CLI terminal type 'echo web: python run.py > Procfile'
4. In Heroku after creating the project app, click the 'Deploy' tab, choose GitHub as your deployment method and select Enable Automatic Deployment.
5. Select the Settings tab next and click the 'Reveal Config Vars' button. You will then need to input the following details:


Once these steps have been followed you will be ready to deploy your website to Heroku.

## Credits 

### Media



### Code 



### Acknowledgements

 A big thank you to my mentor, Gerry McBride for  support and positive feedback throughout the project. A special thanks as well to all the Code Institute online support team for their continued patience and encouragement throughout the project.