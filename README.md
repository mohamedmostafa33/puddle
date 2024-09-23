


## Commands Used to Resolve the Issues


1. **Resetting Migrations and Reapplying**  
   Commands:
   ```bash
    pip install Pillow
    pip list | grep Pillow
   ```
   Purpose: Installing Pillow a Python Imaging Library.

2. **Makemigrations and Migrate**  
   Command:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   Purpose: Creates and applies database migrations to ensure all models have corresponding tables in the database.

3. **Checking Migration Status**  
   Command:
   ```bash
   python manage.py showmigrations
   ```
   Purpose: Displays the current migration status to identify any pending migrations.



5. **Creating Superuser**  
   Command:
   ```bash
   python manage.py createsuperuser
   ```
   Purpose: Creates a new admin user for accessing the Django admin site.

6. **To Run The Project**  
   Command:
   ```bash
   python manage.py runserver
   ```
   Purpose: Start the server."# django_web_application" 
"# django_web_application" 
