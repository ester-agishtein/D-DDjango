# D&amp;D Django Project
This is a Django project for D&amp;D. Using Django, this project provides a database for charecter and team information, as well as a dice roller. 
The charecter and team forms save data to a sqlite3 database for the convenience of the DM. 
This project is hosted on AWS on an Ubuntu server and is served using Apache. 
[You can check out the live project here](http://ec2-18-216-88-37.us-east-2.compute.amazonaws.com/). 

# Technologies
  - Django/Python
  - AWS EC2
  - Apache
  - HTML5
  - CSS/Bootstrap
  
# Running locally
  - Create a folder to store the project.
  - If you do not already have a virtual environment, create one: `sudo pip3 install virtualenv`.
  - Clone the repo: `git clone https://github.com/ester-agishtein/D-DDjango.git`.
  - Activate the virtual environment: `source myprojectenv/bin/activate`.
  - Change into the project directory: `cd D-DDjango\esaPythonPortfolio`.
  - Install the necessary requirements: `pip install -r requirements.txt`.
  - Run migrations: 
    - `python manage.py makemigrations`
    - `python manage.py migrate`
    - `python manage.py collectstatic`
    - `python manage.py runserver 0.0.0.0:8000`
    
 # About the project:
 
  <ins> Teams </ins> 
  
  Teams represent groupings of charecters. A DM can use the feature as a way of marking charecters to be part of a campaign, or to create a group of monsters or NPCs.  
    
 <ins> Charecters </ins> 
  
   Charecters represent a charecter, monster, or NPC. The DM can fill out their stats, alignment, and include any notes they have on the charecters. 


  
