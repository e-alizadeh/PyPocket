# PyPocket

![](https://img.shields.io/badge/Project%20Status-Under%20Development-green)

[![Actions Status](https://github.com/e-alizadeh/pypocket/workflows/Build%20and%20Test/badge.svg)](https://github.com/e-alizadeh/pypocket/actions)

![](https://github.com/e-alizadeh/pypocket/workflows/Main%20Workflow/badge.svg?branch=master)
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
[comment]: <> ([![SonarCloud]&#40;https://sonarcloud.io/images/project_badges/sonarcloud-white.svg&#41;]&#40;https://sonarcloud.io/dashboard?id=e-alizadeh_PyPocket&#41;)

A Python Package for GetPocket (https://getpocket.com)


## Installation
```bash
pip install pypocket
```

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


## New features in the pipeline
- Retrieve pocket contents according to given tags
- Modify the pocket contents properties
