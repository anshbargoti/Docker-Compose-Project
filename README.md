# Docker-Compose-Project

# WordPress-Docker-Compose
WordPress is a free and open source blogging tool and a content management system (CMS) based on PHP and MySQL, which runs on a web hosting service. Features include a plugin architecture and a template system. WordPress is used by more than 22.0% of the top 10 million websites as of August 2013. WordPress is the most popular blogging system in use on the Web, at more than 60 million websites. The most popular languages used are English, Spanish and Bahasa Indonesia.

# OwnCloud-Docker-Compose
OwnCloud is a self-hosted file sync and share server. It provides access to your data through a web interface, sync clients or WebDAV while providing a platform to view, sync and share across devices easily—all under your control. ownCloud’s open architecture is extensible via a simple but powerful API for applications and plugins and it works with any storage.

By using this repository you can :-
1. Pull images from [DockerHub](https://hub.docker.com/)
2. Create Docker volumes for permanent use.
3. Set Up MySQl Database.
4. Set up Wordpress for creating a website or blog.
5. Set up OwnCloud server for file hosting services.

## Built with
- RedHat Linux RHEL8
- Docker
- wordpress
- owncloud
- MYSQl

## Requirements
Make sure you have the latest versions of **Docker** and **Docker Compose** installed on your Base OS(In my case, RHEL8).

## For Docker Installation on Redhat/Centos:
- Configure yum by adding ***docker.repo and dvd.repo*** inside the `/etc/yum.repos.d` for local installation using  https://download.docker.com/linux/centos/docker-ce.repo   
- Now, execute command `yum install docker-ce --nobest`

## Start Docker:
```
$ sudo systemctl start docker
```
After Docker installation, Install Docker Compose:-
```
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
![img0](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/installing_docker_compose.PNG)

After installation of the above files:-
```
sudo systemctl start docker
sudo systemctl enable docker
```
 ##  Download the Required Images
Download The OwnCloud and Wordpress and MySQL image from https://hub.docker.com using 
    
    docker pull owncloud:latest
    docker pull wordpress:5.1.1-php7.3-apache
    docker pull mysql:5.7 
 
 ##  Create the Required Volumes
   
    docker volume create owncloud_storage_new
    docker volume create ownsql_storage_new
    docker volume create mysql_storage_new
    docker volume create wp_storage_new
    
![img0](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/image.jpg)

 ## MySQL setup
Write command 

    docker -i -t -e MYSQL_ROOT_PASSWORD=(your_password) -e MYSQL_USER=(username) -e MYSQL_PASSWORD=(your_password) -e MYSQL_DATABASE+ (any_database_name) --name dbos mysql:5.7
    
 ## MySQL client
If you want to verify that your database has been created or not, install MySQL client software using `yum install mysql`. After installation execute this command : 
   
    mysql -h 172.20.0.2/16 (your MySQL container IP) -u (username) -p(password)
    
 ## Docker-Compose
Install a docker-compose software from https://docs.docker.com/compose/install. 
Make a compose file using 

    mkdir wordpress.
    mkdir owncloud.
    
![img0](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/directory.jpg)
    
You can create/edit your docker-compose file using 
    
    vim docker-compose.yml
The file name should always be docker-compose.yml

Now, How to create it and maintain it as Infrastructure As A Code(IAAS). It's using docker-compose, it uses YAML format file to make it an easy and managable source code file to easily share and create environment. For this you have to create a file with name docker-compose.yml inside each of the directory of wordpress and owncloud, for now assume we have to give this name only but it's not always the case you can give other name or make multiple files also.

## Docker-Compose-File

![img0](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/owncloud.png)
![img1](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/wordpress.png)

## Scripting

Now, We will use python script file for better TUI behaviour using os module in python, import os loads the os module of python using which you can run CLI(Command Line Interface) commands. So for this I have used system() function of os module as os.system("<command you want to perform>").

![img0](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/python_script.png)


Open a terminal and `cd` to the folder in which `python script file` is saved and run `python3 docker.py`:-

![img0](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/docker-compose(1).png)
![img1](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/docker-compose(2).png)
![img2](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/docker-compose(3).png)

Hola!, Everything is Set now the containers are now built and running. You should be able to access the WordPress and OwnCloud with the configured IP in the windows browser address by :-

For Wordpress=> `http://192.168.xx.xx:8081`  and for linux OS `http://172.2x.x.x:8081`.
For OwnCloud=> `http://192.168.xx.xx:8082`  and for linux OS `http://172.2x.x.x:8082`

## Here is an instance of my OwnCloud server website and Wordpress website which I built using this repo:- 

![img0](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/browseWordpress.PNG)
![img1](https://github.com/anshbargoti/Docker-Compose-Project/blob/master/snap/browse_Owncloud.PNG)

### Fore more reference on docker-compose 

### Start Environment

```
docker-compose start
```

### Stopping Environment

```
docker-compose stop
```

   #### Depends_on : 
OwnCloud and Wordpress uses database server. We have to specify which database container it should depend on.
   #### Ports : 
To expose our container to outside world by using PAT.
   
  
## Author
[**Ansh Bargoti**]
