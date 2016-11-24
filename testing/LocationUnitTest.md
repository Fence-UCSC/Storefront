# Location (Map Display) Unit Test Report
## Storefront by Fence
2016-11-23

Tests performed by *Brian Lederman*

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
