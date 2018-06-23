# Olympics-Medal-Table
## Getting started

### Open you terminal first

### 1. Create the virtual environment

virtualenv mypython

### 2. Activate the virtual environment

source mypython/bin/activate  (for Mac OS/Linux)

mypthon\Scripts\activate (Windows)

### 3. Clone the project

git clone https://github.com/prakashatul1/Olympics-Medal-Table.git

### 4. Go to project root

cd olympics_medal_table/

### 5. Install requirements.txt

pip install -r requirements.txt

### 6. Makemigrations and migrate

python manage.py makemigrations

python manage.py migrate

### 7. scrape the data to the database

python manage.py scrape_table

### 8. Run Server in local

python manage.py runserver

### 9. Open project in web browser

Copy paste this link in url ---->>  http://127.0.0.1:8000/

### 10. Login with credentials

username = moody
password = moodyanalytics

### 11. Checkout the table in db

you can view the table by clicking on the "Country" link

you click on any of the headers to sort the data.

### 12. Checkout the map

To view map copy paste this link in url ---->>  http://127.0.0.1:8000/map 

## Note: You can also do edit operation by click on the rank of the country on table and see the changes in the graph. 
