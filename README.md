# Cyber Security Base 2022 - Course Project I

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

## FLAW 1: [CSRF (Cross-Site Request Forgery)](https://cybersecuritybase.mooc.fi/module-2.3/1-security)  

Write here...

## FLAW 2: [Injection](https://owasp.org/Top10/A03_2021-Injection/)  

Write here...

## FLAW 3: [Insecure Design](https://owasp.org/Top10/A04_2021-Insecure_Design/)  

Write here...

## FLAW 4: [Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)  

Write here...

## FLAW 5: [Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)  

Write here...