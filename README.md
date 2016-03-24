# Doc-Certs
Doctors and their certified specialties, sub-specialties.

### Setup
Add login credentials as environmental variables:
* CERT_SITE_USER
* CERT_SITE_PW

Then:<br>
`sudo pip install --upgrade virtualenv`<br>
`virtualenv path/to/this/repo`<br>
`cd path/to/this/repo`<br>
`source bin/activate`<br>
`sudo pip install -r requirements.txt`

### Run the script
`python scraper.py`

### Exit virtual environment
`deactivate`
