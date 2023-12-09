#!/bin/bash
sudo python3 /home/ubuntu/ci_cd/commit_check.py
echo "running python script.."
sleep 5
pwd
STATUS=`jq ".newCommit" json-dump.json`
echo $STATUS
if [ "$STATUS" == "true" ]; then
if [ -d /var/www/html/CI-CD_adv_rohan ]; then
  echo "Directory exists."
  cd /var/www/html/CI-CD_adv_rohan
  sudo git pull origin main
  sudo cp -f /var/www/html/CI-CD_adv_rohan/*  /var/www/html/

React

Reply

else
cd /var/www/html/
sudo git init
sudo git remote add origin https://github.com/RohanU307/CI-CD_adv_rohan.git
sudo git clone https://github.com/RohanU307/CI-CD_adv_rohan.git
sudo cp -f /var/www/html/CI-CD_adv_rohan/* /var/www/html/
fi
sleep 5
echo "Please wait! restarting nginx server.."
sudo systemctl restart nginx
echo "Nginx restarted successfully!"
fi