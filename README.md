# Cyber Security Base 2022 - Course Project I

My Cyber Security Base Course Project with flaws from the [OWASP 2021 list](https://owasp.org/www-project-top-ten/) + CSRF.

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

Locations of flaws:
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/polls/templates/polls/add_poll.html#L9
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/polls/templates/polls/add_poll.html#L14
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/polls/templates/polls/detail.html#L10

Cross-site request forgery is an attack where existing user priviliges (cookies or tokens) of an authenticated user on a computer are used to make malicious requests and access private user data. In other words, if a user is logged in to, for example, their banks website, a malicious agent can send an unsolicited email or plant an exploit on a site they know the target is going to visit. If the website is vulnerable to CSRF, the attacker can implant a malicious url in an HTML image or link, or if the target website only accepts POST requests, then through an HTML form and some javascript. Once executed it looks like the target has willfully transferred funds to the attacker with no way to remedy the situation other than contacting the bank itself and trying to seek help through them.

To fix these flaws we only need to add {% csrf_token %} to each form in our application and django will take care of the rest. You can see this as comments in the linked locations of the flaws.

## FLAW 2: [Injection](https://owasp.org/Top10/A03_2021-Injection/)  

Write here...

## FLAW 3: [Insecure Design](https://owasp.org/Top10/A04_2021-Insecure_Design/)  

Write here...

## FLAW 4: [Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)  

Write here...

## FLAW 5: [Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)  

Write here...