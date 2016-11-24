# Contact Unit Test Report
## Storefront by Fence
2016-11-23
Tests performed by *Ion Fong Chan*

### Definitions
- *OFFICIAL EMAIL* : storefront.fence@gmail.com
- *DOMAIN* : A placeholder for whatever site the project is installed on. For the deployment server, 
*DOMAIN* = "http://fence.pythonanywhere.com"
- *PRODUCT PAGE* : *DOMAIN*/product/${product_id}
- *SHOW INTEREST BUTTON* : a button to contact seller via email in *PRODUCT PAGE*

### Test 1: *SHOW INTEREST BUTTON* functionality
| Login Status | Action |
| --- | --- |
| *Not Logged In* | Redirect to the login page |
| *Logged In* | Display a email message form so the user can contact the seller. |

### Test 2: *SHOW INTEREST BUTTON* email form
| Title | Text | Action |
| --- | --- | --- |
| True | True | Email will be sent from the *OFFICIAL EMAL* to the seller. The email title is the title entered in the email form. The email content is the text from the form and the user contact email. |
| True | False | Display an error message: "Error! There was an error while sending your email. Plesae try again or contact the support" |
| False | True | Display an error message: "Error! There was an error while sending your email. Plesae try again or contact the support" |
| False | False | Display an error message: "Error! There was an error while sending your email. Plesae try again or contact the support" |

* True: if the user filled in any characters, numbers, symbols, or spaces
* False: if the content box is empty

### Test 3: *SHOW INTEREST BUTTON* Show/Hide 
| Product owned by the user | Show/Hide Button in *PRODUCT PAGE* |
| --- | --- |
| True | Hidden |
| False | Show |

