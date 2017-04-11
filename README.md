# ClassGotcha-Backend

## Set up

### Clone
```
> git clone https://github.com/C0deZLee/ClassGotcha-Backend.git
> cd ClassGotcha-Backend
```
### Checkout to dev branch

```
> git checkout dev
```

### Create local folder for temp database and virtual env

```
mkdir local/tmp
```

### Virtual Env
(Why Virtual Env? [Check this](https://www.davidfischer.name/2010/04/why-you-should-be-using-pip-and-virtualenv/))
```
> virtualenv env
> source env/bin/activate
```
### Install Dependencies

```
> pip install -r requirements.txt
```

### Migrate database

```
> python manage.py makemigrations
> python manage.py migrate
```

### Create Superuser

```
> python manage.py createsuperuser
```

### Run local server

```
> python manage.py runserver
```
