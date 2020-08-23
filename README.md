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
    - [**Existing Features**](#existing-features)
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

It is made clear to the user that the site is an e-commerce site from the home page due to the clear title and supporting text above the three currently top rated products from the store. The user is able to view these products immidiately or visit the gallery page.

The user is able to peruse all available products in the gallery page, this could be achieved by viewing all products as initially displayed, filtering by price/rating/category, or selecting the specific category of interest. This allows the user to filter the products in a broad sense or to narrow down the field to a particular type of product. A user has the ability to register as a user, or login if a previous account has been created, and then add items to a bag and  proceed to checkout to make the purchase.

User's also have the ability to use the contact page to send a message to the admin panel, or to view the blog page to read, comment and like various blog posts, as long as they are logged in.

User types woud be split into the following categories:
	- Visitor - Person on the website (not necessarily registered with an account)
	- Registered User - Person on the website with an account
    -Admin - Owner of the website (logged in)

### User stories:

**Blog**
1. As a visitor I want to be able to view an overview of the latest blog posts
2. As a visitor I want to be able to view a single, full blog post
3. As a registered user, I want to be able to comment on a single blog post
4. As a registered user, I want to be able to like a single blog post

**Search**
1. As a visitor I want to be able to find products within the site based on typing in keywords into the search bar

**Gallery**
1. As a visitor I want to be able to view an overview of the products available
2. As a visitor I want to be able to filter the products displayed
3. As a visitor I want to be able to view individual product details
4. As a registered user, I want to be able to add a product into the shopping cart

**Contact**
1. As a visitor I want to be able to submit a message to the site admin
2. As an admin I want to be able to view messages submitted by visitors and users

**Account / Authentication**
1. As a visitor I want to be able to register for an account
2. As a registered user I want to be able to login to my account 
3. As a registered user I want to be able to log out of my account

**Shopping Bag**
1. As a registered user I want to be able to view my shopping bag 
2. As a registered user I want to be able to edit the items in my shopping bag
3. As a registered user I want to be able to remove an item from my shopping bag

**Checkout**
1. As a registered user I want to be able to securely checkout and make a payment for my product(s)
2. As a registered user I want my checkout delivery details to be saved to my profile

**Profile**
1. As a registered user I want information from my order to be saved and viewable
2. As a registered user I want to be able to update my delivery information

**Pagination**
1. As a visitor I would like to be able to view content split into separate pages to reduce loading times

**Frame Preview**
1. As a visitor I would like to be able to preview what a product looks like with various frame colours

**Content Management**
1. As an admin I want to be able to add product content within the site
2. As an admin I want to be able to edit and delete product content within the site
3. As an admin I want to be able to add blog content within the site
4. As an admin I want to be able to edit and delete blog content within the site

### Colour Scheme

I approched this project with a simple minimalist colour scheme in mind, as the main focus is presenting photos that stand out for customers to purchase. The Navbar is a simple off white (#f8f9fa) background with black text and font awesome icons to stand out clearly. The shopping cart icon and product cost are highlighted in a light shade of blue (#17a2b8) to stand out both from the Navbar background and the background colour of the content.

The body background colour throughout is a very light shade of blue (#c3d8e2) so as to not take focus from the products being sold, and so that all text and content is clear and easy to read.

As the photos are intended to be the focus of colour on most pages, I opted to leave the headings as black to make them clear and legible.

The top row of the Footer uses the same grey colour as the Header to display the social media icons in a darker grey (#6f6f6f) to make them stand out. The text footer below this contrasts this by using the same dark grey colour as a background, but using the off white (#f8f9fa) as the icon colours.

Throughout the site blue is used as a colour to signify an option to edit/update, whilst red is associated with removing or deleting content.

### Wireframes

I decided to use handrawn wireframes for this project, as there are a lot of features on certain pages which would be easier to reflect by hand. For the most part the wireframes match up with the final product, with the exception of the introduction to pagination and an alteration to the product details pages, which were introduced during the production process.

## Features

### Existing Features:

* Blog - Allow visitors to see more information posted by the site admin about the products or the photographer
* Responsive layout - Allows visitors to visit the site on any device and resize their browser without losing content
* Search - Allows visitors to quickly navigate to products quickly by searching key words
* Gallery - Allows visitors to view and narrow down images by selecting filters
* Contact - Allows visitors to contact the site owner by filling out a form 
* Account/ Authentication - Allows visitors more interaction with the website by registering / logging in to become registerd users
* Shopping - Allows registered users to buy their favourite prints
* Shopping Cart - Allows registered users to add and remove products before buying
* Messages - Allows the visitor to receive relevant feedback on actions taken by posting a message in the top right corner of the screen
* Pagination - Allows pages to load faster where there is a large amount of content and reduces unnneccessary data transfer
* Content management - Allows admins to update content & products on the site
* Frame preview - Allows visitors to preview a selected print in a variety of frame colours before purchasing
* Checkout - Allows users to checkout and make a secure payment for their product(s)

### Future Features:

* Enhanced search - Allow visitors to search for key words in blog posts in addition to products
* Gallery pagination - Add pagination to the gallery
* Enhanced pagination - Visitors on mobile devices load less products on each page when not on WiFi so as to reduce data usage.
* Animations - Add animation to the home page to make products look more dynamic and appealing upon visiting the website

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
* [Postgres](https://www.postgresql.org/)
    - The project uses **Postgres** as the database upon deployment to Heroku
* [AWS - S3](https://aws.amazon.com/s3/)
    - The project uses **AWS S3** as an object storage service for static files and media files

## Testing

All of the testing for this project was done manually, however online validators were used to check the code used. These will be detailed below under the Code Validation heading. Testing always focussed on ensuring that the User Stories were being adhered to, that the website is responsive across all desktop, tablet and mobile devices and that the develoment was following the guidance of the wireframes where appropriate.

**Blog**:

*As a visitor I want to be able to view an overview of the latest blog posts*

- Pre-requisites:
-- Visitor is on desktop and on the homepage
- Steps:
-- 1. Click blog button in navigation bar

Expectation :
- Blogs page loads
- The last four blog posts displayed
- Page is set to 1 of x
- Each post has the title and date visible


*As a visitor I want to be able to view a single, full blog post*

- Pre-requisites:
-- Visitor is on desktop and on the blog page
- Steps:
-- 1. Click a blog’s title

Expectation:
- Blog’s content is visible
- Number of likes is displayed and accurate
- Comments are displayed and accurate

*As a registered user, I want to be able to comment on a single blog post*

- Pre-requisites:
-User is logged in on desktop and on the blog page
- Steps:
-- 1. Click a blog’s title 
--  -- See single blog post
-- 2. Click Add Comment link
--  -- See comment form displayed
-- 3. Fill in add comment form
-- 4. Click submit button

Expectation:
- Redirected to single blog post
- Comment is displayed under blog post

*As a registered user, I want to be able to add a like to a single blog post*

- Pre-requisites:
-- User is logged in on desktop and on the blog page

- Steps:
-- 1. Click a blog’s title
--  -- See single blog post
--  -- Like button is colour blue as user not clicked 
-- 2. Click Like button

Expectation:
- Like button changes to a red Unlike button
- Number of likes increases by 1

**Search**:

*As a visitor I want to be able to find products within the site based on typing in keywords into the search bar* 

- Pre-requisites:
--  -- Visitor is on desktop and on the homepage
Steps:
    1. Type search request into the search bar

Expectations:

- Loads any relavent products on the Gallery page
- If the search bar input does not match any product name or description, it loads the Gallery page stating "0 Products found for 'x'"

**Gallery**:

*As a visitor I want to be able to view an overview of the products available* 

- Pre-requisites:
--  -- Visitor is on desktop and on the homepage
- Steps:
    1. Click Gallery button in navigation bar

Expectation:
- Gallery page loads
- All Products are displayed
- Each Product has an image and related information visible

*As a visitor I want to be able to filter the products displayed*

- Pre-requisites:
--  -- Visitor is on desktop and on the Gallery page
- Steps:
    1. Click on All Products dropdown link
    2. Click on individual Category links

Expectation:
- All Products are filtered by visitor selection
- All Products within Category selection are displayed

*As a visitor I want to be able to view individual product details*

- Pre-requisites:
--  -- Visitor is on desktop and on the Gallery page
- Steps:
    1. Click on Product image

Expectation:
- Product image and details are visible

*As a registered user, I want to be able to add a product into the shopping cart*

- Pre-requisites:
--  -- Visitor is on desktop and on a Product details page
- Steps:
    1. Select size from dropdown
    2. Select quantity
    3. Click Add to Bag button

Expectation:
- View success message confirming the size and quantity of the selected Product have been added to the shopping cart

**Contact**:

*As a visitor I want to be able to submit a message to the site admin*

- Pre-requisites:
--  -- Visitor is on desktop and on the homepage
- Steps:
    1. Click on Contact button in navigation bar
    2. Fill in contact form
    3. Click send message button

Expectation:
- Receive confirmation that the message has been received

*As an admin I want to be able to view messages submitted by visitors and users*

- Pre-requisites:
--  -- Admin is on desktop and on the home page
- Steps:
    1. Change the end of the homepage URL to /admin
    2. Click the Contact model

Expectation:
- All submitted contacts are displayed

**Account / Authentication**:

*As a visitor I want to be able to register for an account*

- Pre-requisites:
--  -- Visitor is on desktop and on the homepage
- Steps:
    1. Click on My Account button in the navigation bar
    2. Select Register from the dropdown
--  -- See a Sign Up form
    3. Fill in sign up form
    4. Click Sign Up button
    5. Click link sent to email to confirm registration
    6. Click the Confirm button

Expectation:
- Receive confirmation email after registering account
- Receive confirmation message after confirming email address

*As a registered user I want to be able to login to my account*

- Pre-requisites:
--  -- Visitor is on desktop and on the homepage
- Steps:
    1. Click on My Account button in the navigation bar
    2. Select Log In from the dropdown
--  -- See a Sign in form
    3. Fill in sign in form

Expectation:
- Choose between Username or email for first box and password in the next to log in
- Receive confirmation message confirming log in success

*As a registered user I want to be able to log out of my account*

- Pre-requisites:
--  -- Visitor is on desktop and on the homepage
- Steps:
    1. Click on My Account button (now replaced with your username) in the navigation bar
    2. Select Log Out from the dropdown
--  -- See a Sign Out confirmation button
    3. Click Sign Out

Expectation:
- Receive a confirmation message confirming I have signed out

**Shopping Bag**

*As a registered user I want to be able to view my shopping bag*

- Pre-requisites:
--  -- Visitor is on desktop and on the homepage
- Steps:
    1. Click on Shopping cart icon

Expectation:
- Shopping cart page loads
- Product content, size, quantity and cost are displayed

*As a registered user I want to be able to edit the items in my shopping bag*

- Pre-requisites:
--  -- Visitor is on desktop and on the Shopping Cart page
- Steps:
    1. Click on the + or - symbols to alter the quantity of the selected product in the shopping cart.
--  -- This can also be achieved by typing a new number in the text box
    2. Click the update button
Expectation:
- Receive a confirmation message that the shopping cart has been updated
- Product quantity and subtotal change to reflect the update

*As a registered user I want to be able to remove an item from my shopping bag*

- Pre-requisites:
--  -- Visitor is on desktop and on the Shopping Cart page
- Steps:
    1. Click the remove button
Expectation:
- Receive a confirmation message that the product has been removed
- Be redirected to a shopping cart page confirming the cart is empty

**Checkout**:

*As a user I want to be able to securely checkout and make a payment for my product(s)*

- Pre-requisites:
--  -- Visitor is on desktop and on the Shopping Cart page
- Steps:
    1. Click on Secure Checkout button
--  --  See a checkout form with order summary
    2. Fill in personal details and payment information
    3. Click Complete Order

Expectation:
- Receive confirmation message of successful purchase and redirected to an order summary
- Receive a confirmation email of successful purchase
- Data from order to be saved onto a Profile page

*As a registered user I want my checkout details to be saved to my profile*

- Pre-requisites:
--  -- Visitor is on desktop and on the Checkout page
- Steps:
    1. Click the 'save this delivery information to my profile' button after filling in delivery form
    2. Click Complete Order

Expectation:
- Details from delivery section on checkout form to be saved onto a Profile page


**Profile**:

*As a registered user I want information from my order to be saved and viewable*

- Pre-requisites:
--  -- Visitor is on desktop and on the homepage
- Steps:
    1. Click on the account button (the user's name) dropdown and select My Profile

Expectation:
- Details from registered user order will be displayed if the save details box was checked
- Details from registered user's previous orders will be displayed

*As a registered user I want to be able to update my delivery information*

- Pre-requisites:
--  -- Visitor is on desktop and on the Profile page
- Steps:
    1. Fill in default delivery information form
    2. Click update information button
--  -- An update to delivery information can also be achieved by an additional order and checking the save delivery details box

Expectation:
- A message confirming that the Profile has been updated successfully
- Updated information to be displayed on Checkout form

**Pagination**:

*As a visitor I would like to be able to view content split into separate pages to reduce loading times*

- Pre-requisites:
--  -- Visitor is on desktop and on the homepage
- Steps:
    1. Click on Blog button in the navigation bar
    2. Blog page loads, with pagination feature stating what page I am on out of how many
    3. Click Next

Expectation:
- Next page of blog posts loads
- Pagination feature displays the new page number I am on out of how many
- Option to click Previous
- Option to click Next again if there is another page of content

**Frame Preview**:

*As a visitor I would like to be able to preview what a product looks like with various frame colours*

- Pre-requisites:
--  -- Visitor is on desktop and on the product details page
- Steps:
    1. Click on any of the coloured circular buttons

Expectation:
- Border colour of image to change based on the visitor selection

**Content Management**:

*As an admin I want to be able to add product content within the site*

- Pre-requisites:
--  -- Admin is on desktop and on the homepage
- Steps:
    1. Click on Account button (the admin username) from the navigation bar and click Add Product from dropdown
  --  -- See an add product form
    2. Fill in add product form
    3. Click Add Product button

Expectation:
- A message confirming the product has been succesfully added
- A redirect to the newly added page

*As an admin I want to be able to edit and delete product content within the site*

- Pre-requisites:
--  -- Admin is on desktop and on the homepage. This step can be performed on the homepage, Gallery page or product details page
- Steps:
    1. Click on edit button
--  -- See an edit product form with boxes filled with current information
    2. Make necessary changes to product
    3. Click Update Product button
Expectation:
- A message confirming I am editing a product after clicking edit
- A message confirming I have successfully updated the product

*As an admin I want to be able to add blog content within the site*

- Pre-requisites:
--  -- Admin is on desktop and on the homepage
- Steps:
    1. Click on Account button (the admin username) from the navigation bar and click Add Blog from dropdown
  --  -- See an add blog form
    2. Fill in add blog form
    3. Click Add Blog button

Expectation:
- A message confirming the blog has been succesfully added
- A redirect to the Blogs page

*As an admin I want to be able to edit and delete blog content within the site*

- Pre-requisites:
--  -- Admin is on desktop and on the Blog page
- Steps:
    1. Click on edit button
--  -- See an edit product form with boxes filled with current information
    2. Make necessary changes to product
    3. Click Update Product button
Expectation:
- A message confirming I am editing a blog after clicking edit
- A message confirming I have successfully updated the blog


## Code Validation

* I used the W3C HTML Validator tool to validate my HTML code. The W3C Validator tool doesn't recognise the Jinja templating, which resulted in it showing a lot of errors in relation to the Jinja code. This meant carefully going through such html files to ensure that they were formatted correctly.
* I used the W3C CSS Validator tool to validate my CSS code.
* I used the JSHint tool to validate my JavaScript syntax.
* I used the Pep8 Online tool to validate my Python syntax. I had to update a number of lines that were too long and blank spaces I had initially missed.

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

* At the top of the page (as it is currently laid out) clicking the green 'Clone or Download' gives you two otions to clone this GitHub repository. You can download the file as a zip-file and upload it into your new workspace, please ensure that you unzip the file first. Or alternatively you can copy the repository web URL, open the Git CLI terminal and type: git clone https://github.com/JonWil91/Milestone-4.git.
* Ensure you have navigated to the correct file location using the 'cd' command
* The next step would be to create a file named 'env.py', this will be an important file for safely storying your credentials. 
* The next required step would be ensuring you have an up to date requirements.txt file. This can be initialised by typing 'sudo -H pip3 -r requirements.txt' into the terminal, the syntax may differ slightly between IDE's as for use in GitPod the 'sudo' element was not required.
* Next you would be required to make migrations to the database. This would be done in two steps: python3 manage.py makemigrations, and then python3 manage.py migrate
* After migrations are made you would need to load the data from the fixtures. This has to be done in this order: python3 manage.py loadata categories, python3 manage.py loadata products. An error will occur if you try and load products before categories.

Once these steps have been completed you have everything ready to run the application. If you are using the GitPod IDE you would run the command python3 manage.py runserver which will initialise the app and give you the prompt to expose the local host you are running and open it on a browser.

### Remote Deployment

This website has been deployed on Heroku using the master branch on GitHub. To host the project on Heroku the following steps were taken:

1. Sign up and create a free Heroku account and create a new app for later deployment
2. Create a requirements.txt file so that Heroku can install the necessary dependencies to run the app. In the CLI terminal type 'pip3 freeze --local > requirements.txt'
3. Create a Procfile which will tell Heroku what type of application is being deployed and how to run it.
4. In Heroku after creating the project app, click the 'Deploy' tab, choose GitHub as your deployment method and select Enable Automatic Deployment.
5. Create an AWS account, set up an S3 bucket, create a user and policy to authorise
6. Link the AWS account to Heroku and the IDE
7. Select the Settings tab next and click the 'Reveal Config Vars' button. You will then need to input the all secret key data that you do not want to be caught in version control due to risk of users being able to cause malicious damage.

Once these steps have been followed you will be ready to deploy your website to Heroku.

## Credits 

### Media



### Code 



### Acknowledgements

 A big thank you to my mentor, Gerry McBride for  support and positive feedback throughout the project. A special thanks as well to all the Code Institute online support team for their continued patience and encouragement throughout the project.