# Generated by Django 4.2.1 on 2023-05-17 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookBasicInfo',
            fields=[
                ('bookID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('totScore', models.DecimalField(decimal_places=2, max_digits=15)),
                ('rateNumber', models.IntegerField()),
                ('author', models.CharField(max_length=128, null=True)),
                ('status', models.CharField(default='连载', max_length=64)),
                ('onShelf', models.BooleanField(default=True)),
                ('wordsCnt', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=64)),
                ('profile', models.TextField(null=True)),
                ('img', models.ImageField(default='', upload_to='BookImg', verbose_name='图书封面')),
                ('collections', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('img', models.ImageField(default='user_img.jpg', upload_to='UserImg', verbose_name='上传头像')),
                ('gender', models.CharField(max_length=32, null=True)),
                ('region', models.CharField(max_length=128, null=True)),
                ('motto', models.CharField(max_length=128, null=True)),
                ('birth', models.DateField(null=True)),
                ('VIPDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bookbasicinfo')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'indexes': [models.Index(fields=['userID', 'bookID'], name='api_score_userID__787187_idx')],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.IntegerField()),
                ('text', models.TextField()),
                ('visible', models.BooleanField(default=True)),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bookbasicinfo')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'indexes': [models.Index(fields=['userID', 'bookID', 'chapter'], name='api_comment_userID__c016d4_idx')],
            },
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookBasicInfo', to='api.bookbasicinfo')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'indexes': [models.Index(fields=['userID', 'bookID'], name='api_collect_userID__e5304b_idx')],
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.IntegerField()),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bookbasicinfo')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'indexes': [models.Index(fields=['userID', 'bookID'], name='api_bookmar_userID__1934b7_idx')],
            },
        ),
        migrations.CreateModel(
            name='BookContext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.IntegerField()),
                ('title', models.CharField(max_length=128, null=True)),
                ('text', models.TextField()),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bookbasicinfo')),
            ],
            options={
                'indexes': [models.Index(fields=['bookID', 'chapter'], name='api_bookcon_bookID__33cf1b_idx')],
            },
        ),
    ]
