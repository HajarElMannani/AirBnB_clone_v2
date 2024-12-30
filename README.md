# AirBnB clone
------------------------------------------------------------
This project consists of building a full web application: the AirBnB clone.  
## The console  
----------------------------------------------------------------
The console will help us manage the backend and manage the objects of this projetct as the following :  

    Create a new object (ex: a new User or a new Place)  
    Retrieve an object from a file, a database etc…  
    Do operations on objects (count, compute stats, etc…)  
    Update attributes of an object  
    Destroy an object  

----------------------------------------------------------------
### How to start the console?  
Start the console by running the file `console.py`  
```
$ ./console.py
(hbnb)
```
This will run the console on interactive mode.  

To quit the console use `ctrl + d` or the command `quit`:  
```
(hbnb) quit
$
```
### how to use it?

The console uses the following commands:  
Eof, quit, create, show, destroy, all, help, update.


**EOF**  
Use EOF command or `ctrl+d` to quit the console.  
```
(hbnb) EOF
$
```
---------------------------------------------------------
**quit**
Use `quit` command to quit the console:  

```
(hbnb) quit
$
```
------------------------------------------------------------
**help**  
Use help to have documentation and usage of the console:  

```
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
```
---------------------------------------------------------------
**create**  
Use create to create a new instances, it prints the id of te object  
**usage**: `create <class>`  
```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```
---------------------------------------------------------------
**show**  
Use `show` to print the string representation of an instance based on the class name and id.  
**Usage**: `show <class> <id>`  
```
(hbnb) hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```
--------------------------------------------------
**all**  
Use `all` to print all string representation of all instances based or not on the class name  

**usage**: `all or all <class>`  
```
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```
or:  
```
(hbnb) all
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```
---------------------------------------------------
**destroy**  
Use `destroy` to Deletes an instance based on the class name and id  
**usage**: `destroy <class> <id>`  
```
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb)
```
-----------------------------------------------------
**update**  
Use `update` to update an instance based on the class name and id by adding or updating attribute.  

**usage**: `update <class name> <id> <attribute name> "<attribute value>"  `
```
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
```
