# backsoul-articles-back
Django,Graphql,cloudinary free hosting images, heroku and cloudflare.
virtualenv env
source env/bin/activate
docker-compose -f docker-compose-local up
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
