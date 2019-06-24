# -*- coding: utf-8 -*-


from askbot.search.postgresql import setup_full_text_search
from django.db import models, migrations
import askbot
import os.path

def init_postgresql_fts(apps, schema_editor):
    conn = schema_editor.connection
    if hasattr(conn, 'vendor') and conn.vendor == 'postgresql':
        script_path = os.path.join(
                            askbot.get_install_directory(),
                            'search',
                            'postgresql',
                            'thread_and_post_models_10032013.plsql'
                        )
        setup_full_text_search(script_path)

        script_path = os.path.join(
                            askbot.get_install_directory(),
                            'search',
                            'postgresql',
                            'user_profile_search_12192015.plsql'
                        )
        setup_full_text_search(script_path)


class Migration(migrations.Migration):

    dependencies = [
        ('askbot', '0003_auto_20151218_0909'),
    ]

    operations = [
        migrations.RunPython(init_postgresql_fts)
    ]
