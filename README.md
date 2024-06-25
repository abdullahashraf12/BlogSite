# Blog Application with Advanced Features (Django Based)

## Installation

To install the required dependencies for this project, run the following command:

```bash
pip install -r requirements.txt
```
## Running The Project
## In Windows
```bash
./venv/Scripts/Activate.ps1
cd BlogSite
# your Current Ip as ipconfig  get the ip and your desired Port
python manage.py runserver ip:port
```
## In Linux
```bash
source venv/Scripts/activate
cd BlogSite
# your Current Ip as ifconfig to get the ip and your desired Port

python manage.py runserver ip:port
```

## In API Pagination URL
```bash
# http://ip:port/api/posts/?items_per_page=1&page_size=2
# or apply on comments
# http://ip:port/api/comments/?items_per_page=1&page_size=2
```

## Docker
Navigate to Folder BlogSite and then do these commands in terminal (Ensure Docker Is Running Before Run These Commands)
```bash
docker-compose build
docker-compose up
```
## Test Resuults Commands
```bash
coverage run --source='.' manage.py test userauths.Test.User_Authentication_Test.AuthenticationTestCase
coverage run --source='.' manage.py test blogApp.Test.CRUD_Operations_Test.CRUDTestCase
coverage run --source='.' manage.py test blogApp.Test.Django_REST_Frameworks_APIClient_Test.APITestCase
coverage run --source='.' manage.py test blogApp.Test.ModelsTest.ModelsTestCase

coverage html

cd htmlcov
python -m http.server

```
## Checkout Testing Files 
For Details Files are (TestDetails.docx , test_results.html ) & 
you can use the commands below (Ensure Run It Inside BlogSite Folder )
```bash

coverage html
cd htmlcov
python -m http.server
```

## Deployment Instructions
Here Are Some Links That Helped In Deploying
```bash

#1st "https://www.youtube.com/watch?v=7O1H9kr1CsA" 
#2nd "https://medium.com/@chodvadiyasaurabh/deploying-a-python-django-project-on-aws-step-by-step-guide-with-commands-84ca8a4f9d6f"
#3rd "https://medium.com/code-with-muh/deploy-django-application-on-ec2-with-postgresql-s3-domain-and-ssl-setup-e21143317223" 
#4th "https://a4u.medium.com/deploy-django-with-nginx-gunicorn-and-ssl-certificate-ce7d037c7507"
```
## Feel Free To Reach Out 
Feel Free To Contact Me : abdullah.ashraf.abdelraouf@gmail.com