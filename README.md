

# MegaMillions Group

[![Build Status](https://travis-ci.org/dreardon/megamillions-group.svg?branch=master)](https://travis-ci.org/dreardon/megamillions-group)

MegaMillions Group is an application which tracks the Mega Millions drawing results against a group of tickets and players. 
Essentially, it is meant to track on ongoing office pool.
 It is built with [Python][0] using the [Django Web Framework][1].

## Installation

To set up a development environment quickly, first install Python. Then install and configure virtualenv.

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py makemigrations
    python manage.py migrate

Finally, after creating a Django super user, log in and add new lottery tickets to your profile.

### TODO

Create better administrative pages to add group players
Create better administrative pages to create tickets
Add the ability to deprecate group players and old tickets
