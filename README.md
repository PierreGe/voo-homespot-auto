# voo-homespot-auto
Automatic authentification to Voo Homespot and keep connection alive.


## Requirements
`python 2.7 or 3.x`

`requests`

`daemon` (optional)

## Install
In a virtualenv

`pip install -r requirements`

`mv config.py.sample config.py``

Write your user and password in the config.py file

## Run
In a shell

`python main.py`

As a daemon 

`python daemonvoo.py`
