# Generated by Django 2.1.4 on 2019-01-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20181123_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='source',
            field=models.CharField(choices=[('local', 'Local'), ('ldap', 'LDAP/AD'), ('openid', 'OpenID'), ('radius', 'Radius')], default='local', max_length=30, verbose_name='Source'),
        ),
    ]
