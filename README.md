# Alt Tech

This repository contains a collection of tools to automate
various functionality on Alt Tech media sites, such as Minds,
Gab, or GNU Social. Most of that functionality is wrapped into
Python classes that are meant to provide an easy to use
abstraction of each site's API.

## Installation

The API wrappers from the directory ``api_wrappers`` can each be
installed with the ``install.sh`` script from each top level.
Afterwards, one should be able to import each module from Python
like a regular module.

## Usage Example

```
from mindsapi import mindsapi

api = mindsapi.MindsAPI('username', 'password')
api.login()
api.post_custom(message='Test!')
```
