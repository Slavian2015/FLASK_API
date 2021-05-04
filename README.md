Flask-SQLAlchemy-Docker-Compose-API
==========================

|ci| |coveralls| |pypi|


Quick start
===========

Chose a folder where to clone the project

.. code::

    cd path/to/all_projects

Clone the project

.. code::

	sudo git clone https://github.com/Slavian2015/FLASK_API.git
	cd FLASK_API
--------------

Prepare docker image
=======

.. code::

	sudo docker-compose build
	sudo docker-compose up -d
	

Run the program
=======

.. code::

	sudo docker exec -u root flask_api bash -c "python /usr/local/WB/dashboard/main.py"
	
--------------

Now you can go to "http://0.0.0.0:5151/courses" and you will see all the courses
=======


Make "GET" request to find course by ID
=======

.. code::

	http://0.0.0.0:5151/courses/1
	


Make "PUT" request to UPDATE course by ID
=======

make sure to add "body" to your request with key-value of the argument to UPDATE 

.. code::

	http://0.0.0.0:5151/courses/1
	


Make "DELETE" request to DELETE course by ID
=======

.. code::

	http://0.0.0.0:5151/courses/1
	
	

Make "POST" request to FILTER courses by one of the arguments (title / start_date / end_date )
=======

make sure to add "body" to your request with key-value of the argument to filter 

.. code::

	http://0.0.0.0:5151/courses/find
	

	
Make "POST" request to CREATE new course
=======

make sure to add "body" to your request with all key-value pairs

.. code:: python

	body = {
            "amount": 45, 
            "end_date": "2021-05-11", 
            "start_date": "2021-05-04", 
            "title": "Math"
	}

.. code::

	http://0.0.0.0:5151/courses/new