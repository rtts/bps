from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pandocfield.fields

class Migration(migrations.Migration):

    dependencies = [
        ('autodidact', '0007_auto_20170308_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'ordering': ['file'],
            },
        ),
        migrations.CreateModel(
            name='StepFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='autodidact.Step')),
            ],
            options={
                'ordering': ['file'],
            },
        ),
        migrations.RemoveField(
            model_name='tag',
            name='content_type',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='programmes',
            new_name='programs',
        ),
        migrations.AddField(
            model_name='programme',
            name='_description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='programme',
            name='degree',
            field=models.PositiveIntegerField(choices=[(10, 'Bachelor'), (20, 'Pre-master'), (30, 'Master')], default=10),
        ),
        migrations.AddField(
            model_name='programme',
            name='description',
            field=pandocfield.fields.PandocField(auto_create_html_field=False, blank=True),
        ),
        migrations.AddField(
            model_name='programme',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='pagefile',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='autodidact.Page'),
        ),
    ]
