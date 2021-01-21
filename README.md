# PyPocket

![](https://img.shields.io/badge/Project%20Status-Under%20Development-green)

[![PyPI version](https://badge.fury.io/py/pypocket.svg)](https://badge.fury.io/py/pypocket)
![MIT License](https://img.shields.io/badge/License-MIT-blueviolet)
[![Code Style: Black](https://img.shields.io/badge/Code%20style-black-black)](https://github.com/psf/black)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=e-alizadeh_PyPocket&metric=security_rating)](https://sonarcloud.io/dashboard?id=e-alizadeh_PyPocket)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=e-alizadeh_PyPocket&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=e-alizadeh_PyPocket)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=e-alizadeh_PyPocket&metric=coverage)](https://sonarcloud.io/dashboard?id=e-alizadeh_PyPocket)

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