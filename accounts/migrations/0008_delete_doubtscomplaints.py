# Generated by Django 5.0.1 on 2024-04-21 09:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_alter_teacher_user_doubtscomplaints"),
    ]

    operations = [
        migrations.DeleteModel(
            name="DoubtsComplaints",
        ),
    ]
