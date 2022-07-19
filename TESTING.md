# Testing 

## Validator Testing 

### HTML Validation
All HTML pages were tested using [W3C Markup Validation](https://validator.w3.org/). 
- One warning was displayed on all pages. This refers to the section element that holds the flash messages. Please see below the examples for the HTML validation.

![First example of HTML Validation](cabinlove/static/images/cabinshtml.png)
![Second example of HTML Validation2](cabinlove/static/images/locationshtml.png)
![Third example of HTML Validation](cabinlove/static/images/registerhtml.png)

### CSS Validation
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to test the style.css file. No changes were required.

![CSS validator](cabinlove/static/images/css.png)

### JavaScript Validation
[JSHint Validator](https://jshint.com/) was used to validate all JavaScript files. 

![Javascript validator](cabinlove/static/images/javascript.png)

### Python Validation
[PEP8 Online](http://pep8online.com/) validator was used to test the run.py file.

![PEP8 online validation](cabinlove/static/images/python.png)

### Accessibility
The site achieved a Lighthouse accessibility score of 100% which confirms that the website is accessible.

![PEP8 online validation](cabinlove/static/images/accessibility.png)


## Responsiveness Testing

- The site was tested on various devices such as desktop, laptops and mobiles to ensure responsiveness. The website performed as intended. The responsive design was also checked using Chrome Developer Tools across multiple devices.

<details><summary><b>Responsiveness testing</b> (click to expand)</summary>

Desktop view

![Desktop size](cabinlove/static/images/large_chrome.png)

Tablet view

![Tablet size](cabinlove/static/images/medium_edge.png)

Mobile view

![Mobile size](cabinlove/static/images/small_mozilla.png)

</details>

## Browser Testing

- The site was tested on different browsers (Google Chrome, Firefox, Microsoft Edge) without issues.

<details><summary><b>Browser testing</b> (click to expand)</summary>

Google Chrome

![Google Chrome](cabinlove/static/images/large_chrome.png)

Microsoft Edge

![Microsoft Edge](cabinlove/static/images/medium_edge.png)

Mozzilla Firefox

![Mozzilla Firefox](cabinlove/static/images/small_mozilla.png)

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

## User story testing
