# Overview
API developed with python + django. For company management in the shoe industry. [test developed for Huia]

# Requirements

* Python (3.8.3) [Installation](https://www.python.org/downloads/release/python-383/ "Installation") 
* Virtualenv (20.2.2) [Installation](https://virtualenv.pypa.io/en/latest/installation.html "Installation")
* Visual Studio Code (Recomended IDE) [Installation](https://code.visualstudio.com/ "Installation")

# Run project
* Git clone this repository.
* Open ide and project folder (vs used).
* At terminal: <br>
 ```
 $ pip install virtualenv
 $ virtualenv venv -p python
 $ ./venv/scripts/activate
 $ pip install -r requirements.txt
 $ cd huiatest
 $ python manage.py collectstatic
 $ python manage.py migrate
 $ python manage.py createsuperuser
 $ python manage.py runserver
 ```
* Access http://127.0.0.1:8000/ or http://localhost:8000/
* /login for authentication.

# Endpoints
More details are avalibe at http://localhost:8000/redoc/ or http://localhost:8000/swagger/ <br>
Manager are avalibe at http://localhost:8000/admin/
<br>
 **All GET methods don't list inactive items.**

Url | HTTP | Operation | Result
-- | -- |-- |--
`/`| GET | READ | List created urls.
`/auth/login` | POST | CREATE | A new access token is create for the logged user.
`/auth/logout` | POST | CREATE | User logout and disable the token.
`/user` | GET, PUT, PATCH | READ, CREATE, UPDATE | Obtains some informations of the logged user and allows to edit it.
`/password/change/`| POST | UPDATE | Updates the user's password.
`/client`| GET, POST | READ, CREATE | Gets all clients/ create a new one.
`/client/{pk}`| GET, PUT, PATCH, DELETE | READ, UPDATE, DELETE | Gets an client by id and allows to edit it.
`/quality-lot`| GET, POST | READ, CREATE | Gets all quality lots/ create a new one.
`/quality-lot/{pk}`| GET, PUT, PATCH, DELETE | READ, UPDATE, DELETE | Gets an quality lot by id and allows to edit it.
`/product`| GET, POST | READ, CREATE | Gets all products/ create a new one.
`/product/{pk}`| GET, PUT, PATCH, DELETE | READ, UPDATE, DELETE | Gets an product by id and allows to edit it.
`/order`| GET, POST | READ, CREATE | Gets all orders/ create a new one.
`/order/{pk}`| GET, PUT, PATCH, DELETE | READ, UPDATE, DELETE | Gets an order by id and allows to edit it.
`/order-list`| GET | READ | Gets all orders and allows to sort it by purchase date or total value. Also allows include or exclude inactive orders of the list.
`/order-list/{pk}`| GET | READ | Gets an order by id and allows to sort it by purchase date or total value. Also allows include or exclude inactive orders of the list.

# Usage
 All endpoints follow de same template. More details are avalibe at http://localhost:8000/redoc/ or http://localhost:8000/swagger/
 Manager are avalibe at http://localhost:8000/admin/
 
* **GET**: <br>
Exemple at http://localhost:8000/client/ <br>
Parameters: No parameters. <br>
Responses: 
```
 {
    "name": "Theo",
    "cpf": "49966688855",
    "birth_date": 06/06/2006,
    "inactive": false
}
```

* **GET (by id)**: <br>
Exemple at http://localhost:8000/client/{pk} <br>
Parameters: A unique integer value identifying this Client. <br>
Responses: 
```
 {
    "name": "Theo",
    "cpf": "49966688855",
    "birth_date": 06/06/2006,
    "inactive": false
}
```

* **POST**: <br>
Exemple at http://localhost:8000/quality-lot/ <br>
Parameters: 
```
 {
    "fabrication_date": "date",
    "quality": integer,
    "inactive": boolean
 }
```
 Responses: 
```
 {
    "id": 1,
    "fabrication_date": "2020-12-27",
    "quality": 2,
    "inactive": false
 }
```

* **PUT**: <br>
Exemple at http://localhost:8000/product/{pk} <br>
Parameters: <br>
 **A unique integer value identifying this Product (Id).**<br>
```
{
    "name": "TESTE",
    "description": "teste",
    "quality_lot": 1,
    "color": "Red",
    "price": "0.03",
    "inactive": false
 }
```
 Responses: 
```
 {
    "name": "TESTE",
    "description": "teste",
    "quality_lot": 1,
    "color": "Red",
    "price": "10.00",
    "inactive": false
}
```

* **DELETE**: <br>
Exemple at http://localhost:8000/order/{pk} <br>
Parameters: A unique integer value identifying this Product (Id).<br>
Responses: No Responses (if complete without errors)


## Report
Report urls: http://localhost:8000/order-list/ or http://localhost:8000/order-list/{pk} <br>

* **GET** <br>
Parameters: Ordering (Ex: http://localhost:8000/order-list/?ordering=total_value, http://localhost:8000/order-list/?ordering=purchase_date) <br>
Inactive (Ex: http://localhost:8000/order-list/?inactive=true) <br>
Page (A page number within the paginated result set. Ex: http://localhost:8000/order-list/?page=2) <br>
A unique integer value identifying this Order (if url is http://localhost:8000/order-list/{pk}). 
<br>
Responses: <br>

```
{
    "count": 6,
    "next": "http://localhost:8000/order-list/?page=2",
    "previous": null,
    "results": [
        {
            "id": 2,
            "client": {
                "name": "Client Test 1",
                "cpf": "49999999999",
                "birth_date": "2020-12-27",
                "inactive": false
            },
            "seller": {
                "id": 1,
                "password": "pbkdf2_sha256$216000$GJ0x4fB5WwVs$IEf2UFKXo1OkM32pazDJ2qfi9t7Vnr/mQ3STosMl79c=",
                "last_login": "2020-12-28T01:04:10.810039Z",
                "is_superuser": true,
                "username": "seller test",
                "first_name": "",
                "last_name": "",
                "email": "",
                "is_staff": true,
                "is_active": true,
                "date_joined": "2020-12-27T21:08:20.998319Z",
                "groups": [],
                "user_permissions": []
            },
            "products": [
                {
                    "name": "TESTE",
                    "description": "teste",
                    "quality_lot": 1,
                    "color": "Red",
                    "price": "10.00",
                    "inactive": false
                }
            ],
            "purchase_date": "2020-12-27",
            "total_value": "10.00",
            "inactive": false
        },
        {
            "id": 3,
            "client": {
                "name": "Client Test 2",
                "cpf": "12345678912",
                "birth_date": "2020-12-27",
                "inactive": false
            },
            "seller": {
                "id": 1,
                "password": "pbkdf2_sha256$216000$GJ0x4fB5WwVs$IEf2UFKXo1OkM32pazDJ2qfi9t7Vnr/mQ3STosMl79c=",
                "last_login": "2020-12-28T01:04:10.810039Z",
                "is_superuser": true,
                "username": "seller test",
                "first_name": "",
                "last_name": "",
                "email": "",
                "is_staff": true,
                "is_active": true,
                "date_joined": "2020-12-27T21:08:20.998319Z",
                "groups": [],
                "user_permissions": []
            },
            "products": [
                {
                    "name": "TESTE",
                    "description": "teste",
                    "quality_lot": 1,
                    "color": "Red",
                    "price": "10.00",
                    "inactive": false
                }
            ],
            "purchase_date": "2020-12-27",
            "total_value": "10.00",
            "inactive": false
        },
        {
            "id": 4,
            "client": {
                "name": "Client Test 3",
                "cpf": "78945612378",
                "birth_date": "2020-12-27",
                "inactive": false
            },
            "seller": {
                "id": 1,
                "password": "pbkdf2_sha256$216000$GJ0x4fB5WwVs$IEf2UFKXo1OkM32pazDJ2qfi9t7Vnr/mQ3STosMl79c=",
                "last_login": "2020-12-28T01:04:10.810039Z",
                "is_superuser": true,
                "username": "seller test",
                "first_name": "",
                "last_name": "",
                "email": "",
                "is_staff": true,
                "is_active": true,
                "date_joined": "2020-12-27T21:08:20.998319Z",
                "groups": [],
                "user_permissions": []
            },
            "products": [
                {
                    "name": "TESTE",
                    "description": "teste",
                    "quality_lot": 1,
                    "color": "Blue",
                    "price": "2.00",
                    "inactive": false
                }
            ],
            "purchase_date": "2020-12-27",
            "total_value": "2.00",
            "inactive": false
        },
        {
            "id": 5,
            "client": {
                "name": "Client Test 4",
                "cpf": "45678912356",
                "birth_date": "2020-12-27",
                "inactive": false
            },
            "seller": {
                "id": 1,
                "password": "pbkdf2_sha256$216000$GJ0x4fB5WwVs$IEf2UFKXo1OkM32pazDJ2qfi9t7Vnr/mQ3STosMl79c=",
                "last_login": "2020-12-28T01:04:10.810039Z",
                "is_superuser": true,
                "username": "seller test",
                "first_name": "",
                "last_name": "",
                "email": "",
                "is_staff": true,
                "is_active": true,
                "date_joined": "2020-12-27T21:08:20.998319Z",
                "groups": [],
                "user_permissions": []
            },
            "products": [
                {
                    "name": "TESTE",
                    "description": "teste",
                    "quality_lot": 1,
                    "color": "Blue",
                    "price": "2.00",
                    "inactive": false
                }
            ],
            "purchase_date": "2020-12-27",
            "total_value": "231232.00",
            "inactive": false
        }
    ]
}
```
