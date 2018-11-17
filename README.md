## Item Catalog Readme ##

![Front-End Photo](frontend_demo.png)

- This is a flask application that will start a webserver
serving at Localhost:5000
- Data is persisted in a SqLite database hosted on the local machine
- Users can login via OAuth2.0 using Google Api, and perform CRUD operations
via the frontend being delivered by flask. 


## Dependencies ##

- Virutal Machine (Virtualbox)
	- https://www.virtualbox.org/wiki/Downloads
	- Install the platform package for your operating system
- Vagrant
	- Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem
	- https://www.vagrantup.com/downloads.html
	- Install for your operating system
	- Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.


## How to Start Application ##

1. Via Command Line, traverse to the root directory of this git repo (where
the Vagrantfile is)
2. Execute 'vagrant up'
	- Wait till execution finishes, and you are given the terminal again
3. Execute 'vagrant ssh' (This will SSH you into the VM)
4. In SSH, execute 'cd ../../vagrant/catalog'
5. Run 'python database_setup.py'
6. Run 'python initalize_item_database.py'
7. Run 'python application.py'
8. Visit localhost:5000 on a web browser on same machine to visit Item Catalog


## Design ##

- The backend is sqlite, the database is mapped to ORM using SQLAlchemy
- Flask is the webserver framework
- It follows the PEP8 style guide.
