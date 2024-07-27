# Generated by Django 5.0.6 on 2024-07-27 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_alter_category_options_alter_club_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
        migrations.AlterModelOptions(
            name='club',
            options={'verbose_name': 'Club', 'verbose_name_plural': 'Clubs'},
        ),
        migrations.AlterModelOptions(
            name='clubmeeting',
            options={'verbose_name': 'Club Meeting', 'verbose_name_plural': 'Club Meetings'},
        ),
        migrations.AlterModelOptions(
            name='step',
            options={'verbose_name': 'Step', 'verbose_name_plural': 'Steps'},
        ),
        migrations.AlterModelOptions(
            name='steplesson',
            options={'verbose_name': "Step's lesson", 'verbose_name_plural': "Step's lessons"},
        ),
        migrations.AlterModelOptions(
            name='steptest',
            options={'verbose_name': "Step's test", 'verbose_name_plural': "Step's tests"},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects'},
        ),
        migrations.AlterModelOptions(
            name='subjecttitle',
            options={'verbose_name': 'Subject title', 'verbose_name_plural': 'Subject titles'},
        ),
        migrations.AlterModelOptions(
            name='testanswer',
            options={'verbose_name': "Test's answer", 'verbose_name_plural': "Test's answers"},
        ),
        migrations.AlterModelOptions(
            name='testquestion',
            options={'verbose_name': "Test's question", 'verbose_name_plural': "Test's questions"},
        ),
        migrations.AlterModelOptions(
            name='usersubject',
            options={'verbose_name': "User's subject", 'verbose_name_plural': "User's subjects"},
        ),
        migrations.AlterModelOptions(
            name='usertestresult',
            options={'verbose_name': 'Test result', 'verbose_name_plural': 'Test results'},
        ),
        migrations.AlterModelOptions(
            name='usertoteltestresult',
            options={'verbose_name': 'Total test result', 'verbose_name_plural': 'Total test results'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
    ]
