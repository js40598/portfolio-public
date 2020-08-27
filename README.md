# portfolio-public

To view this website visit https://portfolio-sj.herokuapp.com/

This repository is posted more likely for code reviews, 
but if you want to run it for any purpose on your localhost,
go on.


To run locally:

git clone https://github.com/js40598/portfolio-public.git
cd portfolio-public
python manage.py migrate
python manage.py loaddata fixtures/pages
python manage.py loaddata fixtures/projects
python manage.py loaddata fixtures/tasks
python manage.py loaddata fixtures/contact
python manage.py runserver localhost:8000

open localhost:8000 in your browser