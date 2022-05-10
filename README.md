<div id="top"></div>

<h1 align="center">Lottery Application</h1>
  <br>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="/images/python.svg" alt="python" width="100" height="100"><img src="images/4691324_flask_icon.png" alt="flask" width="100" height="100"><img src="/images/317755_badge_html_html5_achievement_award_icon.png" alt="html" width="100" height="100"><img src="/images/jinja.png" alt="jinja" width="100" height="100"><img src="images/2993785_docker_social media_icon.png" alt="docker" width="100" height="100">
</div>


1. [ Project Brief. ](#brief)
2. [ Planning. ](#planning)
3. [Risk Assessment](#risk)
4. [Presentation](#video)
5. [Technical Build Requirement](#build)
6. [Testing](#test)
7. [Automation](#automation)
8. [Issues](#issues)
9. [Future Consideration](#future)

<p align="right">(<a href="#top">back to top</a>)</p>  

<!-- ABOUT THE PROJECT -->
## Project Brief
<a name="brief"/>
The project is a containerised lottery generation application which uses 4 services.  Service one creates 6 random nnumbers between 1 and 50, Service two generates a random choice of either Wednesday or Saturday, Service three combines both services 1 and 2 and renders an HTML template.  Service four generates whether the draw is a rollover based on two conditionals (a rollover occurs when the sum of all 6 numbers is less than 150 and the day is Saturday).  The code base is held on one Virtual Machine, created in Google Cloud Platform and is containerised/built locally using Docker.   

Essentially the application is designed to demonstrate the implementation of learning gained and meets the following requirements

| Requirement | Detail |
| --- | --- |
| Trello board  | Kanban board with full expansion on user stories, use cases, tasks and issues within the project.|
| Feature Branching | Use of version control system built through a cloud based CI server |
| Webhooks | Implemntation of webhooks to trigger a Jenkins reployment when the code base is changed |
| Service Architecture | Four services must be created which send post and get requests to each other |
| Containerisation | Each Service is containerised and the built images are pushed to Docker hub |
| Orchestration | The containers must be replicated accross two VM's which are part of a Docker Swarm |
| Configuration | The project must be configured and an environment provisioned using an Ansible playbook |
| Reverse Proxy | The project must be accessible to the user via a reverse proxy server (Nginx) |

## Planning 
<p align="right">(<a href="#top">back to top</a>)</p>
<a name="planning"/>

The planning stage involved the use of Trello as a project management tool where a workboard was created to hold the User Stories and to record the progress of the various build stages of the application
<p></p>
<br />
<div align="center">
    <img src="#" alt="Logo" width="1000" height="400">
</div>

## Risk Assessment
<p align="right">(<a href="#top">back to top</a>)</p>
<a name="risk"/>

A risk assessment was generated to ensure the build process went as smoothly as possible and introduced control measures for the potentialy adverse effects of the variables identified.

<div align="center">
    <img src="images/risk.png" alt="Logo" width="1000" height="400">
</div>


<a name="video"/>

## Presentation

   <span align="center"> [![Music application](.jpg)](#link) </span>

<a name="build"/>

## Technical Build Requirements
<p align="right">(<a href="#top">back to top</a>)</p>

* [python 3 ](https://www.python.org/about/) 
* [Flask](https://flask.palletsprojects.com/en/2.1.x/?msclkid=9eb344a1b67511ec879f0992ab58cf87#user-s-guide)
* [Jinga](https://palletsprojects.com/p/jinja/)
* [mySQL](https://dev.mysql.com/doc/)
* [Google Cloud Platform](https://cloud.google.com/docs)

The app uses python3 which is a high level scripting programming language which integrates Flask as a lightweight micro-framework for developing web applications.  The HTML pages were created using Jinga which is a fast extensible templating engine.

In terms of infrastructure the database server was hosted by Google Cloud platform and used a Virtual Machine to connect mySQL to VScode where a cloned down Github hosted repository holds the source code.

<div align="center">
    <img src="images/architecture.png" alt="Logo" width="800" height="600">
</div>

## Testing
<p align="right">(<a href="#top">back to top</a>)</p>
<a name="test"/>
Once the application code was in place and the app was functioning correctly testing was implemented.  Usually the Test Driven Development would be the process to follow (i.e. writing tests before the code and writing the code so the tests pass), however as the project forms part of a wider learning and training exercise this was not an expectation.

What is a test - "In the simplest terms, a test is meant to look at the result of a particular behavior, and make sure that result aligns with what you would expect."
https://docs.pytest.org/en/7.1.x/explanation/anatomy.html

Two types of tests were implemented 
* [pytest ](https://docs.pytest.org/en/7.1.x/index.html) - tests which passed if the running code gave expected results
* [Pytest Coverage](https://pypi.org/project/pytest-cov/) - a report which indicated the percentage of which the tests covered the entirety of the code base.

## Pytest

## Test Base
Pytest essentially allowed a test application to be created which ran through all of the build steps including creating the database, tables and then adding in test data. 

## Test Views

These tests passed if executing the route functions resulted in success response codes and the asserted data from the rendered html template ( i.e. the home route had a 200 response code and the word "Music" was rendered in the home template.

## Test Data

These tests passed if executing adding data from the form to the route resulted in success response codes and the asserted data from the rendered html template 

The tests, when run would result in output to the terminal as below

<div align="center">
    <img src="#" alt="pytest" width="1000" height="500">
</div>

## Pytest Cov

When considering the combined scope of all of the individual tests the coverage report would provide a percentage.  The percentage effectively showed the extent to which the individual tests covered entired the code base.
When run the following output would be displayed in the terminal.

<div align="center">
    <img src="#" alt="pytestcov" width="1000" height="350">
</div>

The full tests can be found by clicking <a href ="#" target="blank">here </a>


## Build Automation

<p align="right">(<a href="#top">back to top</a>)</p>
<a name="automation"/>
In building this project a list of commands had to be executed in order to install the various modules and dependencies of the project.  A virtual environment had to be created and then the database connection string had to be exported before the app could be run.  Further commands were required to run the tests and also to generate the reports.  In terms of automation all of these commands could be run using <a href = "https://www.jenkins.io/">Jenkins</a>.

<div align="center">
    <img src="#" alt="jenkins logs" width="1000" height="350">
</div>

Within Jenkins a link to the github repository (hosting the source code) was made and a script with build and test stages was run.  The successfull build resulted in an hosted application which produced the following console output within Jenkins.

<div align="center">
    <img src="#" alt="jenkins_console" width="1000" height="350">
</div>
<p></p>
<div align="center">
    <img src="images/jenkins_green.PNG" alt="jenkins_tick" width="1000" height="400">
</div>


<a name="issues"/>

## Issues


<a name="future"/>

## Future Considerations

<p align="right">(<a href="#top">back to top</a>)</p>
         
## Acknowledgements
* Victoria Sacre (QA Tutor)
* general support from the friendly 22MarEnable1 cohort.

## Project by

**Simon Hart**

