# Storefront by *Fence*
A CMPS 115 Fall 2016 project at UC Santa Cruz.

Check us out at [PythonAnywhere](https://fence.pythonanywhere.com).

## Members
* Harjyot Bal
* Tommaso Bonato
* Ion Fong "Rory" Chan
* Brian Lederman
* August Valera

## Documentation
* Presentation: [Google Slides](https://docs.google.com/presentation/d/12FC7L3qjBPTURlRjZnUYxmHMhlFeNLSTxkpVp7d3uiE)/[PPTX](docs/Presentation.pptx)
* Release plan: [Web](docs/ReleasePlan.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/docs/ReleasePlan.md)
* Sprint 1
  * Plan: [Web](docs/Sprint1/Sprint1Plan.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/docs/Sprint1/Sprint1Plan.md)
  * Report: [Web](docs/Sprint1/Sprint1Report.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/docs/Sprint1/Sprint1Report.md)
* Sprint 2
  * Plan: [Web](docs/Sprint2/Sprint2Plan.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/docs/Sprint2/Sprint2Plan.md)
  * Report: [Web](docs/Sprint2/Sprint2Report.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/docs/Sprint2/Sprint2Report.md)
* Sprint 3
  * Plan: [Web](docs/Sprint3/Sprint3Plan.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/docs/Sprint3/Sprint3Plan.md)
  * Report: [Web](docs/Sprint3/Sprint3Report.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/docs/Sprint3/Sprint3Report.md)
* Scrum board: [Waffle.IO](https://waffle.io/Fence-UCSC/Storefront)
* System and Unit Test Report: [Web](docs/SysUnitTestReport.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/docs/SysUnitTestReport.md)
  * `/` (Homepage): [Web](testing/HomeUnitTest.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/testing/HomeUnitTest.md)
  * `/product/*` (Product pages and Adding a new product): [Web](testing/ProductUnitTest.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/testing/ProductUnitTest.md)
  * `/search/*` (Search bar and results): [Web](testing/SearchUnitTest.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/testing/SearchUnitTest.md)
  * `/store/*` (Store listing and Store profiles): [Web](testing/StoreUnitTest.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/testing/StoreUnitTest.md)
  * `/user/*` (Login and Editing profile): [Web](testing/LoginUnitTest.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/testing/LoginUnitTest.md)
  * Contacting seller: [Web](testing/ContactUnitTest.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/testing/ContactUnitTest.md)
  * Location display and updating: [Web](testing/LocationUnitTest.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/testing/LocationUnitTest.md)
  * Review display and posting: [Web](testing/ReviewUnitTest.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/testing/ReviewUnitTest.md)
* Known Problems Report: [Web](docs/KnownProbReport.md)/[PDF](https://gitprint.com/Fence-UCSC/Storefront/blob/master/docs/KnownProbReport.md)

## Installation
* Install Python and the [web2py](http://github.com/web2py/web2py) framework server application on the deployment service
  * For reference, we used the hosting service [PythonAnywhere](http://pythonanywhere.com) which automates the web2py installation process, and has a free plan for developers with minimal bandwidth/performance
* Clone the project in the `web2py/applications` directory with `git clone http://github.com/Fence-UCSC/Storefront web2py/applications/Storefront`
* Run web2py with `python web2py/web2py.py` and navigate to the `$HOST/Storefront` page, where $HOST is configured in the web2py settings
