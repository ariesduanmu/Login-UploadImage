# Login-UploadImage
Login&amp;UploadImage Simple Server in Flask


### Uage

*datebase init*

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

*add user*

```
python manage.py shell
>> user = User('admin')
>> user.password = 'password'
>> db.session.add(user)
>> db.session.commit()
```


*run server*

`python manage.py`

*browser*

`http://127.0.0.1:1337/`
