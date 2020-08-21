import os
import git
import time
import csv
import sys
import shutil


print ("Please enter your input in the format : orgname/repo \n")
with open('output.csv', 'w', newline='') as csvfile:
	fieldnames = ['Name','Clone_URL','Latest_Commit_Date','Latest_Commit_Author']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

#Keep reading input from stdin
for line in sys.stdin:
	if 'Exit' == line.rstrip():
		break
	print ("\nProcessing Repo .... : " +line)
	repo_name = line.split("/")

	#checking if clone directory exists
	if os.path.exists("clone_folder"):
		shutil.rmtree("clone_folder")
	
	#Construct the repository URL for accessing 
	repo_url = "https://github.com/"+line.rstrip('\n');
	
	#Constructing the clone URL for the repository
	clone_url= repo_url+".git"
	
	#clone the repository
	repo = git.Repo.clone_from(repo_url, "clone_folder")
	headcommit = repo.head.commit
	#Fetching the latest commit time
	committime = time.strftime("%d %b %Y", time.gmtime(headcommit.committed_date))
	
	with open('output.csv', 'a', newline='') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({'Name':repo_name[1], 'Clone_URL':clone_url, 'Latest_Commit_Author': headcommit.committer.name, 'Latest_Commit_Date': committime})
	print("Processing over for Repo : " +line)
print ("***** End of Execution *******")