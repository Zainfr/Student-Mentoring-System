# Generated by Django 5.0.1 on 2024-04-21 16:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0010_attendance_marks_delete_studentmessage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="marks",
            name="student",
        ),
        migrations.DeleteModel(
            name="Attendance",
        ),
        migrations.DeleteModel(
            name="Marks",
        ),
    ]
