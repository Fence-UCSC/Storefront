Login Functionality Unit Test Report
## Storefront by Fence
2016-11-23

Tests performed by *Harjyot Bal*

### Test 1: Shows create new user functionality using google account
1. Allows you to select google account rather it would be using gmail domain or ucsc.edu domain
2. Displays name of the user from the google account
3. Allows you to only edit your content

### Result 1:
1. User name is displayed
2. Accepts gmail and ucsc.edu domain since they are both google accounts
3. User can only perform certain task if logged in
4. Takes user straight to sell's portion of the site if new user.

### Test 2: Allows user to login using the login button from the welcome homepage
1. Asks for google account
2. Signs in as the user
3. Allows you to only edit save content from that account

### Result 2:
1. Accepts both gmail and ucsc.edu domain
2. Displays user's name
3. Saves the content from the last time a user logged in
4. Allows only the user to edit content in the profile
5. Takes user straight to sell's portion of the site if new user.


### Test 3: Allows user to login using the task bar on the right hand side
1. Asks for google account
2. Signs in as the user
3. Allows you to only edit save content from that account

### Result 3:
1. Accepts both gmail and ucsc.edu domain
2. Displays user's name
3. Saves the content from the last time a user logged in
4. Allows only the user to edit content in the profile

### Test 4: Allows user to sign out
1. User is able to sign out
2. Does not display username 
3. Cannot edit any content 

### Result 4
1. User can log out successfully 
2. No longer can change anything related to the profile
3. No name is shown on the welcome page

###Test 5: User attempts to click sell without logging in
1. Can not be able to make a sell post

### Result 5
1. Ask the user to sign in or link a google profile before proceeding 


