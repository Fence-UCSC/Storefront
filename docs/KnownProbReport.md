# Working Prototype Known Problems Report
## Storefront by Fence
2016-11-23

### List of Functions Not Working Properly
- On store profile ($DOMAIN/store/$ID), if site is deployed on non root ($DOMAIN/Storefront/default/store/$ID or other) and user has provided a city, the Google Maps link may not redirect properly (404). This is a result of the Python URL() function resolving unexpectedly.
- On store profile ($DOMAIN/store/$ID), if store has not provided a geolocation, map displays a warning but still defaults to UC Santa Cruz.
- On store profile ($DOMAIN/store/$ID), the store location map can only function correctly in Chrome browser. If the user is using Firefox, Edge , or other browser, the store location map may not shows up in the page.
- When adding a review, if you click on a star rating and then drag downward, the star indicator does not display (light up). However, the selected value persists, affecting visibility but not performance.
