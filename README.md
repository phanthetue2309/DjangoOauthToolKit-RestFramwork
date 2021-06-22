
### First App Test 
- Client id : ```BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu```
- Client secret : ```FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl```
- Client type : ```Confidential```
- Authorization Grant Type : ```password```

#### Remember something :
- Application and User is : 
    + One user have many applications
    

- Run in cmd : 
    ```
  
    curl -X POST -d "grant_type=password&username=tuepro123@gmail.com&password=Thetue2309" -u"BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu:FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl" http://localhost:8000/o/token/
    ```  
- Get access token : 
    ```
    {
        "access_token": "t4waPk5NKpnzoskN380YolhQKHIclY", 
        "expires_in": 36000, 
        "token_type": "Bearer", 
        "scope": "read write groups", 
        "refresh_token": "NijnaCmrSuLfbp0GvKsM9T9e6roq4S"
    }
    ```
- Then use this : 
    ```
    curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/users/
    curl -H "Authorization: Bearer t4waPk5NKpnzoskN380YolhQKHIclY" http://localhost:8000/users/
    ```

- Then get this : 
    ```
    [
        {
            "username":"tue",
            "email":"tuepro123@gmail.com",
            "first_name":"","last_name":""
        },
        {
            "username":"TestUser0",
            "email":"",
            "first_name":"",
            "last_name":""
        },
        {
            "username":"TestUser1",
            "email":"",
            "first_name":"",
            "last_name":""
        },
        {
            "username":"TestUser2",
            "email":"",
            "first_name":"",
            "last_name":""
        }
    ]

    ```
  
- Running with one user : 
    ```
    curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/users/1/
    curl -H "Authorization: Bearer t4waPk5NKpnzoskN380YolhQKHIclY" http://localhost:8000/users/1/
    ```
  
- Running with group : 
    ```
    curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/groups/
    curl -H "Authorization: Bearer NP5MR1MNjzv39R6pZ4VFdbL7Yyscmz" http://localhost:8000/groups/
    ```
- Result : [{"name":"Admin"},{"name":"Leader"}]

- Create a new user : 
    ```
    curl -H "Authorization: Bearer <your_access_token>" -X POST -d"username=foo&password=bar" http://localhost:8000/users/
    curl -H "Authorization: Bearer NP5MR1MNjzv39R6pZ4VFdbL7Yyscmz" -X POST -d"username=foo&password=bar" http://localhost:8000/users/

    ```
  + So you will have an account : 
    + username : foo
    + pass : bar
    
- Refresh access token : 
    ```
    curl -X POST -d "grant_type=refresh_token&refresh_token=<your_refresh_token>&client_id=<your_client_id>&client_secret=<your_client_secret>" http://localhost:8000/o/token/
    curl -X POST -d "grant_type=refresh_token&refresh_token=hixOU41SeEKnJVJ7QH8Zkw1cYaruBJ&client_id=BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu&client_secret=FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl" http://localhost:8000/o/token/

    ```
  
- now you have new access : 
    ```
    {"access_token": "IxOemwptYBSdhYqVC2Fv8eMCSG7z2M", "expires_in": 36000, "token_type": "Bearer", "scope": "read write groups", "refresh_token": "wKigOrENnon23EQSFdKPWemqT9p44o"}
    ```

##  Testing Restricted Access

-  Try to access resources using a token with a restricted scope adding a scope parameter to the token request
    ```
    curl -X POST -d "grant_type=password&username=<user_name>&password=<password>&scope=read" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
    curl -X POST -d "grant_type=password&username=tuepro123@gmail.com&password=Thetue2309&scope=read" -u"BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu:FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl" http://localhost:8000/o/token/

    ```
   
- Result : ```{"access_token": "nujCtO6fgG73RNkeNqFqOD2WqvQ3n2", "expires_in": 36000, "token_type": "Bearer", "scope": "read", "refresh_token": "fCHisuWHnvoUCmANxXVXxBegIsfi8n"}```
  
- Group Scope : 
    ```
    curl -H "Authorization: Bearer nujCtO6fgG73RNkeNqFqOD2WqvQ3n2" http://localhost:8000/users/
    curl -H "Authorization: Bearer nujCtO6fgG73RNkeNqFqOD2WqvQ3n2" http://localhost:8000/groups/
    curl -H "Authorization: Bearer nujCtO6fgG73RNkeNqFqOD2WqvQ3n2" -X POST -d"username=foo&password=bar" http://localhost:8000/users/
    ```

- When you only assign read scope, so you cannot to access using write scope when run this command :
  
      curl -H "Authorization: Bearer nujCtO6fgG73RNkeNqFqOD2WqvQ3n2" -X POST -d"username=foo&password=bar" http://localhost:8000/users/
  
- Therefore, you have to grant new access for user like this :

      curl -X POST -d "grant_type=password&username=tuepro123@gmail.com&password=Thetue2309&scope=write" -u"BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu:FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl" http://localhost:8000/o/token/

- Result : ```{"access_token": "YFt7OGDMUOCkyIMwnlrzPARgvCGkMg", "expires_in": 36000, "token_type": "Bearer", "scope": "write", "refresh_token": "qfxhtAoaLpQghetfxwyDuHinpcIH2V"}```

- Then assign create again : 
  
      curl -H "Authorization: Bearer YFt7OGDMUOCkyIMwnlrzPARgvCGkMg" -X POST -d"username=foo&password=bar" http://localhost:8000/users/

- Result : ```{"username":"foo","email":"","first_name":"","last_name":""}```

**Why assign failed ?**
![img.png](image/img.png)

- Looking at picture you can see that if your scopes does not contain in the Oauth2 Provider then it will be Failed when make other scope.
- However, when you see in picture again you can see that scope can be merged with another like : read groups

## Test with another scopes 
### Test case 1 : 
#### Using scopes is children of root scopes

First you have permission in class group list :

![img_1.png](image/img_1.png)

Then you create new scopes is "read groups" in code : 

![img_2.png](image/img_2.png)

It shows the data even though the scope in class not exists in code. Maybe because of it has permission_classes = [permissions.IsAuthenticated, TokenHasScope]

### Test create another assign 

- **Test with create read and write** :
   
      curl -X POST -d "grant_type=password&username=tuepro123@gmail.com&password=Thetue2309&scope=read write" -u"BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu:FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl" http://localhost:8000/o/token/

- Then the result will be : 
  
      {"access_token": "hyrRZx2XPr9SNCnDlfotTet4Wra66C", "expires_in": 36000, "token_type": "Bearer", "scope": "read write", "refresh_token": "K2b1gSrmDhYHT7dt6ulwoyR6bGCaG1"}

    curl -X POST -d "grant_type=password&username=tuepro123@gmail.com&password=Thetue2309&scope=read user"-u"BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu:FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl" http://localhost:8000/o/token/


### Test case 2 : 
#### Create new model to add scope 
- First I create new App is Album 
- Then create model of it => create serializer and api view
- Add model to site admin then notice this : 
    - When data in admin create it will be had 's' at the end of model
    - Therefore, we have to add 'albums' to oauth provider like this : 
      ![img_3.png](image/img_3.png)
    - Add scope to API view
      ![img_4.png](image/img_4.png)
    - After that you will run in cmd : 
      ![img_5.png](image/img_5.png)
      
    - You can see that run success, and the after have key we will get data :
  
           [{"id":1,"name":"Tue Album","release_date":"2021-06-02","num_stars":1,"artist":1}]

      

### Test case 3 : 
#### Create , update, delete 

- Test with create another album :

    - Create access token : 
      
          curl -X POST -d "grant_type=password&username=tuepro123@gmail.com&password=Thetue2309&scope=read write albums" -u"BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu:FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl" http://localhost:8000/o/token/
    
    - Using access token to add new data albums : 
      
          curl -H "Authorization: Bearer c2wA9oyVyYNIyNu9aanAmEO8BfxvZT" -X POST -d"artist=1&name=Second Album&release_date=2021-06-15&num_stars=1" http://localhost:8000/create/album/

    - **Remember this**
      + When you create using ForeignKey that you have to put ForeignKey to parameter :
        + Such as : 
          + artist = 1 (1 is id of user)
          + name 
          + release_date 
          + num_stars 

- Test with update another album : 
    - Cannot use with curl, so I change to using POSTMAN instead
    - Then I create APIView of update album : 
        ```
        class UpdateAlbum(generics.UpdateAPIView):
          permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
          required_scopes = ['albums']
          queryset = Album.objects.all()
          serializer_class = AlbumSerializer
          lookup_field = 'pk'
        ```
    - Run in post man with access_token and remember your scope to running:
      + If you're using read scope, so you cannot update with code above
      + You have to have read and write scope to update data 
    - Running success in POSTMAN :
      + With read scope only : 
      ![img_6.png](image/img_6.png)
        
      + With read and write scope : 
      ![img_7.png](image/img_7.png)
        
### Test case 4 
#### With read write scope but not have album scope
- If you're just using read write scope and do not use album scope then it will tell that :
  
    {"detail": "You do not have permission to perform this action."}
  
- Or if you're using read write groups scope and do not use album scope it will tell that you do not have permission too.
    

### Test case 5
#### Create new scope not in model in settings.py ( such as : test)
- Test case 6.1 : scope = read groups read write albums
    - Cannot use because of 
    
          curl -X POST -d "grant_type=password&username=tuepro123@gmail.com&password=Thetue2309&scope(0)=create&scope(1)=read&scope(2)=update" -u"BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu:FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl" http://localhost:8000/o/token/

    - In this command you can see that it have three scope : 
        + scope(0)=create&scope(1)=read&scope(2)=update
    
### Test case 6
#### Using ViewSet 

## Permission

### TokenHasScope

-  The TokenHasScope permission class allows access only when the current access token has been authorized for all the scopes listed in the required_scopes field of the view.

- For example:

  ```
  class SongView(views.APIView):
      authentication_classes = [OAuth2Authentication]
      permission_classes = [TokenHasScope]
      required_scopes = ['music']
  ```
  The required_scopes attribute is mandatory.

### TokenHasReadWriteScope

The TokenHasReadWriteScope permission class allows access based on the READ_SCOPE and WRITE_SCOPE configured in the settings.

When the current request’s method is one of the “safe” methods GET, HEAD, OPTIONS the access is allowed only if the access token has been authorized for the READ_SCOPE scope. When the request’s method is one of POST, PUT, PATCH, DELETE the access is allowed if the access token has been authorized for the WRITE_SCOPE.

The required_scopes attribute is optional and can be used by other scopes needed in the view.

For example:
```
class SongView(views.APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    required_scopes = ['music']
```    

When a request is performed both the READ_SCOPE \ WRITE_SCOPE and ‘music’ scopes are required to be authorized for the current access token.

### TokenHasResourceScope
The TokenHasResourceScope permission class allows access only when the current access token has been authorized for all the scopes listed in the required_scopes field of the view but according of request’s method.

When the current request’s method is one of the “safe” methods, the access is allowed only if the access token has been authorized for the scope:read scope (for example music:read). When the request’s method is one of “non-safe” methods, the access is allowed only if the access token has been authorized for the scope:write scope (for example music:write).

```
class SongView(views.APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasResourceScope]
    required_scopes = ['music']
```

The required_scopes attribute is mandatory (you just need inform the resource scope).

### IsAuthenticatedOrTokenHasScope
The IsAuthenticatedOrTokenHasScope permission class allows access only when the current access token has been authorized for all the scopes listed in the required_scopes field of the view but according to the request’s method. It also allows access to Authenticated users who are authenticated in django, but were not authenticated through the OAuth2Authentication class. This allows for protection of the API using scopes, but still let’s users browse the full browseable API. To restrict users to only browse the parts of the browseable API they should be allowed to see, you can combine this with the DjangoModelPermission or the DjangoObjectPermission.

```
For example:

class SongView(views.APIView):
    permission_classes = [IsAuthenticatedOrTokenHasScope, DjangoModelPermission]
    required_scopes = ['music']
    
```

The required_scopes attribute is mandatory.

### TokenMatchesOASRequirements
The TokenMatchesOASRequirements permission class allows the access based on a per-method basis and with alternative lists of required scopes. This permission provides full functionality required by REST API specifications like the OpenAPI Specification (OAS) security requirement object.

The required_alternate_scopes attribute is a required map keyed by HTTP method name where each value is a list of alternative lists of required scopes.

In the follow example GET requires “read” scope, POST requires either “create” scope OR “post” and “widget” scopes, etc.

```
class SongView(views.APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["create"], ["post", "widget"]],
        "PUT":  [["update"], ["put", "widget"]],
        "DELETE": [["delete"], ["scope2", "scope3"]],
    }
```

The following is a minimal OAS declaration that shows the same required alternate scopes. It is complete enough to try it in the swagger editor.

```
openapi: "3.0.0"
info:
  title: songs
  version: v1
components:
  securitySchemes:
    song_auth:
      type: oauth2
      flows:
        implicit:
          authorizationUrl: http://localhost:8000/o/authorize
          scopes:
            read: read about a song
            create: create a new song
            update: update an existing song
            delete: delete a song
            post: create a new song
            widget: widget scope
            scope2: scope too
            scope3: another scope
paths:
  /songs:
    get:
      security:
        - song_auth: [read]
      responses:
        '200':
          description: A list of songs.
    post:
      security:
        - song_auth: [create]
        - song_auth: [post, widget]
      responses:
        '201':
          description: new song added
    put:
      security:
        - song_auth: [update]
        - song_auth: [put, widget]
      responses:
        '204':
          description: song updated
    delete:
      security:
        - song_auth: [delete]
        - song_auth: [scope2, scope3]
      responses:
        '200':
          description: song deleted

```

## Create model user in HRM web and try to add Scope in that 
    
## To show full URL : 
    - pip install django-extensions
    - python manage.py show_urls


## 