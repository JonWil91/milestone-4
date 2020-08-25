Full Stack Milestone Project 4 - Code Institute

# JW Photography 


This is my fourth Milestone project of the Full Stack Frameworks with Django module from Code Institute. This project was designed to demonstrate all the knowledge and skills I have developed throughout the Code Institute Fullstack Web Developer course. This project will pull together the HTMl, CSS, JavaScript and Python skills learnt in previous modules and add using Django 3 to develop an e-commerce website.

## Project Purpose

The primary purpose of this project is to allow a user to navigate across the different pages within a visually appealing and user friendly website and purchase photo products. The products displayed on the site are photos I have taken in various countries whilst travelling and they provide a good range of photo types that would be able to appeal to a broad user base. This pulls together all skills that have been learnt throughout the Code Institute course. The project is an e-commerce website that has the purpose of displaying products for the user to browse, add to a shopping cart and purchase. In addition to this were two custom models for the project which were used in the blog section where users can add comments to a blog and use the contact page to send a message to the Superuser admin panel.

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
    - [**Compatibility**](#compatibility)
* [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)
* [**Credits**](#credits)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

## UX

It is made clear to the user that the site is an e-commerce site from the home page due to the clear title and supporting text above the three currently top rated products from the store. The user is able to view these products immediately or visit the gallery page.

The user is able to peruse all available products in the gallery page, this could be achieved by viewing all products as initially displayed, filtering by price/rating/category, or selecting the specific category of interest. This allows the user to filter the products in a broad sense or to narrow down the field to a particular type of product. A user has the ability to register as a user, or login if a previous account has been created, and then add items to a bag and proceed to checkout to make the purchase.

User's also have the ability to use the contact page to send a message to the admin panel, or to view the blog page to read, comment and like various blog posts, as long as they are logged in.

User types would be split into the following categories: - Visitor - Person on the website (not necessarily registered with an account) - Registered User - Person on the website with an account - Admin - Owner of the website (logged in)


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
2. As a visitor I want to be able to filter the total products displayed
3. As a visitor I want to be able to filter products by geographic category
4. As a visitor I want to be able to view individual product details
5. As a registered user, I want to be able to add a product into the shopping cart

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
2. As a registered user I want to be able to update my delivery information on my Profile page
3. As a registered user I want to be able to update my delivery information on the Checkout page

**Pagination**
1. As a visitor I would like to be able to view content split into separate pages to reduce loading times

**Frame Preview**
1. As a visitor I would like to be able to preview what a product looks like with various frame colours

**Content Management**
1. As an admin I want to be able to add product content within the site
2. As an admin I want to be able to edit product content within the site
3. As an admin I want to be able to delete product content within the site
4. As an admin I want to be able to add blog content within the site
5. As an admin I want to be able to edit blog content within the site
6. As an admin I want to be able to delete blog content within the site

### Colour Scheme

I approached this project with a simple minimalist colour scheme in mind, as the main focus is presenting photos that stand out for customers to purchase. The Navbar is a simple off white (#f8f9fa) background with black text and font awesome icons to stand out clearly. The shopping cart icon and product cost are highlighted in a light shade of blue (#17a2b8) to stand out both from the Navbar background and the background colour of the content.

The body background colour throughout is a very light shade of blue (#c3d8e2) so as to not take focus from the products being sold, and so that all text and content is clear and easy to read.

As the photos are intended to be the focus of colour on most pages, I opted to leave the headings as black to make them clear and legible.

The top row of the Footer uses the same grey colour as the Header to display the social media icons in a darker grey (#6f6f6f) to make them stand out. The text footer below this contrasts this by using the same dark grey colour as a background, but using the off white (#f8f9fa) as the icon colours.

Throughout the site blue is used as a colour to signify an option to edit/update, whilst red is associated with removing or deleting content.


### Wireframes

I decided to use hand drawn wireframes for this project. There were alterations from the wireframes in instances that improved user experience in ways that had not been anticipated at the start of development. Examples such as improving the Product Purpose on the homepage so that it was immediately clear to visitors that it was an e-commerce site for photo prints. Other alterations included the products detail page to use the space effectively and having the navigation bar dropping down as a horizontal row instead of a vertical row on tablet and mobile devices. 


## Features

### Existing Features:

* Blog - Allow visitors to see more information posted by the site admin about the products or the photographer
* Responsive layout - Allows visitors to visit the site on any device and resize their browser without losing content
* Search - Allows visitors to quickly navigate to products quickly by searching keywords
* Gallery - Allows visitors to view and narrow down images by selecting filters
* Contact - Allows visitors to contact the site owner by filling out a form 
* Account/ Authentication - Allows visitors more interaction with the website by registering / logging in to become registered users
* Shopping - Allows registered users to buy their favourite prints
* Payment - use the following Stripe test card details for test payments:
	* Card Number - 4242 4242 4242 4242
	* MM / YY - Any number
	* CVC - Any number
	* Zip Code - Any number
* Shopping Cart - Allows registered users to add and remove products before buying
* Messages - Allows the visitor to receive relevant feedback on actions taken by posting a message in the top right corner of the screen
* Pagination - Allows pages to load faster where there is a large amount of content and reduces unnecessary data transfer
* Content management - Allows admins to update content & products on the site
* Frame preview - Allows visitors to preview a selected print in a variety of frame colours before purchasing
* Checkout - Allows users to checkout and make a secure payment for their product(s)

### Future Features:

* Enhanced search - Allow visitors to search for keywords in blog posts in addition to products
* Gallery pagination - Add pagination to the gallery
* Enhanced pagination - Visitors on mobile devices load less products on each page when not on WiFi so as to reduce data usage.
* Animations - Add animation to the home page to make products look more dynamic and appealing upon visiting the website
* Add option for registered users to delete their account
* Add load more button to profile page in case of high number of previous orders

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



## **Testing**

The majority of testing for this project was done manually, however online validators were used to check the code. These will be detailed below under the Code Validation heading. Testing focused on ensuring that the User Stories are being adhered to, that the website is responsive across all desktop, tablet and mobile devices and that the development is following the guidance of the wireframes where appropriate. 

Testing scripts have been written to test all user stories and ensure they work as intended. The attached test scripts are based on testing on a desktop as the steps sometimes vary for tablet & mobile.

# AUTOMATIC TESTING WAS DONE...


Blog:

_As a visitor I want to be able to view an overview of the latest blog posts_



*   Pre-requisites: \
– Visitor is on desktop and on the homepage
*   Steps: \
– 1. Click blog button in navigation bar

Expectation :



*   Blogs page loads
*   The last four blog posts displayed
*   Page is set to 1 of x
*   Each post has the title and date visible

_As a visitor I want to be able to view a single, full blog post_



*   Pre-requisites: \
– Visitor is on desktop and on the blog page
*   Steps: \
– 1. Click a blog’s title

Expectation:



*   Blog’s content is visible
*   Number of likes is displayed and accurate
*   Comments are displayed and accurate

_As a registered user, I want to be able to comment on a single blog post_



*   Pre-requisites: \
- registered User is logged in on desktop and on the blog page
*   Steps: \
– 1. Click a blog’s title \
– – See single blog post \
– 2. Click Add Comment link \
– – See comment form displayed \
– 3. Fill in add comment form \
– 4. Click submit button

Expectation:



*   Redirected to single blog post
*   Comment is displayed under blog post
*   Receive message confirmation of successfully added comment

_As a registered user, I want to be able to add a like to a single blog post_



*   Pre-requisites: \
– registered User is logged in on desktop and on the blog page
*   Steps: \
– 1. Click a blog’s title \
– – See single blog post \
– – Like button is colour blue as user not clicked \
– 2. Click Like button

Expectation:



*   Like button changes to a red Unlike button
*   Number of likes increases by 1

Search:

_As a visitor I want to be able to find products within the site based on typing in keywords into the search bar_



*   Pre-requisites: \
– – Visitor is on desktop and on the homepage \
Steps:
    1. Type search request into the search bar

Expectations:



*   Loads relevant products on Gallery page
*   If no match found, text on page states “0 Products found for ‘x’”

Gallery:

_As a visitor I want to be able to view an overview of the products available_



*   Pre-requisites: \
– – Visitor is on desktop and on the homepage
*   Steps:
    1. Click Gallery button in navigation bar

Expectation:



*   Gallery page loads
*   All Products are displayed
*   Each Product has an image and related information visible

_As a visitor I want to be able to filter the total products displayed_



*   Pre-requisites: -- -- Visitor is on desktop and on the Gallery page
*   Steps:
    1. Click on All Products dropdown link
    2. Select filter option

Expectation:



*   All Products filtered by visitor selection

_As a visitor I want to be able to filter products by geographic category_



*   Pre-requisites: -- -- Visitor is on desktop and on the Gallery page
*   Steps:
1. Click on preferred geographic filter option

Expectation:



*   All Products within geographic Category selection displayed

_As a visitor I want to be able to view individual product details_



*   Pre-requisites: \
– – Visitor is on desktop and on the Gallery page
*   Steps:
    1. Click on Product image

Expectation:



*   Product image and details are visible

_As a registered user, I want to be able to add a product into the shopping bag_



*   Pre-requisites: \
– – Registered user is on desktop, logged in and on Product details page
*   Steps:
    1. Select frame colour 
    2. Select size from dropdown
    3. Select quantity of product
    4. Click Add to Bag button

Expectation:



*   View success message confirming the size and quantity of the selected Product added to the shopping bag

Contact:

_As a visitor I want to be able to submit a message to the site admin_



*   Pre-requisites: \
– – Visitor is on desktop and on the homepage
*   Steps:
    1. Click on Contact button in navigation bar \
– – See a contact form
    1. Fill in contact form
    2. Click send message button

Expectation:



*   Receive confirmation that the message has been received
*   Redirected to the homepage

_As an admin I want to be able to view messages submitted by visitors and users_



*   Pre-requisites: \
– – Admin is on desktop, logged in and on the admin home page URL
*   Steps:
    1. Click the Contact model

Expectation:



*   All submitted messages are displayed

Account / Authentication:

_As a visitor I want to be able to register for an account_



*   Pre-requisites: \
– – Visitor is on desktop, on the homepage & does not have an account 
*   Steps:
    1. Click on My Account button in the navigation bar
    2. Select Register from the dropdown \
– – See a Sign Up form
    3. Fill in sign up form
    4. Click Sign Up button
    5. Visitor directed to check email for link
    6. Click link sent to email to confirm registration
    7. – – See confirm registration page
    8. Visitor to confirm email then Click Confirm button

Expectation:



*   Receive confirmation message that registration successful  

_As a registered user I want to be able to login to my account_



*   Pre-requisites: \
– – registered user is on desktop,on the homepage and not logged in
*   Steps:
    1. Click on My Account button in the navigation bar
    2. Select Log In from the dropdown \
– – See a Sign in form
    3. Complete sign in form
    4. Click Sign In

Expectation:



*   Receive confirmation message confirming log in success
*   A redirect to the homepage

_As a registered user I want to be able to log out of my account_



*   Pre-requisites: \
– – Registered user is on desktop ,on the homepage and logged in
*   Steps:
    1. Click on username in the navigation bar
    2. Select Sign Out from the dropdown \
– – See a Sign Out confirmation button
    3. Click Sign Out

Expectation:



*   Receive a confirmation message confirming Sign Out successful 
*   A redirect to the homepage 

Shopping Bag

_As a registered user I want to be able to view my shopping bag_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the homepage. Items are in the shopping bag. 
*   Steps:
    1. Click on Shopping bag icon

Expectation:



*   Shopping bag page loads
*   Product content, size, quantity and cost are displayed

_As a registered user I want to be able to edit the items in my shopping bag_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the Shopping bag page. Items are in the shopping bag.
*   Steps:
    1. Click on the + or - symbols to alter the quantity of selected product \
– – This can also be achieved by typing a new number in the text box
    2. Click the update button \
Expectation:
*   Receive a confirmation message that the shopping bag has been updated
*   Product quantity and subtotal change to reflect the update

_As a registered user I want to be able to remove an item from my shopping bag_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the Shopping Bag page. Items are in the shopping bag.
*   Steps:
    1. Click remove button next to applicable product  \
Expectation:
*   Receive a confirmation message that the product has been removed
*   Be redirected to a shopping bag page confirming the applicable product has been removed
*   If shopping bag now empty page displays text stating shopping bag is empty

Checkout:

_As a user I want to be able to securely checkout and make a payment for my product(s)_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the Shopping Bag page. Items are in the shopping bag.
*   Steps:
    2. Click on Secure Checkout button \
– – See a checkout form with order summary
    3. Fill in personal details and payment information
    4. Click Complete Order

Expectation:



*   Receive confirmation message of successful purchase 
*   redirected to an order summary
*   Receive a confirmation email of successful purchase

_As a registered user I want my checkout details to be saved to my profile_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the Checkout page with items in shopping bag.
*   Steps:
    1. Complete delivery form 
    2. Click ‘save this delivery information to my profile’ button
    3. 3. Click Complete Order

Expectation:



*   Details from delivery section on checkout form to be saved in Profile page

Profile:

_As a registered user I want information from my order to be saved and viewable_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the homepage. User has ‘save delivery information to profile’ selected on checkouts. 
*   Steps:
    1. Click on user name in navigation bar
    2. Select ‘My Profile’ from dropdown list 

Expectation:



*   Details from current order will be displayed 
*   Details from previous orders will be displayed

_As a registered user I want to be able to update my delivery information on my Profile page_



*   Pre-requisites: \
– – Registered user is on desktop, logged in and on the Profile page
*   Steps:
    1. Fill in default delivery information form
    2. Click Update Information button

Expectation:



*   A message confirming that the Profile has been updated successfully

_As a registered user I want to be able to update my delivery information on the Checkout page_



*   Pre-requisites: \
– – registered User is on desktop, logged in and on the Checkout page with items in shopping bag.
*   Steps:
    3. Update existing delivery info
    4. Click ‘save this delivery information to my profile’ button
    5. Click Complete Order

Expectation:



*   Updated details from delivery section on checkout form to be saved in Profile page

Pagination:

_As a visitor I would like to be able to view blog content split into separate pages to reduce loading times_



*   Pre-requisites: \
– – Visitor is on desktop and on the homepage
*   Steps:
    1. Click on Blog button in the navigation bar
    2. Blog page loads, with pagination feature stating what number page visitor is on and total number of pages available 
    3. Click Next

Expectation:



*   Next page of blog posts loads
*   Pagination feature displays the new page number visitor is on out of total available 
*   Option to click Previous to return to previous page
*   Option to click Next again if there is another page of content

Frame Preview:

_As a visitor I would like to be able to preview what a product looks like with various frame colours_



*   Pre-requisites: \
– – Visitor is on desktop and on the product details page
*   Steps:
    1. Click on any of the coloured circular buttons under Frame Colour

Expectation:



*   Border colour of image to change based on the visitor selection

Content Management:

_As an admin I want to be able to add product content within the site_



*   Pre-requisites: \
– – Admin is on desktop, on the homepage and logged in
*   Steps:
    1. Click on admin username from the navigation bar 
    2. Click Add Product from dropdown \
– – See an add product form
    3. Fill in add product form
    4. Click Add Product button

Expectation:



*   A message confirming the product has been successfully added
*   A redirect to the newly added page

_As an admin I want to be able to edit product content within the site_



*   Pre-requisites: \
– – Admin is on desktop and logged in. This script works on homepage, Gallery page and product details page
*   Steps:
    1. Click on edit button \
– – See edit product form with current information included \
– – See alert message warning edit status is live
    2. Make necessary changes to product
    3. Click Update Product button \
Expectation:
*   Confirmation message stating product successfully updated 
*   A redirect to the updated product

_As an admin I want to be able to delete product content within the site_



*   Pre-requisites: \
– – Admin is on desktop and logged in. This script works on homepage, Gallery page and product details page
*   Steps:
    4. Click on delete button \
Expectation:
*   Confirmation message stating product successfully deleted
*   A redirect to Gallery page

_As an admin I want to be able to add blog content within the site_



*   Pre-requisites: \
– – Admin is on desktop, logged in and on the homepage
*   Steps:
    1. Click on admin username from the navigation bar 
    2. Click Add Blog from dropdown \
– – See an add blog form
    3. Fill in add blog form
    4. Click Add Blog button

Expectation:



*   A message confirming the blog has been successfully added
*   A redirect to the newly added blog page

_As an admin I want to be able to edit blog content within the site_



*   Pre-requisites: \
– – Admin is on desktop, logged in and on the Blog page. This script works on the Blog page and individual blog posts.
*   Steps:
    1. Click on edit button \
– – See edit blog form with current information included \
– – See alert message warning edit status is live
    2. Make necessary changes to blog
    3. Click Update Blog button \
Expectation:
*   Confirmation message stating blog successfully updated
*   A redirect to the updated blog post

_As an admin I want to be able to delete blog content within the site_



*   Pre-requisites: \
– – Admin is on desktop, logged in and on the Blog page. This script works on the Blog page and individual blog posts.
*   Steps:
    5. Click on delete button \
Expectation:
*   Confirmation message stating blog successfully deleted
*   A redirect to the Blogs page


### Differences in content display across difference devices

* Navigational bar:
	* Desktop - Brand title, search box and navigational links all displayed in one row
	* Tablet - Brand title top left corner, burger menu top right corner of one row and search box centre of next row. When burger menu is clicked the navigational links drop down to a row of six beneath the search box, centrally aligned
	* Mobile - Brand title top left corner, burger menu top right corner of one row and search box centre of next row. When burger menu is clicked the navigational links drop down to two rows of three beneath the search box, centrally aligned
* Home page:
	* Desktop and Tablet - Products displayed horizontally in rows of three
	* Mobile - Products displayed vertically one on top of another
* Blogs:
	* Desktop and Tablet - Blogs displayed horizontally in rows of two
	* Mobile - Blogs displayed vertically one on top of another
* Gallery:
	* Desktop - Products displayed horizontolly in rows of four
	* Tablet - Products displayed horizontolly in rows of two
	* Mobile - Products displayed vertically one on top of another
* Product Details:
	* Desktop - Product image with location and location link displayed beneath on one half of screen with product details and interactive buttons on the other side
	* Tablet and Mobile - Product image with location and location link displayed above product details and interactive buttons
* Profile Page:
	* Desktop - Default delivery information displayed in one half of screen with order history taking up the other half
	* Tablet and Mobile - Default delivery information displayed above order history
* Shopping Bag:
	* Desktop and Tablet - Product image/name/size/cost/quantity and subtotal displayed in one row. Bag total, delivery costs and grand total displayed bottom right above buttons to keep shopping or checkout
	* Mobile - Bag total, delivery costs, grand total cost, keep shopping and checkout buttons all displayed centrally on separate rows. Text stating summary of shopping bag contents below on next row and product image below. Below this, each on a separate row centrally aligned: product name, product size, subtotal, quantity and update/remove buttons. At the bottom of the page is an upwards arrow which takes the registered user to the stop of the screen.
* Checkout:
	* Desktop - Details, delivery information and payment form displayed on one half of the screen, with order summary on the other side
	* Tablet and Mobile - Order summary, details, delivery information and payment form displayed one on top of another.
* Order Information:
	* Desktop and Tablet - Order info headings on one side of screen, with corresponding values on the other side in the corresponding rows
	* Mobile - Order info display in one column, with values displayed directly beneath corresponding headings




### Bugs highlighted by testing

* Found that on the checkout page, the registered user's address was saved to the profile regardless of whether the checkbox was saved
	* To be fixed for a future release
* Found that the quantity selector on the bag page does not limit between 1 (min) and 99 (max) as the product details page does
	* To be fixed for a future release
* Found that the pluralize function was not working on the blog details page for like/likes. A simple fix of a typo in the template
* Found that not all links has the CSS cursor added on, fixed as an oversight

# FIX THIS
* During development the category name for snow themed products was amended from *ski_hill* to *snow* to be more inclusive. Upon testing it was discovered that this change had been applied to the local deployment, but had broken the remote deployment product geographical filter link *snow*. 


### Code Validation

* I used the W3C HTML Validator tool to validate my HTML code. The W3C Validator tool doesn't recognise the Jinja templating, which resulted in it showing a lot of errors in relation to the Jinja code. This meant carefully going through such html files to ensure that they were formatted correctly.
* I used the W3C CSS Validator tool to validate my CSS code.
* I used the JSHint tool to validate my JavaScript syntax.
* I used the Pep8 Online tool to validate my Python syntax. I had to update a number of lines that were too long and blank spaces I had initially missed.

## Compatibility

To ensure that the website is accessible and runs across different devices and browsers, I have tested it on the following:

* Chrome
* Safari
* Firefox
* Opera
* Microsoft Edge

## Deployment

This project was developed using the GitPod IDE, committing to Git for every meaningful change and pushing commits to GitHub via the terminal Git commands. On GitHub I was able to view the Code Institute template recommended for GitPod use, clone it, and then create my own repository with the template. After this, it was possible to create a new workspace using GitPod.

### Local Deployment


*   In the terminal enter `git clone [https://github.com/jonwil91/milestone-4](https://github.com/jonwil91/milestone-4)` to make a clone of this repository. Alternatively, by clicking the green 'Clone or Download' you can download the file as a zip-file and upload it into your new workspace, please ensure that you unzip the file first. 
*   In the terminal enter `cd milestone-4` (path to folder)
*   The next step would be to create a ‘.env’, this will be an important file for safely storing your credentials. These can also be stored as GitPod environment variables if used the GitPod IDE.
*   In the terminal enter `pip3 install -r requirements.txt` to install necessary dependencies
*   In the terminal enter `python3 manage.py migrate` to create the database schema
    *   After this stage you ought to notice a db.sqlite3 database file has been created
*   At this point if you enter `python3 manage.py runserver` you will be able to expose the app to port 8000. Products will not yet be displayed
*   The next two inputs have to be entered in this order:
    *   `python3 manage.py loaddata categories`
    *   `python3 manage.py loaddata products`
*   In the terminal enter `python3 manage.py createsuperuser` to create an admin account to access Django’s admin panel
*   In the terminal, in the following order enter
	*   `add .`, 
	*    `git commit -m “[Message for commit]”`,
	*    `git push`.
	*    This will push and safely store all changes to GitHub

At this point the local deployment is functional, bar the checkout feature using Stripe. To add this functionality, sign up for an account with [Stripe](www.stripe.com), collect the following variables to add to the ‘.env’ file

 *   STRIPE_SECRET_KEY = Value
 *   STRIPE_PUBLIC_KEY = Value
 *   STRIPE_WH_KEY = Value

Please note that for testing the checkout feature using Stripe, the test card number is: 4242 4242 4242 (the CVC and expiry date can be any number)

### Remote Deployment

**The deployed site can be found at: https://jw-photography.herokuapp.com**


*   Ensure that you have Procfile created to tell Heroku the type of application using gunicorn and how to run it
*   Visit [Heroku]([www.heroku.com](www.heroku.com)), register and create a new app
*   In the deploy tab set GitHub as deployment method and search for repository (will have to sign into GitHub if a new user)
    *   Click enable automatic deploys to push to Heroku master when pushing to GitHub
    *   In Resources tab, in search bar, look for Heroku Postgres and select Hobby Dev - Free - update to remote database
*   In the terminal enter `heroku login -i` and enter your credentials
*   In the terminal enter `heroku git:remote -a [name of Heroku app]`
*   Initialise a new commit 
	*   `git add .`,
	*   `git commit -m “[git commit message]”`
	*   `git push`
*   Create an AWS account, set up an S3 bucket, create a user and policy to authorise
*   Using an email provider such as Gmail, set up a profile to access  EMAIL_HOST_PASS and EMAIL_HOST_USER credentials
*   In Heroku settings, click Reveal Config Vars and add the following:
    *   AWS_ACCESS_KEY = Value
    *   AWS_SECRET_ACCESS_KEY  = Value
    *   DATABASE_URL = Value
    *   EMAIL_HOST_PASS = Value
    *   EMAIL_HOST_USER = Value
    *   SECRET_KEY = Value
    *   STRIPE_SECRET_KEY = Value
    *   STRIPE_PUBLIC_KEY = Value
    *   STRIPE_WH_KEY = Value
    *   USE_AWS = True
*   The above variables, with the exception of USE_AWS ought to be saved in the settings.py file in the following format:
	*`AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', '')`
 * Make final migrations, in the terminal enter:
 	* `python3 manage.py makemigrations`
    * `python3 manage.py migrate`
  * Once the Heroku build is migrated and completed you can open the app
  * Additional objects can be added to the app through the admin panel, and media saved in the S3 bucket

## Credits 

### Content 

* The Checkout, Profiles and Bag apps were taken from Code Institute mini-project
* Widgets.py files in Blog and Products app were taken from Code Institute mini-project
* *like_view* in Blog app was taken from Youtube [Codemy tutorial](https://www.youtube.com/watch?v=PXqRPqDjDgc&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=18)
* *add_comment* view in Blog app was inspired by Youtube [Coedmy tutorial](https://www.youtube.com/watch?v=OuOB9ADT_bo&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=34)
* Change frame colour feature was inspired by Youtube [The Webshala](https://www.youtube.com/watch?v=lGNwc_DLRfw)
* [Compress Jpg](https://compressjpeg.com/) used to compress images
* Pagination inspired by Youtube video [Parwiz Forogh](https://www.youtube.com/watch?v=N_TWOfLlc7A)

### Media

* All product images are owned by me
	* *No Image* available image was taken from [Google](https://www.google.com/search?q=no+image+available+image&tbm=isch&ved=2ahUKEwjggIKRuLbrAhXJuxoKHY43C9MQ2-cCegQIABAA&oq=no+image+available+&gs_lcp=CgNpbWcQARgCMgQIABBDMgQIABBDMgQIABBDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFDZfFjZfGDhiwFoAHAAeACAAUmIAUmSAQExmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=IQ9FX6DsHMn3ao7vrJgN&bih=978&biw=1920#imgrc=d2Y8RJMlsclozM&imgdii=KG6Rbsh8IbhRxM)
	* Picture of camera in blog was was taken from [Electronics Frontier](https://www.electronicsfrontier.com/nikon-d3500-digital-slr-camera-af-p-18-55mm-f-3-5-5-6g-vr-lens-kit.html?utm_source=shopello_gb&utm_medium=cpo&utm_campaign=google+shopping+ads&utm_term=misc-16284&utm_content=Cj0KCQjw7ZL6BRCmARIsAH6XFDIbHOnDNTirkwUFL8m3GAQmN5stuvAeXLoPDpv3-OBvgqXPpi3nlrAaAqNiEALw_wcB%3B22%3B0)
* Used [Compress Jpg](https://compressjpeg.com/) to compress product image files
* Used [Mastering Markdown](https://jbt.github.io/markdown-editor/#ux) as a Markdown Editor



### Acknowledgements

 A big thank you to my mentor, Gerry McBride for  support and positive feedback throughout the project. A special thanks as well to Roz and Tom for continued support and all the Code Institute online support team for their patience and encouragement throughout the project.