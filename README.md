# Neoquest 3

Tinkering with tech to create a full-scale game based on Neoquest.

## Goals

Yes, the tech I'll be throwing at this will be super overengineering. The project's main goal is for me to learn how to use these tools for larger-scale projects; not necessarily to make this efficient off the bat.

* Have a database with fance stuff
* Create a model
* Run it on Docker/Kuubernetes
* Create microservices
* have you, as a pet, interact with the world
* also add a cache

## References

* ooh it'd be fun to make it like Tir-Nan-Og
* https://idnq.net/
* http://thedailyneopets.com/articles/status-titles/
* http://www.oocities.org/neoquest_2/skills.html

## Web Application
The web application currently serves as a testing ground to view the PC model in a web browser.

To run the web application, run the following commands:

```
# Windows Powershell
$env:FLASK_APP = "app"
$env:FLASK_DEBUG = "development"
flask run
```

## Docker and Kubernetes Deployment

References
* https://codefresh.io/docker-tutorial/hello-whale-getting-started-docker-flask/
* https://learnk8s.io/blog/installing-docker-and-kubernetes-on-windows/

```bash
# Keep forgetting that I have Choco installed for Windows...
choco install minikube -y
choco install docker -y
```

```bash
# Build and deploy image
docker build -t neoquest3:latest .
docker run -d -p 5000:5000 neoquest3

# View Docker deploy status
docker ps -a

# Use docker-compose to deploy
docker-compose up

# If you're seeing an IP address of 192.168.99.100 you're probably using Docker Toolbox
# or Docker Machine, which is running Docker on a Linux VM, and that's the default
# IP address of that VM. If you're using one of these options to run Docker then
# you have to use the $(docker-machine ip) address, usually 192.168.99.100.
curl http://192.168.99.100:5000

# Stop Docker deployment
docker stop $DKR_ID
```

```bash
# After minikube is installed... start minikube
minikube start

# Check K8s status
kubectl get pods

# Check docker connection
minikube docker-env
docker ps

# Similar to Docker VM
curl http://192.168.99.101:5000

minikube delete
```
