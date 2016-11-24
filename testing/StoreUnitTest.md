# Store Page Unit Test Report
## Storefront by Fence
2016-11-23

Tests performed by *August Valera*

### Component Store List/Profile: Test URL Redirection

- $DOMAIN is a placeholder for whatever site the project is installed on. For the deployment server, $DOMAIN="http://fence.pythonanywhere.com"
- $S is the set of integers that correspond to a store id. For examples, if there are 4 stores, $S={1, 2, 3, 4}.

| URL entered | Action |
| --- | --- |
| `$DOMAIN/store` | Display list of all stores |
| `$DOMAIN/store/${int in $S}` | Display store profile page |
| `$DOMAIN/store/${int not in $S}` | Redirect to `$DOMAIN/store` with error message "Store ${int} not found" |
| `$DOMAIN/store/${not an integer}` | Redirect to `$DOMAIN/store` with error message "Store ${int} undefined" |

### Component Store List/Profile: Test User Info (for both the all stores list and on each individual store profile)

- Display store.first_name and store.last_name on left side
- For each info in {store.email, store.city, store.phone}
  - If info is defined: Display tag on right side
  - Else: Do nothing (do not display that any tag)

### Component Store Profile: Test "Edit your profile" button on top right

- `$USERID` refers to the current signed in user's identifier, and is `None` if the user is not signed in
- `$STOREID` refers to the identifier of the current store profile page being viewed
- `$DISPLAY` determines whether the button "Edit your profile" on the top right is displayed on the page

| `$USERID != None` | `$USERID == $STOREID` | `$DISPLAY` |
| --- | --- | --- |
| `False` | N/A | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |