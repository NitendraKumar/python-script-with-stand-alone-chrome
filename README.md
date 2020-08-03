# Running Stand-alone-chrome docker container using docker compose 


### In this example we will learn following ### 
   - How to mount logs directory 
   - How to mount data directory 
   - How to run stand alone chrome container 
   - How to run python script which is using selenium web driver.
   - How to connect chrome server using python script.
   - If container A is dependent on contaner B but container A start first then how to handle this situation using wait-for-it shell script

*After exploring Docker i leant few concept which may be helpfull for other beginner like me*

##Prerequisite
- Before exploring docker you must have docker and docker-compose installed on your machine ( I used ubuntu 14.x.x)
- You also must have permission to access docker.


*Ok Let get your hand dirty with docker*

* Asuming you have all the python script log/data directory inside working directory

* First File in this process is DockerFile 
  * Docker file contains all the instruction to build your docker-image
  * All the instruction to copy all the files of application/python script goes here.
  * See DockerFile in repository.
* Second File docker-compose.yml
  * This file containse how to build your image. 
  * How to start container
  * How to run link the container etc.
  
####Now Lets look into docker-compose.yml

#### Copy File from docker container to host machine
* docker cp <containerid>:/home/users.json /home/palanteert/
 
 


  
