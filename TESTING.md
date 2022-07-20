# Testing 

## Validator Testing

### HTML Validation
All HTML pages were tested using [W3C Markup Validation](https://validator.w3.org/). 
- One warning was displayed on all pages. This refers to the section element that holds the flash messages.

<details><summary><b>HTML validation images below</b> (click to expand)</summary>

![HTML Validation of Home](cabinlove/static/images/testing_images/cabinshtml.png)
![HTML Validation of Locations](cabinlove/static/images/testing_images/locationshtml.png)
![HTML Validation of Registration](cabinlove/static/images/testing_images/registerhtml.png)
![HTML Validation of Login](cabinlove/static/images/testing_images/loginhtml.png)
![HTML Validation of I want to go there](cabinlove/static/images/testing_images/wanttogohtml.png)
![HTML Validation of Add cabin](cabinlove/static/images/testing_images/addcabinhtml.png)
![HTML Validation of Edit cabin](cabinlove/static/images/testing_images/editcabinhtml.png)
![HTML Validation of Add location](cabinlove/static/images/testing_images/addlocationhtml.png)
![HTML Validation of Add location](cabinlove/static/images/testing_images/editlocation.png)

</details>

### CSS Validation
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to test the style.css file. No changes were required.

![CSS validator](cabinlove/static/images/testing_images/css.png)

### JavaScript Validation
[JSHint Validator](https://jshint.com/) was used to validate all JavaScript files. 

![Javascript validator](cabinlove/static/images/testing_images/javascript.png)

### Python Validation
[PEP8 Online](http://pep8online.com/) validator was used to test the run.py file.

![PEP8 online validation](cabinlove/static/images/testing_images/python.png)

### Accessibility
The site achieved a Lighthouse accessibility score of 100% which confirms that the website is accessible.

![PEP8 online validation](cabinlove/static/images/testing_images/accessibility.png)


## Responsiveness Testing

- The site was tested on various devices such as desktop, laptops and mobiles to ensure responsiveness. The website performed as intended. The responsive design was also checked using Chrome Developer Tools across multiple devices.

<details><summary><b>Responsiveness testing</b> (click to expand)</summary>

Desktop view

![Desktop size](cabinlove/static/images/testing_images/large_chrome.png)

Tablet view

![Tablet size](cabinlove/static/images/testing_images/medium_edge.png)

Mobile view

![Mobile size](cabinlove/static/images/testing_images/small_mozilla.png)

</details>

## Browser Testing

- The site was tested on different browsers (Google Chrome, Firefox, Microsoft Edge) without issues.

<details><summary><b>Browser testing</b> (click to expand)</summary>

Google Chrome

![Google Chrome](cabinlove/static/images/testing_images/large_chrome.png)

Microsoft Edge

![Microsoft Edge](cabinlove/static/images/testing_images/medium_edge.png)

Mozzilla Firefox

![Mozilla Firefox](cabinlove/static/images/testing_images/small_mozilla.png)

</details>

## Manual Testing

Throughout development manual testing was carried out, in addition to futher testing at the end of the project.

- Navbar
    - The navbar links take user to relevant pages
- Brand logo
    - Brand logo takes user back to the Home page
- Social media
    - The social media links open in a seperate tab to relevant site
- Home
    - Home page displays all the cabins. Those who are registered users can add new cabins. For users who created the cabins Edit and Delete buttons are displayed.
- Add cabin
    - Form tested through validator. It highlights to the user what is required if it is not filled in correctly.
    - Once created it takes back to the cabins page.
- Edit cabin
    - Form tested through validator. It highlights to the user what is required if it is not filled in correctly.
    - Once edited it takes back to the cabins page.
- Delete cabin 
    - This function works well. First it asks the user if they really want to delete the cabin.
- Locations
    - The Locations page displays all the locations. Only the admin can add new locations and edit or delete existing locations.
- Add location
    - Form is validated. Once created it takes back to the Locations page.
- Edit location
    - Form is validated. Once edited it takes back to the locations page.
- I want to go there button
    - I want to go there button works well. Once clicked it takes the user to a new page where the cabins are listed by the location.
- Register Form
    - Form is validated. It highlights to the user what is required if it is not filled in correctly.
    - Once registered takes user to their profile page
- Login Form
    - Exisitng users can easily log into their profile
    - If successful, takes users to their profile and welcome message displayed
    - If unsuccessful a flash message will appear prompting users that password and or username is incorrect
- Logout
    - Takes back the user to the Log in page.
    - Once logged out user is not able to see the Add cabin, Edit cabin, Delete cabin functions.

## Unfixed Bugs

There are no unfixed bugs that I am aware of.

## User story testing

As first-time or casual user (as someone who has not registered):

- As an user I want to understand the main purpose of the website easily.

![Welcome message](cabinlove/static/images/testing_images/purpose.png)

- As an user I want to be able to navigate throughout the site.

![Navbar](cabinlove/static/images/readme_images/navbar_notloggedin.png)

- As an user I want to enjoy nice and clean design and style that is inline with the subject of the site.

![Design](cabinlove/static/images/readme_images/home.png)

- As an user I want to browse a variety of cabins all around the world.
- As an user I want to be able to view cabins without having to create an account.

![Browse cabins](cabinlove/static/images/testing_images/allcabins.png)

- As an user I want to list location specific cabins.

![I want to go there button](cabinlove/static/images/readme_images/want_to_go.png)

- As an user I want the option to register for an account, if I want to return later.

![New account](cabinlove/static/images/readme_images/register.png)

As a returning or registered user:

- As an user I want to log into my account.

![Login](cabinlove/static/images/readme_images/login.png)

- As an user I want to log out from my account.

![Logout](cabinlove/static/images/testing_images/logout.png)

- As an user I want to create my own cabins.

![New cabin](cabinlove/static/images/readme_images/newcabin.png)

- As an user I want to edit the cabins I have added.
- As an user I want to delete the cabins I have added.

![Edit and delete cabin](cabinlove/static/images/readme_images/edit_delete.png)
![Edit cabin](cabinlove/static/images/readme_images/editcabin.png)

- As an user I want to contact and follow the website via social media.

![Social media](cabinlove/static/images/testing_images/socialmedia.png)

As admin:

- As admin I want to edit my own cabins.

![Edit cabin](cabinlove/static/images/testing_images/editcabin.png)

- As admin I want to add new cabins.

![New cabin](cabinlove/static/images/readme_images/newcabin.png)

- As admin I want to add new locations.

![New location](cabinlove/static/images/readme_images/newlocation.png)

- As admin I want to edit existing locations.

![Edit location](cabinlove/static/images/readme_images/editlocation.png)

- As admin I want to delete existing locations.

![Delete location](cabinlove/static/images/testing_images/locations_delete.png)
