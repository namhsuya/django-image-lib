# django-image-lib
A django API that can be used to upload and fetch images.


### Build
git clone into your local machine

run the following commands to host it on your localhost:
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py migrate --run-syncdb`
- `python manage.py runserver`

### Usage
Access the api via the localhost (to test it)

Upload via this URL:
- http://127.0.0.1:8000/api/item/

Fetch image list for a single user via this URL:
- http://127.0.0.1:8000/api/item/?uploaded_by=test

### Example run
![alt text](https://github.com/namhsuya/django-image-lib/blob/master/test.png)
![alt text](https://github.com/namhsuya/django-image-lib/blob/master/test2.png)
