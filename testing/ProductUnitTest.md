# Product Page Unit Test Report
## Storefront by Fence
2016-11-23

Tests performed by *Tommaso Bonato*

### Test 1: Product URL Redirection

- `$URL` is the URL used to access the page, through any referrer
- `$DOMAIN` is a placeholder for whatever site the project is installed on. For the deployment server, `$DOMAIN="http://fence.pythonanywhere.com"`
- `$VALIDACTIONS` is the set of strings that correspond to a valid action to do within the product page
- `$VALIDID` is the set of integers that correspond to a valid product in the database
- `$LOGGED` is used to indicate if the user is logged in or not

| `$URL entered` | Action |
| --- | --- |
| `$DOMAIN/product AND NOT $LOGGED` | Display the Google Login page |
| `$DOMAIN/product AND $LOGGED` | Display the page to add a new product |
| `$DOMAIN/product/$VALIDID` | Redirect to `$DOMAIN/product/$VALIDID` and displays the product. Valid both if $LOGGEDIN or not" |
| `$DOMAIN/store/NOT$VALIDID` | Redirect to `$DOMAIN/index` with error message "Product ${input} does not exist" |

### Test 2: Behaviour when adding a new product

- On the left of the page the `$USER` can see the information that will be extracted from his profile and used when adding a new product. Once added, these informations will be visible to everyone.
- The table below explains the behaviour of the form with various inputs. Only two inputs are always required, `$NAME` and `$CATEGORY`, all the other ones are optional
- `$CATEGORY` and `$STATUS` are a dropdown menu where only one choice is allowed

| `$CATEGORY` | `$NAME` | `$DESCRIPTION` | `$PICTURE` | `$PRICE` | `$STATUS` | Result |
| --- | --- | --- | --- | --- | --- | --- |
| Valid Input | Valid Input | Valid Input | Valid input | Valid Input | Valid Input | Product added successfully |
| Empty Input | Empty Input | Valid Input | Valid input | Valid Input | Valid Input | Error while compiling the form since two required fields are empty |
| Valid Input | Valid Input | Valid Input | Non Image Input | Valid Input | Valid Input | Product added successully |
| Valid Input | Valid Input | Valid Input | Empty Input | Valid Input | Valid Input | Product added successully, image substituted with a default "No-Image" one |
| Valid Input | Valid Input | Valid Input | Non Image Input | Empty Input | Valid Input | Product added successully with a 0.00 price |
| Valid Input | Valid Input | Valid Input | Non Image Input | Non integer Input | Valid Input | The form while not accept non integer values as prizes and delete those characters in real time |

### Test 3: Behaviour when viewing a product (passive behaviour)

- If the `$USER` is `$LOGGEDIN` and viewing his/her own products, she will see all the information about it and two buttons in the top right corner that will allow him/her to `$EDIT` the product and mark it as sold (`$STATUS`)
- If the `$USER` is `$LOGGEDIN` and viewing another person products, he/she will be able to see a button called "Show Interest" (`$INTEREST`) where, if clicked, he/she will be able to contact the owner of the product. See the detailed Unit Test to more details on it
- `If the `$USER` is `NOT $LOGGEDIN` he/she will just be able to see all the product information and a button inviting him/her to login if he/she wants to contact the seller

### Test 4: Behaviour when viewing a product (active behaviour)
- If the `$USER` is `$LOGGEDIN` and viewing his/her own products, he/she will also be able to do some $ACTIONS

| `$ACTION` | Effect |
| --- | --- |
| Click on the `$EDIT` Button | This will display the exact same form as when adding a product with the difference that it is already compiled using the information from the current product and there is one more button to $DELETE the product |
| Click `$DELETE` while `$EDITING` a product | This will prompt an alert asking for confirmation and if the user agrees he/she will remove the item from the DataBase and he/she is redirect to the homepage |
| Click on `$MARK` (Mark as sold) | This will mark the product as sold removing it from the homepage and turning the price label red. It also displays a message saying " This product has been marked as sold, and is no longer visible to other users.|
| Click on `$MARK` (Mark as unsold) | This will mark the product as on-sale making it visible in the homepage and turning the label price green." |



