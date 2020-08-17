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
- replace <username> with approriate user name, remove the angular brackets.
- http://127.0.0.1:8000/api/item/?uploaded_by=<username>

### Example run
- http://127.0.0.1:8000/api/item/?uploaded_by=test
!["Fetching all images uploaded by test"](test.jpg?raw=true)

- http://127.0.0.1:8000/api/item/?uploaded_by=test2
!["Fetching all images uploaded by test2"](test2.jpg?raw=true "Fetching all images uploaded by test2")
