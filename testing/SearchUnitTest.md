# Search Unit Test Report
## Storefront by Fence
2016-11-23

Tests performed by *Ion Fong Chan*

###Definitions
- *DOMAIN* : A placeholder for whatever site the project is installed on. For the deployment server, 
*DOMAIN* = "http://fence.pythonanywhere.com"
- *EMPTY* : Without any input in the keyword input box
- *OTHER CATEGORIES OPTION* : One of the category options except "ALL" and "ALL CATEGORIES"
- *SEARCH PAGE* : *DOMAIN*/search
- *STRING* : A combination of symbols, spaces, and characters
- *WORD* : Combination of charcters without space beteen them such as "apple" and "web2py"


### Test 1: Search Keyword
| Keyword entered | Action |
| --- | --- |
| *`EMPTY`* | Redirect to the *SEARCH PAGE*.  Display a message "No Matched Product" |
| *`WORD`* | Redirect to the *SEARCH PAGE*. List all the product(s) whose name contains *WORD* without case sensitive.  The list of results are orderd by the latest created date and with maximum of 20 products per page. |
| *`STRING`* | Redirect to the *SEARCH PAGE*. List all the product(s) whose name contains *STRING* without case sensitive. The list of results are orderd by the latest created date and with maximum of 20 products per page. |

### Test 2: Search Option
| Option selected | Action |
| --- | --- |
| *`ALL or ALL CATEGORIES`* | Redirect to the *SEARCH PAGE*. Display the products that have the search keyword in name from all different categories. The list of results are ordered by the lastest created date and have maximum 20 products per page |
| *`OTHER CATEGORIES OPTION`* | Redirect to the *SEARCH PAGE*. Display all the product that have the search keyword in name from the selected category. The list of results are ordered by the lastest created date and have maximum 20 products per page |
