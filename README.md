# Flask Skeleton Project

### Flask skeleton project as a base project for app development
##### [https://github.com/barakpinchovski/flask-skeleton-project](https://github.com/barakpinchovski/flask-skeleton-project)
<br/>

##### Description: 
This is a base skeleton Flask project to start developing on.
<br/>
You may want to modify some of the configurations and files as needed. 
   
###
##### Keywords: 
flask, lean, skeleton, project, structure, environment, setup, template, fullstack, web, development, app, university, education.
###

##### By Barak Pinchovski
[LinkedIn](https://www.linkedin.com/in/barakpinch/)
##
 
### Setup and run instructions:

#### Prerequisites:
Open the project's dir in the terminal and run the following commands:
1. pip install virtualenv
1. virtualenv venv
1. pip install python-dotenv
<br/>

#### Configurations:
Open the project's dir in the terminal and:
1. Run the command: **python -c "import os; print(os.urandom(16))"**
1. Copy the output string
1. Edit the project's **.env** file found inside the root folder
1. Overwrite the **SECRET_KEY** value with the string you copied
<br/>
 
#### Run:
 Run the project with your IDE's configuration, or from the terminal by using the **flask run** command
 
 ##
 
### Usage:

#### Connecting and querying a database:
1. Edit **.env** file with your database details
1. On `.py` files you'd like to connect to the database, use the following imports:
    ```python
    from settings import DB
    import mysql.connector
    ```
1. Connect to the database with **DB as the argument
    ```python
   db_connection = mysql.connector.connect(**DB)
   ```
1. **Tip**: If you'd like the queried results to behave like JavaScript objects then instantiate cursor as follows:
    ```python
   db_cursor = db_connection.cursor(named_tuple=True)
   ``` 
   Once you do that, you'll be able access the properties with dot notation.
   
   Read more about it [here](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)
   
   Example:
   ```python
   from settings import DB
   import mysql.connector
   db_connection = mysql.connector.connect(**DB)
   db_cursor = db_connection.cursor(named_tuple=True)
   db_cursor.execute('SELECT * FROM example_table')
   records = db_cursor.fetchall()
   for record in records:
       print(record.id) #prints the record's ID 
   ```