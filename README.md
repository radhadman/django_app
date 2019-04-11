# Final Project.  
Medical scheduling system  

## PROGRESS:  

##### 1.(12)Adapt the django application you have been working on so far and change it so that it serves acompletely new purpose. For instance maybe it is an uber-stlye application, or a meeting roombooking system. Full marks will be awarded for creativity, originality, and depth.  

		IN PROGRESS - (Haddon)

##### 2.(4)Ensure that the application can be deployed automatically one one step using only the heattemplate and environment file. Use the following repository for ideas to get you started:https://cisgitlab.ufv.ca/201901COMP351AB1s00/heat-templates.  
		As discussed with Carl we are going to use our own phisical servers making this imposible,
		but as I Andrew discussed with him earlier this will not effect gradeing of the other sections. 

##### 3.(4)Add 2-Factor authentication to your web application.  

		IN PROGRESS - (Cuiyu)
	
##### 4.(4)Your project should ideally use two virtual machines. One is a build and test server runningJenkins and another is a production server.  

		Using phyisical machines 100% DONE - (Andrew) 
			Jekinis Server @ - 70.78.103.158:8080  
		    		Login: CisProject
		    		Password: 1Get6dog!
			Production Django Server @ - 96.48.0.114:8000  


##### 5.(4)Configure a webhook on the master branch of your webdesignproject repository so that when-ever a commit is made to the master branch, Jenkins fetches the latest code from the repositoryand deploys it to the production server  

		WEB HOOKS 100% DONE - (Andrew)
		BULDING 100% DONE - (Andrew)
		DEPLOYING TO PRODUCTION SERVER 100% DONE - (Andrew) 

##### 6.(4)Enhance your continuous integration and testing pipeline so that the Jenkins server runs unit tests on your project.  

		50% DONE - Researching implementing testing.  

##### 7.(4)Make your deployed application accessible using one of the following: ngrok, pagekite, argo(or similar technology)  
		
		100% DONE - (ANDREW)
			Start file can be found inside project, will update addresses as they change.
			http://01720553.ngrok.io/admin

##### 8.(12)Your progress along the way is just as important as the final product. Ensure that you areregularly commmitting your changes to the repository. If you have difficulties coordinatingyour changes, I recommend using different branches in the same repository. Avoid creatingmultiple new repositories. Keep the README.md file in the master branch constantly updatedabout who has done work on what aspects of the application.  

		100% DONE - Forking, working and steadily updating. 

##### 9.(8)Document your work. This is above and beyond the normal requirement to cite your sources.Use Markdown format (not html, not MS Word, not PDF, etc)  

		100% DONE - In this readme and also in line code citation.  

##### REFERENCES:  
     
    https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04
    https://stackoverflow.com/questions/17743549/recursively-add-the-entire-folder-to-a-repository#17747376
    https://stackoverflow.com/questions/45135263/class-has-no-objects-member
    http://rahmonov.me/posts/continuous-integration-and-continous-deployment-for-django-app-with-jenkins/
    https://github.com/twtrubiks/docker-jenkins-django-tutorial/blob/master/jenkins_host/docker-compose.yml
    https://wiki.jenkins.io/display/JENKINS/Docker+Compose+Build+Step+Plugin
    https://jekhokie.github.io/ubuntu/linux/jenkins/docker/container/ci/python/2018/07/14/jenkins-ci-with-python-in-docker.html
    https://raspberrypituts.com/django-raspberry-pi-tutorial/
    https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
    https://ngrok.com/docs
    
    Followed Tutorials 1:1 (As per assignment):
    
    https://docs.djangoproject.com/en/2.1/intro/tutorial01/
    https://docs.djangoproject.com/en/2.1/intro/tutorial02/
    https://docs.djangoproject.com/en/2.1/intro/tutorial03/
    https://docs.djangoproject.com/en/2.1/intro/tutorial04/
    https://docs.djangoproject.com/en/2.1/intro/tutorial05/
    https://docs.djangoproject.com/en/2.1/intro/tutorial06/
    https://docs.djangoproject.com/en/2.1/intro/tutorial07/