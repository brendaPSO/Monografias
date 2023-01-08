# Monografias

* Instale os requirements com o comando:
* pip3 install -r requirements.txt

* Em seguida faça as migrações: 
* python manage.py makemigrations
* ./manage.py migrate

* Execute o projeto:
* python manage.py runserver

# Caso ocorra o erro ModuleNotFoundError: No module named 'psycopg2':

* Execute o seguinte comando:
* pip install psycopg2-binary

# Caso ocorra o erro ModuleNotFoundError: No module named 'Tkinter':

* Execute o seguinte comando:
* sudo apt-get install python3-tk

# Caso ocorra o erro ModuleNotFoundError: No module named 'django-filters'

* Execute o seguinte comando:
* pip install django-filter