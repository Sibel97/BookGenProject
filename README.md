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

(https://raw.githubusercontent.com/Sibel97/BookGenProject/main/Read-me%20images/Book-Gen.png)

## Jira : Planning 
For this project Jira was used to manage the workflow, creating a backlog of tasks that needed to be created, as well as user stories. For each of these tasks, a priorty was set based on its importance to the project, and a story point was assigned based on how difficult of a task it would be to implement. This again allowed me a better understanding of what needed to be done and the best way to divide the project into sprints. 
(INSERT PICTURE OF BACKLOG)

Once the sprints were created with their allocated tasks, it was moved onto a kanban board where I could keep track of the tasks that were in progress, which were completed and which were yet to be started. Again this just allowed for further planning and tracking of the development of the project. 

(INSERT PICTURE OF BOARD)

Using Jira and the built-in attributes you can allocated to tasks and sprints allowed me to keep track of the number of story points in total the project had and compare this to the days I had to complete the assignment. This allowed me to created an expected burndown of my story points in relation to time, keeping track of my progress I was then able to include my actual burndown progress. Overall, there were quite a few deviations to the expected burndown, either because of issues faces prolonging the task or some running smoother than expected but overall the project was completed on time. 

(INSERT PICTURE OF BURNDOWN CHART)


## Risk Assessment : Planning 

(INSERT RISK ASSESSMENT PICTURE)

This risk assessment details some of the possible risks that may have been encountered when completeing these products, mainly the issues that were possible would be down to poor planning or design on my end, or mainly issues with GCP, Jenkins, Ansible and docker as these are the biggest contributing factors to the project, the python is key but simple in comparrison. The risk assessment breaks down what may happen, the outcome, who is responsible, how detrimental the error would be if occured, probablity, response and preventative measures. Identifying these issues before they occur allows for better control of issues when and if they arise duing the project timeframe. 

## Version Control System : Feature-Branch Model 

## Virtual Machines : GCP

## The Application : Service-oriented Architecture 

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





