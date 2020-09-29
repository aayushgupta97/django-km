# Generated by Django 2.0.5 on 2020-09-28 18:21

from django.db import migrations


def save_data_to_model(apps, schema_editor):
    Post = apps.get_model("posts", "Post")
    data = [
        {
            "title": "Title 1",
            "message": "Message 1"
        },
        {
            "title": "Title 2",
            "message": "Message 2"
        },
        {
            "title": "Title 3",
            "message": "Message 3"
        }
    ]

    for post_data in data:
        Post.objects.create(**post_data)


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(save_data_to_model),
    ]
