# Store Page Unit Test Report
## Storefront by Fence
2016-11-23

Tests performed by *August Valera*

### Component Store List/Profile: Test URL Redirection

- `$URL` is the URL used to access the page, through any referrer
- `$DOMAIN` is a placeholder for whatever site the project is installed on. For the deployment server, `$DOMAIN="http://fence.pythonanywhere.com"`
- `$VALIDIDS` is the set of integers that correspond to a valid store id. For example, if there are 4 stores, `$VALIDIDS={1, 2, 3, 4}`.

| `$URL entered` | Action |
| --- | --- |
| `$DOMAIN/store` | Display list of all stores |
| `$DOMAIN/store/${int in $VALIDIDS}` | Display store profile page |
| `$DOMAIN/store/${int not in $VALIDIDS}` | Redirect to `$DOMAIN/store` with error message "Store ${int} not found" |
| `$DOMAIN/store/${input not an integer}` | Redirect to `$DOMAIN/store` with error message "Store ${input} undefined" |

### Component Store List/Profile: Test User Info (for both the all stores list and on each individual store profile)

- Display `$NAME` of seller on left side of profile page
- For each of store's {`$EMAIL`, `$CITY`, `$PHONE`}
  - If defined: Display tag with on click action (tested below) on right side of profile page
  - Else: Do nothing (do not display that any tag)

| Information Provided | On-Click Action |
| --- | --- |
| `$EMAIL` | `mailto:$EMAIL` |
| `$PHONE` | `tel:$PHONE` |
| `$CITY` | `maps.google.com/?q=$CITY` |

### Component Store Profile: Test Responsive Design

- `$WIDTH` refers to the width of the browser window
- `$GRID` display style shows each module {"User Info", "Location", "Reviews", "Recent Products"} in
  a 4 panel square grid, with "User Info" in top left, "Location" in top right, etc.
- `$LIST` display style shows each module one after the other in a list format, suitable for
  mobile devices

| `$WIDTH` | Page Display Style |
| --- | --- |
| `< 992px` | $LIST |
| `>= 992px` | $GRID |

### Component Store Profile: Test "Edit your profile" button on top right

- `$USERID` refers to the current signed in user's identifier (integer), and is `None` if the user is not signed in
- `$STOREID` refers to the identifier of the current store profile page being viewed
- `$DISPLAY` determines whether the button "Edit your profile" on the top right is displayed on the page

| `$USERID != None` | `$USERID == $STOREID` | `$DISPLAY` |
| --- | --- | --- |
| `False` | `N/A` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |

### Component Store Profile: Test "Recent products" limit 5

- `$LENGTH` refers to the amount of products currently shown in the recent
  products list

| `$LENGTH` | Display of recent products list |
| --- | --- |
| `=0` | Blue info bar with message "This user has not posted any products." |
| `>0` and `<=5` | Displays list of `$LENGTH` products, with most recent on top |
| `>5` | Displays a list of `5` products, with most recent on top |

- `$NEWPRODUCT` refers to a product that has been just added by the user whose profile is being viewed
- `$OLDESTPRODUCT` refers to the oldest product in the set of displayed products on the profile page

| `$LENGTH` | Behavior when adding `$NEWPRODUCT` |
| --- | --- |
| `=0` | Blue info bar disappears and is replaced with `$NEWPRODUCT` |
| `>0` and `<=5` | `$NEWPRODUCT` is appended to top of list |
| `>5` | `$NEWPRODUCT` is appended to top of list, and `$OLDESTPRODUCT` is removed from list |

Note that on the product profile page, there are two additional components *Location (Map)* and *Reviews* that are displayed, however, these components are tested separately.
