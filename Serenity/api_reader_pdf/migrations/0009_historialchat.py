# Generated by Django 4.2.2 on 2023-06-29 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_reader_pdf', '0008_embedding_identificador'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historial', models.TextField(default='[]')),
                ('id_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_reader_pdf.embedding')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
