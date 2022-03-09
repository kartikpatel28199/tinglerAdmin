# Generated by Django 3.2.9 on 2022-03-09 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'User'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='interest',
            new_name='interests',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=45, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.CharField(max_length=45)),
                ('longitude', models.CharField(max_length=45)),
                ('isGlobal', models.CharField(max_length=2)),
                ('distanceRange', models.CharField(max_length=45)),
                ('showMe', models.IntegerField(choices=[(1, 'On'), (0, 'Off')], default=0)),
                ('tinglerAlert', models.IntegerField(choices=[(1, 'On'), (0, 'Off')], default=0)),
                ('showProfilePic', models.IntegerField(choices=[(1, 'On'), (0, 'Off')], default=0)),
                ('age_min', models.IntegerField()),
                ('age_max', models.IntegerField()),
                ('showActivityStatus', models.IntegerField(choices=[(1, 'On'), (0, 'Off')], default=0)),
                ('distanceType', models.CharField(choices=[('Km', 'Km'), ('Mi', 'Km')], max_length=5)),
                ('notification', models.CharField(max_length=45)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('deletedAt', models.DateTimeField()),
                ('userId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.user')),
            ],
            options={
                'verbose_name_plural': 'User Setting',
                'db_table': 'user_setting',
            },
        ),
    ]