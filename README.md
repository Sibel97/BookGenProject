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

![](https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/gcp%20vms.png)

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

### Roles 
### Playbook
### Inventory 

## Docker : Containerisation

### Dockerfiles 
### Building images
### Docker-compose
#### Docker swarm stack : Orchestration Tool

## NGINX : Reverse Proxy

## Testing : Mock Testing/ Unit Tests

## CI Server : Jenkins 

### Pipeline

#### Run Tests
#### Build and push images 
#### Deploy app
#### Print testing reports 

## Continuous Integration : Webhooks

## Issues Encountered 

## What could be Improved 





