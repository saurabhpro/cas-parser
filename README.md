# CASParser Demo

[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub](https://img.shields.io/github/license/codereverser/casparser)](https://github.com/codereverser/casparser/blob/main/LICENSE)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/casparser)

Parse Consolidated Account Statement (CAS) PDF files generated from CAMS/KFINTECH


API Demo for [casparser](https://github.com/codereverser/casparser)

⭐ **Demo** :- https://cas.atomcoder.com  

## Dependencies
- backend
  - python >= 3.8
- frontend
  - node >= 12

## Setup

### Backend
1. Setup python virtualenv and install dependencies

- run 
  > chmod +x ./run.sh

  > ./run.sh

this will install these dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -U setuptools wheel pip
pip3 install -r requirements.txt
```
2. Deploy API
this has to be done in venv (the script takes care of it ;)
```bash
uvicorn app:app --reload
```

3. API curl calls
```bash
curl --location --request GET 'http://127.0.0.1:8000/health'


curl --location --request POST 'http://127.0.0.1:8000/api/process' \
--form 'password="password"' \
--form 'cas=@"/Users/file/path/cams.pdf"'
```


### Frontend
1. Install dependencies from ./web
```bash
pnpm install
```
2. Run frontend
```bash
pnpm run dev
```


### Good reads 
- https://www.howtogeek.com/427982/how-to-encrypt-and-decrypt-files-with-gpg-on-linux/
- https://medium.com/@shay.palachy/temp-environment-variables-for-pytest-7253230bd777

saurabh.kumar@C02D70TBMD6N cas-parser % tar -czvf files.tar files/    
saurabh.kumar@C02D70TBMD6N cas-parser % gpg -r saurabhk1511@gmail.com  -o files.enc -e files.tar

saurabh.kumar@C02D70TBMD6N cas-parser % gpg -q --batch --yes -d --passphrase="battlestar75" \
    -vo tests/files.tar tests/files.enc
saurabh.kumar@C02D70TBMD6N cas-parser % tar -xvf tests/files.tar -C tests/