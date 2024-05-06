# custom_database_backend.py

class CustomDatabaseOperations:
    def datetime_cast_date_sql(self, value):
        return f"TO_DATE('{value.year}-{value.month}-{value.day}', 'YYYY-MM-DD')"

# migration file
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('datacollection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='MyModel',
            name='pulse_type',
            field=models.CharField(max_length=100, blank=True),
        ),
   
    ]
