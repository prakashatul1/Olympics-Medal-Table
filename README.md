# Olympics-Medal-Table
## Getting started

### Open your terminal first

### 1. Create the virtual environment with python3

```
virtualenv -p python3 mypython
```

### 2. Activate the virtual environment

source mypython/bin/activate  (for Mac OS/Linux)

### 3. Clone the project

git clone https://github.com/prakashatul1/Olympics-Medal-Table.git

### 4. Go to project root

cd Olympics-Medal-Table/

### 5. Install all the dpendencies listed in requiremnets.txt

It is advisable to install all the dependencies seperately as different systems will support different version of liabraries 

### 6. Setting up the database

use this link ---->> https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04 for setting up the database if you are using ubuntu 14.04

### 7. Makemigrations and migrate

python manage.py makemigrations

python manage.py migrate

### 8. scrape the data to the database

python manage.py scrape_table

### 9. Create a superuser

python manage.py createsuperuser

### 10. Run Server in local

python manage.py runserver

### 11. Open project in web browser

Copy paste this link in url ---->>  http://127.0.0.1:8000/

### 12. Login with credentials

login with credentials you entered while creating superuser

### 13. Checkout the table in db

you can view the table by clicking on the "Country" link

you click on any of the headers to sort the data.

### 14. Checkout the map

To view map copy paste this link in url ---->>  http://127.0.0.1:8000/map 

## Note: You can also do edit operation by clicking on the rank of the country on table and see the changes in the graph. 
