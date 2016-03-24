# Doc-Certs
Doctors and their certified specialties, sub-specialties.

### Setup
Add login credentials as environmental variables:
* CERT_SITE_USER
* CERT_SITE_PW

Then:
`sudo pip install --upgrade virtualenv`
`virtualenv path/to/this/repo`
`cd path/to/this/repo`
`source bin/activate`
`pip install -r requirements.txt`

### Run the script
`python scraper.py`

### Exit virtual environment
`deactivate`
