# Review System Unit Test Report
## Storefront by Fence
2016-11-23

Tests performed by *Harjyot Bal*

### Test 1: Allows user to post 
1. Allows to rate a store with a 5 star rating
2. Write content

### Result 1:
1. Only allows to rate with whole stars instead of using partial rating
2. Contented is posted
3. Displays who wrote the review

### Test 2: Allows one user review per store
1. Allows only one review from the user per store
2. Users have control to change post

### Result 2:
1. One review per user
2. When logged in the user has the option to delete the review and repost but no functionality to actually edit

### Test 3: When are users allowed to post reviews 
1. Users are unable to post a review for their own store when logged in
2. Users are unable to post reviews when not logged in

### Result 3:
1. No option to add post is given if user is on their own store
2. No option to add post for any store is given if user is not logged in to their accounts

### Test 4: Overall store ratings
1. Calculates the average rating for a user's store page

### Result 4:
1. Calculates rating depending on the number of stars and the amount of reviews that were post. If one user gave a 5 star and another gave 3 stars the average rating of the overall store is 4 stars

### Test 5:Post organization and information displaying
1. Reviews are post based on time
2. Displays who and when

### Result 5:
1. Review post are order based on most recent with the most recent posted on top
2. Displays the username of the critic 
3. Displays how long was this post up. Normally displays hours and days since posted than keeping track of actual time
4. No actual date is displayed 



