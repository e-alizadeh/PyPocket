# PyPocket

![](https://img.shields.io/badge/Project%20Status-Under%20Development-green)


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