#!/bin/bash

##This has been written for auto add commit and push from asus laptop to master repo
#git add --all && git commit -m "Auto add, commit and push script" && git push

##This clause is for sudo push
#sudo git add --all && sudo git commit -m "Auto add, commit and push script" && sudo git push

git add --all && git commit -m "Auto add, commit and push script" && git push
#If exit code returns '1' (operation not permitted) then...
#echo "$?"
if ["$?" -eq "128"]
then
  echo "Sudoless command successful"
else
  echo "Sudoless command failed, now running as root"
  sudo git add --all && sudo git commit -m "Auto add, commit and push script" && sudo git push
fi


