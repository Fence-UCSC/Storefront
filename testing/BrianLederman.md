# Maps and Home Unit Test Report
## Storefront by Fence
2016-11-23
Tests performed by Brian Lederman

Location Tests
### Test 1: Right click for location
1. Right click on location not already specially marked by Google (e.g. Porter College, University Santa Cruz...)
2. Right click on marked location
3. Right click outside of map

### Results 1
1. Marker is moved
2. Marker is not moved
3. Marker is not moved

### Test 2: Saving Marker Location
1. Move marker without pressing 'edit' button
2. Move marker pressing 'edit' and not pressing 'update'
3. Move marker pressing 'edit' and 'cancel' 
4. Move marker pressing 'edit' and refreshing
5. Move marker pressing 'edit' and 'update'

### Results 2
1. Marker is immovable
2. Marker location is not saved
3. Marker location is not saved
4. Marker location is not saved
5. Marker location is saved

### Test 3: Editing Marker
1. Is user's account
2. Is not user's account

### Results 3
1. Can move marker
2. Cannot move marker

Home Tests
### Test 1: Flavor Text
1. Not logged in
2. Logged in
3. Refresh Page [0-5]
4. Refresh Page [5-infinite]

### Results 1
1. Set 1 of flavor texts
2. Set 2 of flavor texts
3. Flavor texts cycle and change through
4. Flavor texts continue to cycle and change through

### Test 2: Items
1. Click on item
2. Resize page

### Results 2
1. Redirects to correct page
2. Page is responsive
