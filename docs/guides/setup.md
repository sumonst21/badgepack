## How to get started on your local development environment.
### Prerequisites:

program | download link
--- | ---
git | https://git-scm.com/downloads
python 2.7.x | https://www.python.org/downloads/
virtualenv | https://virtualenv.pypa.io/en/stable/installation/
mysql | http://dev.mysql.com/downloads/mysql/
Microsoft Visual C++ 9.0 | https://www.microsoft.com/en-us/download/details.aspx?id=44266

### Create project directory and environment

* `mkdir badgepack && cd badgepack`
* `virtualenv env`
* `source env/scripts/activate` *Activate the environment (each time you start a session working with the code)*

*Obtain source code and clone into code directory*

* `git clone https://github.com/lestrato/badgepack.git work`
* `cd work`

*Your Directory structure will look like this:*
```
badgepack
├── work
│   ├── apps
│   │   ├── account
│   │   ├── badge
│   │   ├── base
│   │   ├── community
│   ├── docs
│   │   ├── guides
│   │   ├── project
│   │   ├── status
|   ├── media       
|   │   ├── uploads     
|   │   │   ├── badges     
│   ├── static
│   │   ├── bootstrap       
│   │   │   ├── css
│   │   │   ├── fonts
│   │   │   ├── js
│   │   ├── images
│   │   ├── templates
│   │   │   ├── account
│   │   │   ├── badge
│   │   │   ├── base
│   │   │   ├── community
|   │   │   │   ├── components
│   ├── work
├── env
```

### Install requirements
*from within badgepack/work directory*

* `pip install -r requirements.txt`

*if you're having errors installing mysql-python, consider downloading the file for your appropriate platform from here:*
* http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
* Install using: `pip install [file-name]`

### Customize local settings to your environment
* cp work/settings.py.example work/settings.py
* Edit the work/settings.py file and insert local credentials for DATABASES

### Migrate databases, build front-end components
* `./manage.py migrate`
* `./manage.py createsuperuser` or `winpty python manage.py createsuperuser` *follow prompts to create your first admin user account*

### Run a server locally for development
* `./manage.py runserver`
* Navigate to http://localhost:8000/
* Login with superuser or create new account

### Creating the admin group
* Navigate to http://localhost:8000/admin
* Login with superuser
* Navigate to http://localhost:8000/admin/auth/group/add/
* Set 'Name' as Admin
* Add privileges to Admin (recommended are add, change, delete for community and membership)
* Save

### Setting users as admins
* Navigate to http://localhost:3000/admin/auth/user/
* Select user to promote to admin
* Tick checkbox "Staff status" under 'Permissions'
* Add to group 'Admin'
* Save
