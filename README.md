## Item Catalog Readme ##

- This is a flask application that will start a webserver
serving at Localhost:5000
- All 

## Dependencies ##

- Virutal Machine (Virtualbox)
	- https://www.virtualbox.org/wiki/Downloads
	- Install the platform package for your operating system
- Vagrant
	- Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem
	- https://www.vagrantup.com/downloads.html
	- Install for your operating system
	- Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## How to Execute ##

1. Via Command Line, traverse to the vagrant configuation directory
2. Execute 'Vagrant up'
	- Wait till execution finishes, and you are given the terminal again
3. Execute 'Vagrant ssh'
4. Now you are in the virutal machine, type psql to access the PostGreSQL command interface
5. Type 'createdb news' to initialize the news database
6. Exit the PostGresSQL command line by typing '\q' and return
7. Execute 'python report.py' and results of the report will print in the terminal


## Design ##

- The program is sending queries to the local postgres database sitting in a virutal machine, and printing out the results to the standard output. 
- It follows the PEP8 style guide.
