# BookGenProject
QA devops practical project - Sibel Hassan

## Project Brief
The requirements of this project was to create a service orientated application
that follos this architecture, using four services that work with each other
to produce an end result. From here the project must use cloud fundamentals and 
continuous integration techniques. 

The requirements of the project are as follows:

* An Asana / Jira board with full expansion on tasks needed to complete the project.
* Record of any issues or risks faced during the project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
* If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application.
* The project must follow the Service-oriented architecture that has been asked for.
* An Ansible Playbook that will provision the environment.
* A reverse proxy to make the application accessible to the user.

For the purpose of this project the minimum viable product was planned and created.

## Appplication : Design 

For this project I created an application that generates a book when requested user, by choosing a random genre, then a random author and finally returning a book that matches both. This was created using a service-oriented architecture, a front end service sending html requests to API's to recieve its end result.

![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Book-Gen.png)

## Jira : Planning 
For this project Jira was used to manage the workflow, creating a backlog of tasks that needed to be created, as well as user stories. For each of these tasks, a priorty was set based on its importance to the project, and a story point was assigned based on how difficult of a task it would be to implement. This again allowed me a better understanding of what needed to be done and the best way to divide the project into sprints. 

![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Jira%20backlog%2C%20sprints.png)

Once the sprints were created with their allocated tasks, it was moved onto a kanban board where I could keep track of the tasks that were in progress, which were completed and which were yet to be started. Again this just allowed for further planning and tracking of the development of the project. 

![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Sprint%20example.png)

Using Jira and the built-in attributes you can allocated to tasks and sprints allowed me to keep track of the number of story points in total the project had and compare this to the days I had to complete the assignment. This allowed me to created an expected burndown of my story points in relation to time, keeping track of my progress I was then able to include my actual burndown progress. Overall, there were quite a few deviations to the expected burndown, either because of issues faces prolonging the task or some running smoother than expected but overall the project was completed on time. 

![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/burndown.jpg)


## Risk Assessment : Planning 

![](![image](https://user-images.githubusercontent.com/45011190/189105781-2782050d-88ba-40c8-8772-4d68c3579c4d.png)

This risk assessment details some of the possible risks that may have been encountered when completeing these products, mainly the issues that were possible would be down to poor planning or design on my end, or mainly issues with GCP, Jenkins, Ansible and docker as these are the biggest contributing factors to the project, the python is key but simple in comparrison. The risk assessment breaks down what may happen, the outcome, who is responsible, how detrimental the error would be if occured, probablity, response and preventative measures. Identifying these issues before they occur allows for better control of issues when and if they arise duing the project timeframe. 

## Version Control System : Feature-Branch Model 

![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/branches%20for%202ns.png)

For this project github was used as the version control system within this project which allowed me to keep track of changes made to my repository. For this project the feature-branch model was utilised, meaning that for any big feature of the project a new branch was created to work off of. This means that the two main branches Main and Dev, are unaffected by any new changes to the code until it is time to include it into this project. This ensures that if an issue occurs when the features are integrated, the main branches are unaffected by this change and are still functional. For this project I had a branch for each service, a configuration branch, testing branch and a branch where improvements were made or errors were fixed. This allowed me to keep a working product whilst constantly being able to update and improve the project on another branch. 

## Virtual Machines : GCP

One of the requirements of this project was for the app to be deployed to a cloud based virtual machine and for this project I used google cloud platform. Here I creamed the virtual instances that I connected to VSCode, a Jenkins server, a swarm manager(node-m) and a swarm worker (instance-1). It was on these virtual machines that I was able to work on a remote host and build the application as well as deploy it. 

![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/gcp%20vms.png) \

In order for the virtual machines to run the applications needed, I needed to create firewall rules and add them as network tags to allow the virtual machine to connect to the ports when running, for example, flask apps run on port 5000 and jenkins runs on port8080 so these needs to be accepted and accessible within these virtual machines. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/GCP%20tags.png)

## The Application : Service-oriented Architecture 

Having a service-oriented architecture for the application was a key part in this project, the brief declared a front end was required, two random services and a logic service that returned the desired result. To achieve this the application was planned as follows: \
**Service 1 : Front End** This is what the user will see - it will make the requests to the other service apis and then print the result to the user. \
![image](https://user-images.githubusercontent.com/45011190/189123211-a7b0ff86-d2c6-49d1-81a6-4b9d4da149bc.png) \
**Service 2 : Genre-api** This is the server that randomly selects a genre from an array using random.choice and sends it back to the **front-end**\
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/s2%20random.png) \
**Service 3 : Author-api** This is the server that randomly selects an author from an array using random.choice and sends it back the the **front-end**\
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/s3%20random.png) \
**Service 4 : Book-api** This is the logic server, which takes the randomly selected genre and author from **service 1** and **service 2** and returns a book that matches the two. In order to do this a dictionary was created, the key being the book title and the values being a tuple of (genre,author) passed from the variables in the front end. It then returns the book that matches the correct genre and author and sends it back the the **front-end**. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/s4%20logic.png) 

## Ansible : The Environment 
Ansible is an automation tool, that for this project was used to develop the environment that the virtual machines would be using. To do this, a folder called configuration was created that was home to all of the ansible side of the project. The benefit of using ansible is that it automatically allows the environment to be built for the virtual machines to make sure they have all the requirements and tasks defined. 
### Roles 
Ansible roles allowed me to automate tasks that needed to be done to develop the environment on the virtual machines that would be used. The following roles were created. \
**DockerInstall** This task when called in the playbook, would download docker onto all the hosts specified. This not only ensures that all hosts have docker installed, but they have the same version. \
**initialinstalls** This role was created to update apt packages and install the necessary packages for this project to run on the vms, these packages included * *Python3, python3-pip, git and python-setuptools* * to their latest versions. \
**Pipinstalls** Similar to the previous role, this was created to install the pip dependencies for the project, these being * *Flask and Pytest* - These are the initial pip installs requires and the others were covered by the requirement.txt files within each service folder. \
**Swarminit** This role initialised the swarm, gathers the swarm info and then deploys the app. This role is primarily for the swarm manager. It provisions the manager node ready for any number of worker nodes to join the project needs scaling. For this project only one worker node will be joining the swarm. \
**Swarmjoin** This role is primarily for the worker nodes and it joins the worker to the swarm initalised by the manager node.\
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Ansible%20roles.png)

### Playbook
The playbook is where you allocate the tasks to the host groups defined in the inventory. As you can see in my playbook, there are tasks that all hosts need to do, which are in the installs to provision the environment. Further down is the unique task swarminit assigned to the manager host and the swarm join allocated to the worker group hosts. The become true option allows the tasks to be carried out as a root/sudo command. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Playbook%20yaml.png) \

### Inventory 
The inventory file defines the hosts and the host groups that will be used when running the ansible tasks defined above. For this project we have the worker-group and the manager-group. For the mvp, only one worker node was provisioned so only one host exists under each host group. Once the hosts are defined, we can then set the variables, the host name is jenkins, the path to the shh key so they can connect, turning off strict host key checking to prevent errors and a path to the python interpreter. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Inventory%20yaml.png) \

## Docker : Containerisation
Docker was used within this project, it allows the product to be containerised so that whenever or wherever the project needs to run it will be delivered and run in the same way, as defined within the dockerfiles. Just like actual shipping containers, the project is developed, saved into an image which is then containerised, and shipped to wherever the project needs to run. 
### Dockerfiles & Building Images 
Images are files used to execute code within containers and a Dockerfilea allow us to break down the different elements needed to run in order to build that image. It basically includes the build instructions for that image. When the docker build command is then run, docker will follow these instructions to build the image. 
**FROM** details where the image is built from, in this case this image is being built from * *python:3.8* * which is referencing and calling information from the python:3.8 docker image to automate the build process. \
**COPY** this copies all of the files within the same directory as the dockerfile. \
**RUN** run is a command that runs during build time of the image, this specific run pip installs all the dependencies from the requirements.txt file. \
**EXPOSE** simply details the port that needs to be exposed for project. \
**ENTRYPOINT** specifes the executable command that will run the container. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Dockerfile.png) \

### Docker-compose
Docker-compose files are used to define, run and manage multiple containers without the need to define each and every container indivually. It allows you to spin up or spin down the containers with one command. Within this docker compose file you break it down into the services needed, for this project the different services/apis as well as the NGINX service where broken down and defined. It breaks down what the image will be called, the ports that need to be exposed, the network it may be using, the build path and more. For this project I created a book-net network that all containers needed to be on in order to communicate with each other. \ 
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/docker%20compose.png)

When docker compose up is run within my project environment it creates containers for all of the services, Nginx and the network needed for them to communicate, as well as any replicas asked for. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/docker%20compose%20up.png) \

### Docker swarm stack : Orchestration Tool
Docker swarm is an orchestration tool that allows us to deploy the same application across as many environments as we need without needing to redefine it. You have a swarm manager that created the stack, and then you can connect as many workers as you need that will run the same application. For the purpose of this project, the swam manager is node-m and it is where the application was designed and first deployed. The one and only worker node for this project is called instance-1 and it runs exactly the same application on that virtual machine as the manager. This means many different environments can run the same application by simply joing the stack. 

## NGINX : Reverse Proxy
A reverse proxy sits in front of a web server and receives all the requests before they reach the origin server, this maintains anonymity and enhances security, it ensures no user directly communicates with the origin server. NGINX in this case listens on port 80, takes requests and then sends them to the front end service of my application on port 5000.\
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/nginx.png) \

## Testing : Mock Testing/ Unit Tests
Mock testing is a way to generate a fake output of a function that needs to be tests, this is key when testing functions that make a request from a seperate API that is unreachable at testing. For testing, I carried out tests for each serivce, testing that service 2 and 3 called a random value within the arrays and returned them. I tested the logic in s4 to ensure it was sending a correct book based on author and genre, and within the front end, I tested its home value as well as its ability to return results given it has its mock values. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/mock%20unit%20tests.png) \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/book-api%20test.png) \


## CI Server : Jenkins 

### Pipeline
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Pipeline%20stages%20view.png) \
#### Run Tests
Using a testing script within my protect I called the script to be run, this allowed my tests to be run on jenkins as part of my pipeline. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/test%20script.png) \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/test%20outcomes.png) \
#### Build and push images 
During the build and push stage, I just called the docker build command to build the images of the app, log into docker hub and push the created images to my docker hub. 
#### Deploy app
During the deploy app stage I ran the docker compose file, the nginx file as well as running the playbook and the inventory to give tasks to the correct hosts.\
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Pipeline%20code.png)
#### Print testing reports 
As a post declarative action on my pipeline I used the cobertura plugin to create testing reports for all of the unit tests run in the testing stage of my pipeline. This just allowed the testing results and coverage to be clearly displayed and graphs to be created to clearly showed the outcome of my tests. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/cobertura.png) \
![](https://github.com/Sibel97/BookGenProject/blob/main/Read-me%20images/test%20graph%20coverage.png) \ 
\
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/success.png) \
## Continuous Integration : Webhooks
A github webhook was created for my repo so that upon a new commit and push to the repo, jenkins will then rebuild and update the application. This is to ensure that any updates are constantly being integrated into the application without the need to manually go back into jenkins and build it. This ensures the application is always progressing and keeping up to date with anything new added. \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/webhook%20.png) \
![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/webhook%20build.png)\

## Issues Encountered 
I had quite a few issues, mainly ones that were easier to fix but some that took a while. 
* I had an issue with my apt installations, I needed to change become true to become yes. 
* I kept getting errors about my python and docker versions until I declared the ansible python interpreter path in inventory.yaml
* I forgot to expose the ports in the docker compose, so the pages would load manually, but fail when it was docker composed, or built in jenkins.

## What could be Improved 
* Given more time I would have liked to have worked on the appearence of the website more.
* A database could have been used to store the previously generated books. 

![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/result%20app.png) 




