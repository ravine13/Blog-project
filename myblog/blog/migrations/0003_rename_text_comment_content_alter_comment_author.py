# Generated by Django 4.2 on 2024-11-24 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0002_rename_content_comment_text_alter_comment_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="text",
            new_name="content",
        ),
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
