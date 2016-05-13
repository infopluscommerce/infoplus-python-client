# infoplus-python-client
Infoplus is a cloud platform to manage your inventory, orders, warehouse, and shipments.

The Infoplus API exposes the full breadth and depth of the Infoplus platform to all clients.
With the Infoplus API, you can integrate Infoplus functionality into other platforms 
(e.g. your ERP, shopping cart, accounting system, etc.), enabling you to do, in your own platform, 
anything you can do in Infoplus. 

This repository is a native Python client for full access to the Infoplus API.

## Infoplus API Resources
The Resources listed below will provide all the information you need to integrate with the Infoplus API. 

### Developer's Home Page
https://www.infopluscommerce.com/developers/
* This site gives you an overview of the Infoplus API. 
* Get a general understanding of the API and quick steps on getting started. 

### Infoplus API Reference Site
http://developers.infopluscommerce.com/
* The Infoplus API is a modern JSON + REST API, and the API Reference Site is the complete documentation of all endpoints, resources, and fields available in the API. 
* Whether you're using the API directly over HTTPS, or if you're using a pre-built Client Library like this one, the API Reference Site gives you the specific details you need for each API call available, along with live demo capabilities.
* The API Reference Site also lets you request access to a free Demo Account to test out the API. 

### Have Questions?
* Read an [Overview of the Infoplus API](https://support.infopluscommerce.com/support/solutions/articles/11000010373)
* Get in touch with the [Infoplus Support Team](https://support.infopluscommerce.com/support/tickets/new)
* Visit the [Infoplus API Forum](https://support.infopluscommerce.com/support/discussions/forums/11000000138)

# Python Client Details

## Requirements.
Python 2.7 and later.

## Setuptools
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```

Or you can install from Github via pip:

```sh
pip install git+https://github.com/infopluscommerce/infoplus-python-client.git
```

To use the bindings, import the pacakge:

```python
import Infoplus
```

## Manual Installation
If you do not wish to use setuptools, you can download the latest release.
Then, to use the bindings, import the package:

```python
import path.to.Infoplus
```
