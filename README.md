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
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/polls/templates/polls/detail.html#L10

Cross-site request forgery is an attack where existing user priviliges (cookies or tokens) of an authenticated user on a computer are used to make malicious requests and access private user data. In other words, if a user is logged in to, for example, their banks website, a malicious agent can send an unsolicited email or plant an exploit on a site they know the target is going to visit. If the website is vulnerable to CSRF, the attacker can implant a malicious url in an HTML image or link, or if the target website only accepts POST requests, then through an HTML form and some javascript. Once executed it looks like the target has willfully transferred funds to the attacker with no way to remedy the situation other than contacting the bank itself and trying to seek help through them.

To fix these flaws we only need to add {% csrf_token %} to each form in our application and django will take care of the rest. (The CSRF flaw is fixed in my project so that the demo app runs)

## FLAW 2: [Injection](https://owasp.org/Top10/A03_2021-Injection/)  

Locations of flaws:
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/polls/views.py#L35
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/polls/views.py#L51

Injection is a vulnerability in the code where a malicious user can send code to the server hidden as regular user data that then gets executed on the server. This execution is not planned for and hence can cause anything from access to private data to corruption of files. One of the most common forms of injection is SQL injection where database queries are made without "cleaning" or "sanitizing" user data i.e. making sure it contains only what it is supposed to. 

Currently the flaw in my code only exists in the comments meaning I have already fixed it. This has been done by utilizing djangos readymade models framwork for database queries which takes care of sanitizing data so that injection of the SQLite database is not possible. In the commented lines you can however see that when using the execute command the database is vulnerable to injection.

## FLAW 3: [Insecure Design](https://owasp.org/Top10/A04_2021-Insecure_Design/)  

Locations of flaws:
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/polls/tests.py#L3
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/polls/views.py#L13

Insecure design is a collection of software flaws that arise from poor design and software architecture. Examples of insecure design are systems which are vulnerable to bots in for instance scalping, flaws in business logic with either monetary or privacy leaks, or authentication systems that are designed for speed and ease of use potentially allowing users to choose unsafe passwords. In other words, insecure design is an umbrella term for inherent logical or systematic flaws that are not as a result of poor implementation, but rather due to poor design. The main prevention against insecure design is the use of robust testing and design protocols. Django allows us to create automated tests and as a developer one can follow a discipline called TDD or test driven development to create tests in advance and build functionality around them. 

To fix the lack of tests I simply need to create a wide range of tests covering different situations and edge cases. Another flaw in my app is that one can vote several times on a single poll which is not wanted as this can skew results. Testing would have discovered this flaw, and to fix it one needs to implement similar systems as with the "Millionaire" exercise in part 5 of the course.

## FLAW 4: [Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)  

Locations of flaws:
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/cybersecurityproject/settings.py#L41

Vulnerable and outdated components is a flaw where one uses pre-existing software components i.e. code that has vulnerabilites thereby exposing one's own app to these vulnerabilities as well. This means that one needs to periodically audit the components one uses to make sure one isn't exposing oneself to vulnerabilities as time goes on and more security risks are discovered. Luckily django and many other frameworks do this automatically so we only need to pay attention to its warnings.

So just for the sake of this flaw I tried to found a vulnerable component and when I ran pip-audit I found that the werkzeug package has known vulnerabilites. Hence including it in the project is a flaw and to fix this one needs to either remove the package or update it.


## FLAW 5: [Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)  

Locations of flaws:
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/cybersecurityproject/settings.py#L128
https://github.com/oskari83/CyberSecurityBaseProject/blob/master/cybersecurityproject/polls/views.py#L8

Failures in security logging and monitoring are flaws that lead to inability to detect breaches or malicious use. Not only does this mean that responding to these breaches is impossible (since one does not even know they are happening), but the root cause of these breaches remains unearthed. Proper logging and monitoring is essential in making sure that one can act in response to security breaches and fix any vulnerabilities as they give a hint to the developer as to how to correct them.

As there is no logger currently in use in the project, fixing this flaw requires us to simply add a logger to our project and then configure it to log any important actions in our app. We could for example log every time that a poll is created or voted on or the adming logs in to the app etc. 