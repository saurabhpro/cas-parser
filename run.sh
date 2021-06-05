#!/bin/bash

python3 -m venv venv                    # setup virtual env
set -e
source venv/bin/activate                # To activate the virtual env

pip3 install -U setuptools wheel pip    # install
pip3 install -r requirements.txt

## ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface 
## between async-capable Python web servers, frameworks, and applications.
uvicorn app:app --reload                # depoy api through ASGI server.

deactivate                              # To deactivate the virtual env