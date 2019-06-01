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

## Database Migrations and Updates

```bash
flask db init

flask db migrate -m "message goes here"
```

## Docker and Kubernetes Deployment

References
* https://codefresh.io/docker-tutorial/hello-whale-getting-started-docker-flask/
* https://learnk8s.io/blog/installing-docker-and-kubernetes-on-windows/
* https://blogmilind.wordpress.com/2018/01/30/running-local-docker-images-in-kubernetes/
* https://github.com/kubernetes/minikube/blob/master/README.md
* TBD: https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/

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

# You'll need to find the IP address of the Docker or K8s cluster
# that is run on a VM
curl http://192.168.99.100:5000

# Stop Docker deployment
docker stop $DKR_ID
```

```bash
# After minikube is installed, start minikube
# For first-time creations, I needed to restart this process a few times
minikube start --v=7 --alsologtostderr

# Integrate Docker to Minikube
minikube docker-env
docker ps

# Check K8s status
kubectl get pods

# Can SSH into Minikube to debug
minikube ssh

# Deploy the local Docker image into Minikube
docker build -t neoquest3:latest .
kubectl run neoquest3 --image=neoquest3:latest --image-pull-policy=Never --port=5000
kubectl expose deployment neoquest3 --type=NodePort

# Open the webapp based on K8s configs
minikube service neoquest3

# Teardown deployment and stop the Minikube cluster
kubectl delete deployment neoquest3
kubectl delete svc neoquest3
minikube stop
```
