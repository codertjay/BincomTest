
### Activation Virtualenv

`pip -h`
`pip install virtualenv`
`virtualenv env`

## if you are using windows

`env\Scripts\activate.bat`

### else

`source env/bin/activate`

### installing packages ( make sure you are in the root folder)

`pip install -r  requirements.txt`

### Run Task on Windows

- (If on Mac ) celery -A BincomTest worker --loglevel=info
- (If on Windows) celery -A BincomTest worker -l info --pool=solo 
### open another tab

- `celery -A BincomTest beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`