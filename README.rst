System Information using Flask
===============================
This application is developed on flask using a private package called ``systeminfo`` to display the information of the platform this app is installed on. To use this application simply follow the following steps:
+ Install this app and all its dependencies from this repository::

        pip install git+https://git@github.com/harshrpg/COMP30670_FlaskSI.git

+ Once installation is complete, Set the ``FLASK_APP`` environment variable::  
      
        set FLASK_APP = app

+ Run the following command:: 
      
        flask run

This application uses private package called ``systeminfo``. This package will be installed automatically with this flask app. You can still find the ``systeminfo`` package at:
        
        <https://github.com/harshrpg/COMP30670_CookieCutter>
