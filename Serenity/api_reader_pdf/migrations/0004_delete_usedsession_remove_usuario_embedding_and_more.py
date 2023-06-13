# Generated by Django 4.2.2 on 2023-06-12 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_reader_pdf', '0003_usedsession'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UsedSession',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='embedding',
        ),
        migrations.AddField(
            model_name='embedding',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='embeddings', to=settings.AUTH_USER_MODEL),
        ),
    ]
