# CASParser Demo

API Demo for [casparser](https://github.com/codereverser/casparser)

⭐ **Demo** :- https://cas.atomcoder.com  

## Dependencies
- backend
  - python >= 3.9
- frontend
  - node >= 12

## Setup

### Backend
1. Setup python virtualenv and install dependencies

- run 
  > chmod +x ./run.sh

  > ./run.sh

this will install these dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -U setuptools wheel pip
pip3 install -r requirements.txt
```
2. Deploy API
this has to be done in venv (the script takes care of it ;)
```
uvicorn app:app --reload
```

3. API curl calls
```js
curl --location --request GET 'http://127.0.0.1:8000/health'


curl --location --request POST 'http://127.0.0.1:8000/api/process' \
--form 'password="password"' \
--form 'cas=@"/Users/file/path/cams.pdf"'
```


### Frontend
1. Install dependencies from ./web
```
pnpm install
```
2. Run frontend
```
pnpm run dev
```
