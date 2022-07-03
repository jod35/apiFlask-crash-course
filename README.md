# APIFlask crash course
This is code I wrote for a crash course on [APIFlask](https://apiflask.com/).


## How to run project
- Clone repository with  
```` git clone https://github.com/jod35/apiFlask-crash-course.git && cd apiFlask-crash-course````

- Install all requirements <br>
````pip3 install -r requrements.txt````

- Set up your ```FLASK_ENV``` , ```FLASK_DEBUG``` , ``` FLASK_APP``` in a ```.flaskenv``` file <br>
````
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_APP=main.py
````

- Run ```db.py``` to create database 
- Run app with ```flask run```