#!/bin/bash

#This has been written for auto add commit and push from asus laptop to master repo
git add --all && git commit -m "Auto add, commit and push script" && git push

#This clause is for sudo push
sudo git add --all && sudo git commit -m "Auto add, commit and push script" && sudo git push
