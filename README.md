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
Feel Free To Contact Me : abdullah.ashraf.abdelraouf@gmail.com