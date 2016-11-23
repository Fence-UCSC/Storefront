# Store Page Unit Test Report
## Storefront by Fence
2016-11-23
Tests performed by *August Valera*

### Test 1: URL Redirection

Definitions
- *DOMAIN* is a placeholder for whatever site the project is installed on. For the deployment server, *DOMAIN*="http://fence.pythonanywhere.com"
- *S* is the set of integers that correspond to a store id. For examples, if there are 4 stores, *S*={1, 2, 3, 4}.

| URL entered | Action |
| --- | --- |
| `*DOMAIN*/store` | Display list of all stores |
| `*DOMAIN*/store/${int in *S*}` | Display store profile page |
| `*DOMAIN*/store/${int not in *S*}` | Redirect to `*DOMAIN*/store` with error message "Store ${int} not found" |
| `*DOMAIN*/store/${not an integer}` | Redirect to `*DOMAIN*/store` with error message "Store ${int} undefined" |
