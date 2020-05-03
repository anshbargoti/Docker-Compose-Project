import os

os.system("tput setaf 1")
print("\n\t\t\t----------------")
print("\t\t\t Welcome to TUI")
print("\t\t\t----------------")
os.system("tput setaf 4")


while True:
  print("""
  Press 1: Launch Wordpress Infrastructure
  Press 2: Lauch Owncloud Infrastructure
  Press 3: Remove Wordpress Infrastructure
  Press 4: Remove Owncloud Infrastructure
  Press 5: Exit
  """)
  os.system("tput setaf 6")
  print("Enter your choice : ",end="")
  ch=input()
  os.system("tput setaf 7")
  if int(ch)==1:
      os.chdir("/wordpress/")
      os.system("docker-compose up -d")
  elif int(ch)==2:
      os.chdir("/owncloud/")
      os.system("docker-compose up -d")
  elif int(ch)==3:
      os.chdir("/wordpress/")
      os.system("docker-compose stop")
      os.system("docker-compose rm")
  elif int(ch)==4:
      os.chdir("/owncloud/")
      os.system("docker-compose stop")
      os.system("docker-compose rm")
  elif int(ch)==5:
      exit()
