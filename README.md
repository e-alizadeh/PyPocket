# PyPocket

![](https://img.shields.io/badge/Project%20Status-Under%20Development-green)

[![Actions Status](https://github.com/e-alizadeh/pypocket/workflows/Build%20and%20Test/badge.svg?feature=master)](https://github.com/e-alizadeh/pypocket/actions)
[![PyPI version](https://badge.fury.io/py/pypocket.svg)](https://badge.fury.io/py/pypocket)
![MIT License](https://img.shields.io/badge/License-MIT-blueviolet)
[![Code Style: Black](https://img.shields.io/badge/Code%20style-black-black)](https://github.com/psf/black)
 

---
[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/dashboard?id=PyPocket)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=PyPocket&metric=coverage)](https://sonarcloud.io/dashboard?id=PyPocket)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=PyPocket&metric=security_rating)](https://sonarcloud.io/dashboard?id=PyPocket)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=PyPocket&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=PyPocket)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=PyPocket&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=PyPocket)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=PyPocket&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=PyPocket)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=PyPocket&metric=ncloc)](https://sonarcloud.io/dashboard?id=PyPocket)
---

A Python Package for GetPocket (https://getpocket.com). 
The Export option in Pocket will generate a dry html file containing only the saved article links. 
PyPocket library will generate a more sophisticated HTML report with given tags, the article title, time added. 
You can specify the number of articles you want to retrieve too (particularly useful if you have a large collection of saved articles).

More functionalies are under development like the ability to filter and export by tag(s), additional metadata, *etc*. 

Check the development roadmap for this project [here](https://github.com/e-alizadeh/PyPocket/projects/1). Feel free to request a new feature!


## Installation
```bash
pip install pypocket
```

## Library Requirements
- requests (`pip install requests`)
- dominate (`pip install dominate`)

---
## Prerequisite: Obtain Your Consumer Key & Access Token
In order to use PyPocket, you will need consumer_key and access_token for your Pocket. 
For the consumer_key, you can follow Step 1 of [Pocket Authentication API Documentation](https://getpocket.com/developer/docs/authentication)
to obtain your consumer_key. 

For obtaining your access_token, you can either follow the pocket documentation (above link) to get your access_token,
or use the `Auth` class available in this library for your convenience as below. 
```python
from pypocket.auth import Auth
auth = Auth(consumer_key="your_consumer_key")
# The following will automatically obtain a request_token and ask you to authorize it. 
auth.authorize_request_token_browser() 
```

The `auth.authorize_request_token_browser()` will open a webpage to getpocket.com website asking  you to authorize the token. 
Once, you authorize it. Then you can get your access token by running the following:
```python
access_token = auth.get_access_token() 
```
---
## Usage

```python
from pypocket import Pocket

p =  Pocket(
    consumer_key="your_consumer_key", 
    access_token="your_token", 
    html_filename="report"
)
p.to_html(num_post=10)
```
---


## New features in the pipeline
- Retrieve pocket contents according to given tags
- Modify the pocket contents properties
