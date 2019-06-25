 FORMAT: 1A

# obnk API

# Group Users

## Signup [/users/signup/]

### Signup [POST]

An authorization token is sent back.
Henceforth this token must be attached in the header in order to authenticate the user.

HEADER:
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
+ Request (application/json)

        {
           "email":"user@gmail.com",
           "password": "thepassword"
        }

+ Response 201 (application/json)

        {
            "token": "6a87d6c754dcd2fe5c9b1309ac35458049915278"
        }

## Login [/users/login/]

### Login [POST]

If the credentials are correct an authorization token is sent back.
Henceforth this token must be attached in the header in order to authenticate the user.

HEADER:
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
+ Request (application/json)

        {
           "email":"user@gmail.com",
           "password": "thepassword"
        }

+ Response 201 (application/json)

        {
            "token": "6a87d6c754dcd2fe5c9b1309ac35458049915278"
        }


## User Profile [/users/profiles/]

### Update Profile [PATCH]

Updates basic information for the authenticated user. This can be used to change password as well.

---
**Attributes:**
- `tradingPreferences` (dictionary): money[allow trade your products with money], allCategories[allow to trade your products for all kind of products], productCategories [allow to trade your products for all products matching with the provided categories]
---

+ Request (application/json)

            {
                "password": "New password",
                "firstName": "First",
                "lastName": "Last",
                "email": "user@gmail.com",
            }

            No one of these fields are mandatory, it's possible to update just 1 field.

+ Response 200 (application/json)

        {
            "uuid": "c631b233-a154-4327-863f-f60ac184ea54",
            "email": "pau.gimo@gmail.es",
            "firstName": "UserFirst",
            "lastName": "UserLast",
        }

### Get profile [GET]

Get own profile

+ Response 200 (application/json)

        {
            "uuid": "c631b233-a154-4327-863f-f60ac184ea54",
            "email": "pau.gimo@gmail.es",
            "firstName": "Pau",
            "lastName": "Giralt",
        }

## Get specific user's profile [/users/profiles/{user_uuid}/]


### Get specific user's profile [GET]

+ Response 200 (application/json)

        {
            "uuid": "c631b233-a154-4327-863f-f60ac184ea54",
            "email": "user@gmail.com",
            "firstName": "James",
            "lastName": "Ford",
        }

# Group Financials

## Transfer [/financials/transfers/]

### Transfers [POST]

Transfer `transfer_amount` from source user to target user if there are enough funds. If the transfer is successful the current account balance of the source user is returned.


+ Request (application/json)

        {
          "source_user": "1b7fa5fc-1f8d-490d-8171-1ddea31dcbef",
          "target_user": "718304a1-121f-411c-9e79-5fbe32df27ac",
          "transfer_amount": 52
        }

+ Response 201 (application/json)

        {
            "currentBalance": "48"
        }
