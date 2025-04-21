# Student API with Django

## Endpoints

- `/students/`: Returns a list of students from the database
- `/subjects/`: Returns all subjects grouped by year

## Setup Instructions

1. Clone the repo
2. Run `python -m venv env && source env/bin/activate` (or `env\Scripts\activate` on Windows)
3. Run `pip install -r requirements.txt`
4. Run `python manage.py migrate`
5. Run `python manage.py createsuperuser`
6. Run `python manage.py runserver`




## Bash Scripts (Assignment 2)

This project includes three bash scripts located in the `bash_scripts/` directory.

### Scripts Overview

- **health_check.sh**  
  Checks server health (disk usage, CPU load, memory usage, and running processes). Logs output to `/var/log/server_health.log`.

- **backup_api.sh**  
  Backs up the API project directory and SQLite database. Deletes backups older than 7 days. Logs to `/var/log/backup.log`.

- **update_server.sh**  
  Updates system packages, pulls the latest code from Git, and restarts the web server. Logs to `/var/log/update.log`.

### Setup Instructions

1. Set execute permissions:
   ```bash
   chmod +x bash_scripts/*.sh
