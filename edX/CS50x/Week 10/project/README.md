# __INSPIRE__
#### Video Demo:  <https://youtu.be/D4UbuZvwhsA>

## __Definition__
 This web-app allows user to create accounts and by loging in, they can create, edit and delete notes.

 Project structure :
 - static
 - templates
 - app.py
 - inspire.db
 - README.md
 - requirements.txt

## __Usage__

```cd project```
```flask run```
```
Then by clicking on the given link, web-app would be opened.
```

## __Functioning__

The static folder contains 1 file.

#### __style.css__ :
It contains all the css for the html files in the templates folder.

The templates folder contains 8 files.

#### __home.html__ :
It is the index or the home page of the website which describes the app and have two buttons login and register. If a new
user then click on the register otherwise login.
#### __register.html__ :
User can register by providing email, name and password. If any of the provided info is wrong it will let user know by
alerts. It also has a reset button which will delete data from all the input fields. And if the email is already in use it
will open a new page.
#### __user_exist.html__ :
When the user is trying to register with the wrong email, this page will open. It has two buttons register and login. So
if that email already exists user can register with another email or simply log in.
#### __login.html__ :
Now user can login with a valid email, name and password. If all the data is valid it will open the index page otherwise
it will reload the login page.
#### __index.html__ :
All the notes will be displayed here. Each note has two buttons edit and delete. By clicking on delete button, the note
will be deleted and by clicking on edit button, it will redirect to a new page. And a button that has the username and a
phrase like this 'Username, What's on your mind'. By clicking on this button user will be redirected to a new page. On the index there is a also a logout button. By clicking on logout user will be redirected to login page and the session will
get expired.
#### __post.html__ :
This page has a input text field and a submit button. After writing some note user can click on submit that will redirect
again to the index page.
#### __edit_note.html__ :
It has a similar interface like post page but in the text field it has the note, and user can change it and submit it that
will redirect them to the index page.

The app.py contains the corresponding routes for these html pages.

#### __home__ function:
Home route is simply rendering the home page.
#### __index__ function:
Index route check for the session, if the session has expired it redirect to login page otherwise execute a database query
to select notes and then render the index page.
#### __login__ function:
If the post method in login route, it will get name, email and password from the corresponding html page and executes the
database query to check if the info is valid and if valid it will redirect to index page. And if the get method render the
login page.
#### __logout__ function:
It will set the session variable to none and then redirect to index page (which will redirect it to login page).
#### __register__ function:
In the post method of register route we will get the valid name, email and password (validate by regex) and insert it into
the database by executing query and then redirect to the index page. And the get method renders the register page.
#### __user_exist__ function:
User exist route simple renders the user_email page.
#### __post__ function:
In the post method of post route we get the note from the corresponding html page and insert it into the database. And for
the get method, it renders the post page.
#### __delete_note__ function:
Delete route gets the note from the corresponding html page and delete it by executing the query and then redirect to the
index page.
#### __edit_note_page__ function:
Edit note page gets the note and renders the edit_note page.
#### __edit_note__ function:
Edit route gets the unedited and edited note and then execute the database query to update the old note by the new note.
And then redirects to the index page.
### Author : Rameen