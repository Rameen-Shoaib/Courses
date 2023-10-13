# __CURRENCY CONVERTER__
#### Video Demo:  <https://www.youtube.com/watch?v=RtCOCmH6WIw>

## __Definition__
 This project converts currencies to one another.

 Project structure :
 - project.py
 - test_project.py
 - requirements.txt
 - README.md

## __Libraries__

__Requests__ : The request module allows you to send http requests.. [(Readmore)](https://pypi.org/project/requests/)

__ART__ : The pprint module provides a capability to "pretty-print" arbitary Python data structures in a form which can be used as input to the interpreter.[(Readmore)](https://docs.python.org/3/library/pprint.html)

## **Installing Libraries**
There is a a requirements.txt file that has all the libraries used and simply can be install by using the pip commands:

```pip install requests```
```pip install pprintpp```
```pip install pytest```

## __Usage__

```python project.py```
```
Welcome to the Currency Converter! If you want to quit press q
Select an option:
List - list all the currencies
Convert - convert from one currency to another
Rate - get the exchange rate of two currencies
Name - gets the name of the currency id
```
After that the user can select an option List, Convert, Rate or Name. and has the ability to Exit at any time using q.

## __Functioning__

The project.py contains 6 functions including the main function.

#### __get_currencies()__ function :
This function takes no argument. It sends the request to the api to get the data in the form of json and then convert
the dict in it to list and tuples.
#### __print_currencies()__ function:
This function takes one argument, the return value of the get_currencies function. It iterates throught the list and
find the values of currency name, id and symbol and prints it.
#### __currency_name()__ function:
This function takes two argument, the return value of the get_currencies function and takes input the id of the currency to find its name. It iterates throught the list and if the inputted id is equal to the id it prints its name and return it.
#### __exchange_rate()__ function:
This function takes two argument, the base currency and the currency to convert to. It sends the request to the api to get the data in the form of json. If the length of data is zero it print invalid currencies else print the rate and return it.
#### __convert()__ function:
This function takes three argument, the base currency and the currency to convert to and the amount. It takes the return value of the exchange_rate function and multiply it with the amount. Then prints the result and return it.
### Author : Rameen