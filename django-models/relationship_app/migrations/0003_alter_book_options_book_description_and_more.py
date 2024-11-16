# Generated by Django 5.1.2 on 2024-11-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add book'), ('can_change_book', 'Can change book'), ('can_delete_book', 'Can delete book')]},
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='No description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default='No description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]