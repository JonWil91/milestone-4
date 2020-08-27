Full Stack Milestone Project 4 - Code Institute


# **JW Photography**

This is my fourth Milestone project of the Full Stack Frameworks with Django module from Code Institute. This project was designed to demonstrate all the knowledge and skills I have developed throughout the Code Institute Fullstack Web Developer course. This project will pull together the HTMl, CSS, JavaScript and Python skills learnt in previous modules and add using Django3 to develop an e-commerce website.


## **Project Purpose**

This project pulls together all skills that have been learnt throughout the Code Institute course. The project is an e-commerce website that has the purpose of displaying products for the user to browse, add to a shopping cart and purchase. In addition to this are two custom models, in the blog section where users can add comments to a blog and in the contact page where users can send a message to the Superuser admin panel.

The primary purpose of this project is to allow a user to purchase photo products and navigate across the different pages within a visually appealing and user friendly website. The products displayed on the site are photos I have taken in various countries whilst travelling and provide a good range of photo categories  so as to appeal to a broad user base. 

This website  offers value to users as it provides a number of different style photos available to purchase and browse. There is also a blog section to learn more about the website owners and about certain photos.

Note for using site

When making a payment on the site,  please use the following Stripe test card details:



*   Card Number - 4242 4242 4242 4242
*   MM / YY - Any current or future date
*   CVC - Any number
*   ZIP Code - Any number


## **Table of Contents**



*   [UX](#ux)
    *   [User Stories](#user-stories)
    *   [Colour Scheme](#colour-scheme)
    *   [Wireframes](#wireframes)
*   [Features](#features)
    *   [Existing Features](#existing-features)
    *   [Future Features](#future-features)
*   [Technologies Used](#technologies-used)
*   [Testing](#testing)
    *   [Code Validation](#code-validation)
    *   [Compatibility](#compatibility)
*   [Deployment](#deployment)
    *   [Local Deployment](#local-deployment)
    *   [Remote Deployment](#remote-deployment)
*   [Credits](#credits)
    *   [Content](#content)
    *   [Code](#code)
    *   [Acknowledgements](#acknowledgements)


## **UX**

It is clear to the user that the site is an e-commerce site when they land on the home page with the clear title and supporting text above the three current top rated photo products from the store. The user is able to view these products immediately or visit the gallery page for more options.

The user is able to peruse all available products in the gallery page, and can either  view all products as initially displayed, filter by price/rating/category, or select the specific geographic category of interest. This allows the user to narrow down their search to a particular type of product, making the page very user friendly and convenient. A user has the ability to register for an account , or login if one has been created. With an account in place, the user can then add items to a bag and proceed to checkout, with a profile page storing the data of these purchases.

Once a user is registered, they also have the ability to  send a message to the admin panel through the contact page, and to view the blog page where they can read, comment and like various blog posts, as long as they are logged in.

User types are split into the following categories: - Visitor - Person on the website (either not registered with an account or not logged in) - Registered User - Person on the website with an account (logged in) -Admin - Owner of the website (logged in)


### **User stories:**

Blog



1. As a visitor I want to be able to view an overview of the latest blog posts
2. As a visitor I want to be able to view a single, full blog post
3. As a registered user, I want to be able to comment on a single blog post
4. As a registered user, I want to be able to like a single blog post

Search



1. As a visitor I want to be able to find products within the site based on typing in keywords into the search bar

Gallery



1. As a visitor I want to be able to view an overview of the products available
2. As a visitor I want to be able to filter the total products displayed
3. As a visitor I want to be able to filter products by geographic category
4. As a visitor I want to be able to view individual product details
5. As a registered user, I want to be able to add a product into the shopping cart

Contact



1. As a visitor I want to be able to submit a message to the site admin
2. As an admin I want to be able to view messages submitted by visitors and users

Account / Authentication



1. As a visitor I want to be able to register for an account
2. As a registered user I want to be able to login to my account
3. As a registered user I want to be able to log out of my account
4. As a registered user, if I forget a password I want an option to reset it

Shopping Bag



1. As a registered user I want to be able to view my shopping bag
2. As a registered user I want to be able to edit the items in my shopping bag
3. As a registered user I want to be able to remove an item from my shopping bag

Checkout



1. As a registered user I want to be able to securely checkout and make a payment for my product(s)
2. As a registered user I want checkout to handle secure customer authentication when required 
3. As a registered user I want to be told if the payment fails
4. As a registered user I want my checkout delivery details to be saved to my profile

Profile



1. As a registered user I want information from my order to be saved and viewable
2. As a registered user I want to be able to update my delivery information on my Profile page
3. As a registered user I want to be able to update my delivery information on the Checkout page

Pagination



1. As a visitor I would like to be able to view content split into separate pages to reduce loading times

Frame Preview



1. As a visitor I would like to be able to preview what a product looks like with various frame colours

Content Management



1. As an admin I want to be able to add product content within the site
2. As an admin I want to be able to edit product content within the site
3. As an admin I want to be able to delete product content within the site
4. As an admin I want to be able to add blog content within the site
5. As an admin I want to be able to edit blog content within the site
6. As an admin I want to be able to delete blog content within the site
7. As an admin I want to ensure the home page always displays the top rated products


### **Colour Scheme**

I approached this project with a simple minimalist colour scheme in mind, as the main focus is to present photos that stand out for customers to purchase. The Navbar is a simple off white (#f8f9fa) background with black text and font awesome icons to stand out clearly. The shopping bag icon and product cost are highlighted in a light shade of blue (#17a2b8) to stand out both from the Navbar background and the background colour of the content.

The body background colour is a very light shade of blue (#c3d8e2) throughout, so as to not take focus from the products being sold, and so that all text and content is clear and easy to read.

As the photos are intended to be the key focus of colour on most pages, I opted to leave the headings as black to make them clear and legible.

The top row of the Footer uses the same grey colour as the Header to display the social media icons in a darker grey (#6f6f6f) to make them stand out. The text footer below then contrasts this by using the same dark grey colour as a background, but using the off white (#f8f9fa) as the icon colours.

Throughout the site blue is used as a colour to signify an option to edit/update, whilst red is associated with removing or deleting content. This way there is continuity throughout and helps ensure the website is user friendly.


### **Wireframes**

[Link to wireframes folder](https://github.com/JonWil91/milestone-4/tree/master/static/wireframes)

Hand drawn wireframes were used for this project. There were a couple of alterations from the wireframes that had not been anticipated at the start of development as they improved user experience.. Examples such as improving the Product Purpose on the homepage so that the fact it is an e-commerce site for photo prints is immediately clear to visitors upon arrival.  Other alterations include using the space more effectively on the products detail page and having the navigation bar dropping down as a horizontal row instead of a vertical row on tablet and mobile devices.


## **Features**


### **Existing Features:**



*   Blog - Allow visitors to see more information posted by the site admin about the products or the photographer
*   Responsive layout - Allows visitors to visit the site on any device and resize their browser without losing content
*   Search - Allows visitors to quickly navigate to products quickly by searching keywords
*   Gallery - Allows visitors to view and narrow down images by selecting filters
*   Contact - Allows visitors to contact the site owner by filling out a form
*   Account/ Authentication - Allows visitors more interaction with the website by registering / logging in to become registered users
*   Shopping - Allows registered users to buy their favourite prints
*   Shopping Bag - Allows registered users to add and remove products before buying
*   Messages - Allows the visitor to receive relevant feedback on actions taken by posting a message in the top right corner of the screen - for example a successful save.
*   Pagination - Allows pages to load faster where there is a large amount of content and reduces unnecessary data transfer
*   Content management - Allows admins to update content & products on the site
*   Frame preview - Allows visitors to preview a selected print in a variety of frame colours before purchasing
*   Checkout - Allows users to checkout and make a secure payment for their product(s)


### **Future Features:**



*   Enhanced search - Allow visitors to search for keywords in blog posts in addition to products
*   Gallery pagination - Add pagination to the gallery
*   Enhanced pagination - Visitors on mobile devices load less products on each page when not on WiFi so as to reduce data usage.
*   Animations - Add animation to the home page to make products look more dynamic and appealing upon visiting the website
*   Add option for registered users to delete their account
*   Add load more button to profile page in case of high number of previous orders


## **Technologies Used**



*   [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    *   The project uses HTML to create the content and basic elements displayed on the page
*   [CSS](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
    *   The project uses CSS to apply custom styles and colours to the content
*   [Python](https://www.python.org/)
    *   The project uses Python as the back-end programming language
*   [Django](https://www.djangoproject.com/)
    *   The project uses Django in association with Python as a web framework
*   [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
    *   The project uses Jinja for templating the Python and Django code into the HTML files
*   [Stripe API](https://stripe.com/gb)
    *   The project uses Stripe to make secure payments
*   [SQlite](https://www.sqlite.org/index.html)
    *   The project uses SQlite as a database to hold the backend information from the models used within the Python files
*   [Bootstrap](https://getbootstrap.com/)
    *   The project uses Bootstrap for it's responsive, mobile-first approach to front-end web development. It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.
*   [JQuery](https://jquery.com/)
    *   The project uses JQuery as the primary JavaScript functionality and to simplify DOM manipulation.
*   [Google Fonts](https://fonts.google.com/)
    *   The project uses Google Fonts to style the text throughout the site
*   [Font Awesome](https://fontawesome.com/)
    *   The project uses Font Awesome to provide various icons throughout the site
*   [GitPod](https://www.gitpod.io/)
    *   The project uses GitPod as the IDE for development which can be launched from any GitHub page
*   [GitHub](https://github.com/)
    *   The project uses GitHub as a remote repository to push each meaningful change to
*   [Git](https://git-scm.com/)
    *   The project uses Git as version control
*   [Heroku](https://dashboard.heroku.com/apps)
    *   The project uses Heroku as the hosting platform
*   [Postgres](https://www.postgresql.org/)
    *   The project uses Postgres as the database upon deployment to Heroku
*   [AWS - S3](https://aws.amazon.com/s3/)
    *   The project uses AWS S3 as an object storage service for static files and media files


## **Testing**

The majority of testing for this project was done manually, however online validators were used to check the code. These will be detailed below under ‘Code Validation’. Testing focused on ensuring that the User Stories are being adhered to, that the website is responsive across all desktop, tablet and mobile devices and that the development is following the guidance of the wireframes where appropriate.

Testing scripts have been written to test all user stories and ensure they work as intended. The attached test scripts are based on testing on a desktop as the steps sometimes vary for tablet & mobile, as indicated below.


# **AUTOMATION TESTING WAS DONE...**

<details>

<summary>CLICK HERE to expand the full <b>Test Scripts</b>.</summary>

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
*   registered User is logged in on desktop and on the blog page
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
    2. Fill in contact form
    3. Click send message button

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

_As a registered user, if I forget a password I want an option to reset it_



*   Pre-requisites: \
– – Registered user is on desktop, on the homepage & is not logged in
*   Steps:
    9. Click on My Account button in the navigation bar
    10. Select Sign In from the dropdown \
– – See a Sign In form
    11. Click Forgot Password link \
– – See a Password Reset form
    12. Enter email address
    13. Click Reset Password button
    14. Click link sent to email to reset password
    15. – – See Change Password form
    16. Registered user enters new password twice
    17. Click Change Password button

Expectation:



*   Receive confirmation message that changed password successfully
*   Change password form is replaced with text stating ‘Your password is now changed’

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
    1. Click remove button next to applicable product \
Expectation:
*   Receive a confirmation message that the product has been removed
*   Be redirected to a shopping bag page confirming the applicable product has been removed
*   If shopping bag now empty page displays text stating shopping bag is empty

Checkout:

_As a user I want to be able to securely checkout and make a payment for my product(s)_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the Shopping Bag page. Items are in the shopping bag.
*   Steps:
    1. Click on Secure Checkout button \
– – See a checkout form with order summary
    2. Fill in personal details
    3. Fill in Stripe success test card number 4242 4242 4242 4242
    4. Click Complete Order

Expectation:



*   Receive confirmation message of successful purchase
*   Redirected to an order summary
*   Receive a confirmation email of successful purchase

_As a registered user I want the checkout to handle secure customer authentication when required  (pass)_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the Shopping Bag page. Items are in the shopping bag.
*   Steps:
    5. Click on Secure Checkout button \
– – See a checkout form with order summary
    6. Fill in personal details
    7. Fill in Stripe authentication test card number 4000 0025 0000 3155
    8. Click Complete Order \
– – See loading screen followed by authentication model pop up
    9. Click complete authentication

Expectation:



*   Receive confirmation message of successful purchase
*   Redirected to an order summary
*   Receive a confirmation email of successful purchase

_As a registered user I want the checkout to handle secure customer authentication when required (fail)_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the Shopping Bag page. Items are in the shopping bag.
*   Steps:
    *   Click on Secure Checkout button \
– – See a checkout form with order summary
    *   Fill in personal details
    *   Fill in Stripe authentication test card number 4000 0025 0000 3155
    *   Click Complete Order
    *   Click fail authentication

Expectation:



*   Redirected to checkout page with text below payment form stating the error

_As a registered user I want to be told if the payment fails_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the Shopping Bag page. Items are in the shopping bag.
*   Steps:
    *   Click on Secure Checkout button \
– – See a checkout form with order summary
    *   Fill in personal details
    *   Fill in Stripe authentication test card number 4000 0000 0000 9995
    *   Click Complete Order

Expectation:



*   Redirected to checkout page with text below payment form stating the error

_As a registered user I want my checkout details to be saved to my profile_



*   Pre-requisites: \
– – registered user is on desktop, logged in and on the Checkout page with items in shopping bag.
*   Steps:
    1. Complete delivery form
    2. Click ‘save this delivery information to my profile’ button
        1. Click Complete Order

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
    1. Update existing delivery info
    2. Click ‘save this delivery information to my profile’ button
    3. Click Complete Order

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
    1. Click on delete button \
Expectation:
*   Confirmation message stating product successfully deleted
*   A redirect to Gallery page
*   Deleted product is no longer displayed on Gallery page

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
    1. Click on delete button \
Expectation:
*   Confirmation message stating blog successfully deleted
*   A redirect to the Blogs page
*   Deleted blog post is no longer displayed on Blogs page

_As an admin I want to ensure the homepage always displays the top rated products (downgrade a top rated product)_



*   Pre-requisites: \
– – Admin is on desktop, logged in and has identified a change in one of the top rated products. This script works on homepage, Gallery page and product details page
*   Steps:
    4. Click on edit button under product to be changed \
– – See edit product form with current information included \
– – See alert message warning edit status is live
    5. Reduce product rating 
    6. Click Update Product button
    7. See Confirmation message stating product successfully updated and redirected to the updated product
    8. Click homepage link in navigation bar \
Expectation:
*   Amended product is no longer displayed on homepage and replaced by new top product

_As an admin I want to ensure the homepage always displays the top rated products (upgrade product currently not top rated)_



*   Pre-requisites: \
– – Admin is on desktop, logged in and has identified a product currently not top rated. This script works on Gallery page and product details page
*   Steps:
    9. Click on edit button under chosen product \
– – See edit product form with current information included \
– – See alert message warning edit status is live
    10. Increase product rating to co-align with the top products
    11. Click Update Product button
    12. See Confirmation message stating product successfully updated and redirected to the updated product
    13. Click Home link in navigation bar \
Expectation:
*   Amended product is displayed on homepage in top three products  \

</details>

### **Differences in content display across different devices**



*   Navigational bar:
    *   Desktop - Brand title, search box and navigational links all displayed in one row
    *   Tablet - Brand title top left corner, burger menu top right corner and search box centre. When burger menu is clicked the navigational links drop down to a row of six beneath the search box, centrally aligned
    *   Mobile - same set up as Tablet, however drop down displays in two rows of three.  
*   Home page:
    *   Desktop and Tablet - Products displayed horizontally in rows of three
    *   Mobile - Products displayed vertically one on top of another
*   Blogs:
    *   Desktop and Tablet - Blogs displayed horizontally in rows of two
    *   Mobile - Blogs displayed vertically one on top of another
*   Gallery:
    *   Desktop - Products displayed horizontally in rows of four
    *   Tablet - Products displayed horizontally in rows of two
    *   Mobile - Products displayed vertically one on top of another
*   Product Details:
    *   Desktop - Product image and location displayed on one half of screen with product details and interactive buttons on the other side
    *   Tablet and Mobile - Product image and location displayed above product details and interactive buttons
*   Profile Page:
    *   Desktop - Default delivery information displayed in one half of screen with order history on the other half
    *   Tablet and Mobile - Default delivery information displayed above order history
*   Shopping Bag:
    *   Desktop and Tablet - Product details and subtotal displayed in one row. total cost displayed bottom right above buttons to keep shopping or checkout
    *   Mobile - total cost, keep shopping and checkout buttons displayed centrally on separate rows. Summary of shopping bag contents and product image below, along with product details. At the bottom of the page is an upwards arrow which takes the registered user to the top of the screen.
*   Checkout:
    *   Desktop - Details, delivery information and payment form displayed on one half of the screen, with order summary on the other side
    *   Tablet and Mobile - Order summary, details, delivery information and payment form displayed one on top of another.
*   Order Information:
    *   Desktop and Tablet - Order information headings on one side of screen, with corresponding values on the other side in the corresponding rows
    *   Mobile - Order information display in one column, with values displayed directly beneath corresponding headings


### **Bugs highlighted by testing**



*    On the checkout page, the registered user's address is saved to the profile regardless of whether the checkbox was saved
    *   To be fixed for a future release
*   The quantity selector on the bag page does not limit between 1 (min) and 99 (max) as the product details page does
    *   To be fixed for a future release
*   The pluralize function was not working on the blog details page for like/likes. A simple fix of a typo in the template
*   Not all links has the CSS cursor added on, fixed as an oversight
*   During development the category name for snow themed products was amended from _ski_hill_ to _snow_ to be more inclusive. Upon testing it was discovered that this change had been applied to the local deployment, but not the remote deployment so the product geographical filter _snow _didn’t return any results . This was remedied by amending the category name in the admin panel of the remote deployment.


### **Code Validation**



*   I used the W3C HTML Validator tool to validate my HTML code. The W3C Validator tool doesn't recognise the Jinja templating, which resulted in it showing a lot of errors in relation to the Jinja code. This meant carefully going through such html files to ensure that they were formatted correctly.
*   I used the W3C CSS Validator tool to validate my CSS code.
*   I used the JSHint tool to validate my JavaScript syntax.
*   I used the Pep8 Online tool to validate my Python syntax. I had to update a number of lines that were too long and blank spaces I had initially missed.


## **Compatibility - TEST THIS AGAIN**

To ensure that the website is accessible and runs across different devices and browsers, I have tested it on the following:



*   Chrome
*   Safari
*   Firefox
*   Opera
*   Microsoft Edge


## **Deployment**

This project was developed using the GitPod IDE, committing to Git for every meaningful change and pushing commits to GitHub via the terminal Git commands. On GitHub I was able to view the Code Institute template recommended for GitPod use, clone it, and then create my own repository with the template. After this, it was possible to create a new workspace using GitPod.


### **Local Deployment**



*   In the terminal enter `git clone [https://github.com/jonwil91/milestone-4]` to make a clone of this repository. Alternatively, by clicking the green 'Clone or Download' you can download the file as a zip-file and upload it into your new workspace, please ensure that you unzip the file first.
*   In the terminal enter `cd milestone-4` (path to folder)
*   The next step is to create a ‘.env’, this will be an important file for safely storing your credentials. These can also be stored as GitPod environment variables if using the GitPod IDE.
*   In the terminal enter `pip3 install -r requirements.txt` to install necessary dependencies
*   In the terminal enter `python3 manage.py migrate` to create the database schema
    *   After this stage you ought to notice a db.sqlite3 database file has been created
*   Enter `python3 manage.py runserver` to expose the app to port 8000. Products will not yet be displayed
*   The next two inputs have to be entered in this order in the terminal:
    *   `python3 manage.py loaddata categories`
    *   `python3 manage.py loaddata products`
*   In the terminal enter `python3 manage.py createsuperuser` to create an admin account to access Django’s admin panel
*   In the terminal, in the following order enter
    *   `git add .`
    *   `git commit -m "[Insert message for commit]"`
    *   `git push`
    *   This will push and safely store all changes to GitHub

At this point the local deployment is functional, bar the checkout feature using Stripe. To add this functionality, sign up for an account with [Stripe](https://jbt.github.io/markdown-editor/www.stripe.com), collect the following variables to add to the ‘.env’ file



*   STRIPE_SECRET_KEY = Value
*   STRIPE_PUBLIC_KEY = Value
*   STRIPE_WH_KEY = Value

Please note that for testing the checkout feature using Stripe, the test card number is: 4242 4242 4242 (the CVC, expiry date and ZIP code can be any number)


### **Remote Deployment**

The deployed site can be found at: https://jw-photography.herokuapp.com



*   Ensure that you have Procfile created to tell Heroku the type of application using gunicorn and how to run it
*   Visit [Heroku](https://jbt.github.io/markdown-editor/%5Bwww.heroku.com%5D(www.heroku.com)), register and create a new app
*   In the deploy tab set GitHub as deployment method and search for repository (you will have to sign into GitHub if you are a new user)
    *   Click enable automatic deploys to push to Heroku master when pushing to GitHub
    *   In Resources tab, in the search bar, look for Heroku Postgres and select Hobby Dev - Free - update to remote database
*   In the terminal enter `heroku login -i` and enter your credentials
*   In the terminal enter `heroku git:remote -a [name of Heroku app]`
*   Initialise a new commit
    *   `git add .`
    *   `git commit -m "[git commit message]"`
    *   `git push`
    *   ``git push heroku master` if git push fails to push to Heroku automatically`
*   Create an AWS account, set up an S3 bucket, create a user and policy to authorise
    *   I selected London as the region which is written as ‘eu-west-2’ in the settings.py file which was created from the clone command
*   Using an email provider such as Gmail, set up a profile to access EMAIL_HOST_PASS and EMAIL_HOST_USER credentials
*   In Heroku settings, click Reveal Config Vars and add the following:
    *   AWS_ACCESS_KEY = Value
    *   AWS_SECRET_ACCESS_KEY = Value
    *   DATABASE_URL = Value
    *   EMAIL_HOST_PASS = Value
    *   EMAIL_HOST_USER = Value
    *   SECRET_KEY = Value
    *   STRIPE_SECRET_KEY = Value
    *   STRIPE_PUBLIC_KEY = Value
    *   STRIPE_WH_KEY = Value
    *   USE_AWS = True
*   The above variables, with the exception of USE_AWS ought to be saved in the settings.py file in the following format: *`AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', '')`
*   To make final migrations, in the terminal enter:
    *   `python3 manage.py makemigrations - `Create the migrations (generate the `SQL` commands)
    *   `python3 manage.py migrate - `Run the migrations (execute the `SQL` commands)
*   Once the Heroku build is migrated and completed you can open the app
*   Additional objects can be added to the app through the admin panel, and media saved in the S3 bucket


## **Credits**


### **Content**



*   The Checkout, Profiles and Bag apps were taken from Code Institute mini-project
*   Widgets.py files in Blog and Products app were taken from Code Institute mini-project
*   _like_view_ in Blog app was taken from Youtube [Codemy tutorial](https://www.youtube.com/watch?v=PXqRPqDjDgc&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=18)
*   _add_comment_ view in Blog app was inspired by Youtube [Coedmy tutorial](https://www.youtube.com/watch?v=OuOB9ADT_bo&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=34)
*   Change frame colour feature was inspired by Youtube [The Webshala](https://www.youtube.com/watch?v=lGNwc_DLRfw)
*   [Compress Jpg](https://compressjpeg.com/) used to compress images
*   Pagination inspired by Youtube video [Parwiz Forogh](https://www.youtube.com/watch?v=N_TWOfLlc7A)
*   [HeictoJPEG]([https://heictojpg.com/](https://heictojpg.com/)) used to convert HEIC wireframes to JPG format


### **Media**



*   All product images are owned by me
    *   _No Image_ available image was taken from [Google](https://www.google.com/search?q=no+image+available+image&tbm=isch&ved=2ahUKEwjggIKRuLbrAhXJuxoKHY43C9MQ2-cCegQIABAA&oq=no+image+available+&gs_lcp=CgNpbWcQARgCMgQIABBDMgQIABBDMgQIABBDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFDZfFjZfGDhiwFoAHAAeACAAUmIAUmSAQExmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=IQ9FX6DsHMn3ao7vrJgN&bih=978&biw=1920#imgrc=d2Y8RJMlsclozM&imgdii=KG6Rbsh8IbhRxM)
    *   Picture of camera in blog was was taken from [Electronics Frontier](https://www.electronicsfrontier.com/nikon-d3500-digital-slr-camera-af-p-18-55mm-f-3-5-5-6g-vr-lens-kit.html?utm_source=shopello_gb&utm_medium=cpo&utm_campaign=google+shopping+ads&utm_term=misc-16284&utm_content=Cj0KCQjw7ZL6BRCmARIsAH6XFDIbHOnDNTirkwUFL8m3GAQmN5stuvAeXLoPDpv3-OBvgqXPpi3nlrAaAqNiEALw_wcB%3B22%3B0)
*   Used [Compress Jpg](https://compressjpeg.com/) to compress product image files
*   Used [Mastering Markdown](https://jbt.github.io/markdown-editor/#ux) as a Markdown Editor


### **Acknowledgements**

A big thank you to my mentor, Gerry McBride for support and positive feedback throughout the project. A special thanks as well to Roz and Tom for continued support and all the Code Institute online support team for their patience and encouragement throughout the project.
