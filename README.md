# Receive and manage client orders

This application it's and example that how to make a simple application in Django framework

The application have:

 - Product management
 - Client orders
 - Endpoint

# Requirements

 - Pyhton 3
 - Django 2.1
 - SQLITE DB
You could use this github repository,  this repository have a Docker composition with all the necessary to run this project.

# Technical analysis

## DB Tables
### product
  

| Name         | Type                                          | Relation | Other |   |   |
|--------------|-----------------------------------------------|----------|-------|---|---|
| SerialNumber | CharField(max_length=60)                      |          |       |   |   |
| Name         | CharField(max_length=200)                     |          |       |   |   |
| Description  | CharField(max_length=1000)                    |          |       |   |   |
| Price        | DecimalField(max_digits=12, decimal_places=2) |          |       |   |   |

