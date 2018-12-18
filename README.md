# Receive and manage client orders

This application it's and example that how to make a simple application in Django framework

The application have:

 - Product management
 - Clients
 - Client orders
 - Endpoint

# Requirements

 - Pyhton 3
 - Django 2.1
 - SQLITE DB
 - Django rest framework
 - pip install requests
 
You could use this github repository: https://github.com/drl9319/django2X_withDocker, this repository have a Docker composition with all the necessary to run this project.

# Technical analysis

## DB Tables
### product
  

| Name         | Type                                          | Relation | Other |
|--------------|-----------------------------------------------|----------|-------|
| SerialNumber | CharField(max_length=60)                      |          |       |
| Name         | CharField(max_length=200)                     |          |       |
| Description  | CharField(max_length=1000)                    |          |       |
| Price        | DecimalField(max_digits=12, decimal_places=2) |          |       | 

### Client


| Name    | Type                                | Relation | Other |
|---------|-------------------------------------|----------|-------|
| Name    | CharField(max_length=200)           |          |       |
| NIF     | CharField(max_length=50)            |          |       |
| Country | CharField(max_length=1, choices=[]) |          |       |
| City    | CharField(max_length=200)           |          |       |
| Email   | CharField(max_length=200)           |          |       |

### SaleOrder


| Name     | Type                                | Relation | Other |
|----------|-------------------------------------|----------|-------|
| Date     | DateField                           |          |       |
| IdClient | ForeignKey                          | Client   |       |

### SaleOrderLine

| Name      | Type                                          | Relation  | Other |
|-----------|-----------------------------------------------|-----------|-------|
| IdSale    | ForeignKey                                    | SaleOrder |       |
| IdProduct | ForeignKey                                    | product   |       |
| Price     | DecimalField(max_digits=12, decimal_places=2) |           |       |
| Qty       | IntegerField(default=0)                       |           |       |

## Other project info

* **SuperUser** : admin
* **SuperUserEmail** : admin@admin.com
* **SuperUserPasword** : admin123

### Enter to admin Sale orders

URL: http://0.0.0.0:8000/admin/

### E-Mail send

This application have a send e-mail when the client sale is saved, to configure the exit e-mail server, you must go to setings.py and this is the config data:

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your@gmail.com'
EMAIL_HOST_PASSWORD = 'yourPasword'
EMAIL_USE_TLS = True
```
### Api Rest Info

The Api Rest was made with **Django REST Framework**.
If you wont to test this REST, could be use Postman and call to "http://127.0.0.1:8000/Product/" URL, this return data like this:

ScreenShot

This REST api haven't security because it's only an example, but Django REST Framework allow have several security types.

### Example to consume REST Api

http://0.0.0.0:8000/SaleOrdersExample/

### Load example data

This app have example data to refill with data de SQLITE DB. I use the fixtures like if i wont make a test, but only for have structured data and load this if you run this command: **python manage.py loaddata SaleOrdersExample/fixtures/products.json**

This data are in fixtures folder, and the format is JSON, but it's possible make this with YML for example.


