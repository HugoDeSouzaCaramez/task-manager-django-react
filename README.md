docker-compose up --build

docker-compose exec taskmanager python manage.py makemigrations

docker-compose exec taskmanager python manage.py migrate 

docker-compose exec taskmanager python manage.py loaddata seed_data.json

docker-compose exec taskmanager python manage.py seed

docker-compose exec taskmanager python manage.py test

npm run start