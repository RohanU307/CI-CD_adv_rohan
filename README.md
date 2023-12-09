# CI-CD_adv_rohan
CI-CD advanced project repo
**Task 1: Set Up a Simple HTML Project 
Create a simple HTML project and push it to a GitHub repository.**
I have made a simple index.html file to get the webpage which has the backgroud image and some info about my social media and then I have pushed it to the repo.

Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx
I have created an instance named CI-CD-Rohan-Shree as we were both working in a team and installed nginx server on that instance and allowed the ports necessary.

Task 3: Write a Python Script to Check for New Commits
 Create a Python script to check for new commits using the GitHub API.
Shree came up with the python script for fetching the details of repo and new commits and it was generating the json file b setting the value as true/false according to the commits. If there is a new commit then the value would be true and if not then it will set it as false. The python file name is commit_check.py and it will generate the file named json_dump.json

Task 4: Write a Bash Script to Deploy the Code
Create a bash script to clone the latest code and restart Nginx.
I made the bash script in Linux VM I have in my laptop named filescript.sh. First it will run the python script to check for commits. Basically it checks the file which is created by the python script and it will save the json value in the variable named STATUS. If the status is true then it will check whether the folder is already there or not. If ther folder is already created means the repo is already cloned then it will simply pull the latest commits to local otherwise it will clone the repo after initializing git. In both cases we are restarting the nginx server. 

Task 5: Set Up a Cron Job to Run the Python Script
Create a cron job to run the Python script at regular intervals.
We have setup the cronjob for every 5 minutes. The script will run every 5 minutes and if there is any new commit then it will pull the latest changes from the repo and then pull them in EC2 instance.
*/5 * * * * /home/ubuntu/ci_cd/filescript.sh this is the cronjob we have setup.

Overall we have tested the setup and it works fine. I have also shared the website picture.







