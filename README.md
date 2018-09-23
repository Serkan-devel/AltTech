# Alt Tech

This repository contains a collection of tools to automate
various functionality on Alt Tech media sites, such as Minds,
Gab, or GNU Social. Most of that functionality is wrapped into
Python classes that are meant to provide an easy to use
abstraction of each site's API.

## Installation

The API wrappers from the directory api_wrappers can each be
installed with the ``install.sh`` script from each top level.

## Usage Example

```
api = mindsapi.MindsAPI('username', 'password')
api.login()
api.post_custom(message='Test!')
```
