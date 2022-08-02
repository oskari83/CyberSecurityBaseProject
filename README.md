# Cyber Security Base 2021 - Course Project I

My Cyber Security Base Course Project with flaws from the [OWASP 2021 list](https://owasp.org/www-project-top-ten/).

All the fixes to the flaws are written below and not within the code as this is simpler

Link to repository: https://github.com/oskari83/CyberSecurityBaseProject

To use the demo project, download and extract the project files and run the following command:
```
python manage.py runserver
```
If the database isn't working correctly, run the following commands as well:
```
python manage.py makemigrations
python manage.py migrate
```

Once set up, you can access the homepage from: http://127.0.0.1:8000/ or http://127.0.0.1:8000/polls

If you'd like to access the admin interface or make changes to database entries i.e. questions or choices you can do so from:
http://127.0.0.1:8000/admin/
  
**Username:** admin  
**Password:** password