django-treasurehunt-demo
==

What is django-treasurehunt?
--
django-treasurehunt is an online treasure hunt engine built using Django.

Okay, but what exactly is an online treasure hunt?
--
>An online treasure hunt is one type of treasure hunt where players or treasure hunters search for answers to the questions given online. The answers or clues can be hidden anywhere on the Internet. Players use clues and hints given along with the question to get the answer. Once they enter the correct answer they are presented with the next question until they have finished all the questions. The  players who complete all the questions

Here's a live demo
--
http://oth-thebinaryrealm.rhcloud.com/


Running Locally
--

+ Clone this repo :
> git clone https://github.com/code-haven/Django-treasurehunt-demo.git

+ Install dependencies by running 
> pip install -r requirements.txt

+ Apply migrations
> python manage.py makemigrations treasure_hunt<br>
> python manage.py migrate


+ Run the server
> python manage.py runserver 

Now you will have the demo running at http://localhost:8000/

License
==
MIT
