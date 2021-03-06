# Generated by Django 3.0.7 on 2020-06-16 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Categories, unlike tags, can have a hierarchy. You might have a Jazz category, and under that have children categories for Bebop and Big Band. Totally optional.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='noobscribe_socials.Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='name')),
                ('url', models.URLField(blank=True, null=True, verbose_name='url')),
                ('thumbnail', models.URLField(blank=True, null=True, verbose_name='thumbnail')),
                ('subscriber_counter', models.PositiveIntegerField(help_text='total subscriber gained', verbose_name='subscriber counter')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='social_medias', to='noobscribe_socials.Category', verbose_name='Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='youtube_channels', to=settings.AUTH_USER_MODEL)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_noobscribe_socials.socialmedia_set+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Medias',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='YoutubeChannel',
            fields=[
                ('socialmedia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='noobscribe_socials.SocialMedia')),
                ('qrcode', models.ImageField(blank=True, editable=False, null=True, upload_to='qrcode')),
                ('channel_id', models.CharField(max_length=32, unique=True, verbose_name='channel ID')),
                ('view_counter', models.PositiveIntegerField(help_text='total view gained', verbose_name='view counter')),
                ('primary', models.BooleanField(default=False, help_text='People will subscribe and view this channel', verbose_name='Primary')),
            ],
            options={
                'verbose_name': 'youtube channel',
                'verbose_name_plural': 'youtube channels',
            },
            bases=('noobscribe_socials.socialmedia', models.Model),
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('socialmedia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='noobscribe_socials.SocialMedia')),
                ('qrcode', models.ImageField(blank=True, editable=False, null=True, upload_to='qrcode')),
                ('video_id', models.CharField(max_length=32, unique=True, verbose_name='video ID')),
                ('primary', models.BooleanField(default=False, help_text='Used as primary video campaign', verbose_name='Primary')),
            ],
            options={
                'verbose_name': 'youtube video',
                'verbose_name_plural': 'youtube videos',
            },
            bases=('noobscribe_socials.socialmedia', models.Model),
        ),
        migrations.CreateModel(
            name='TaggedMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_medias', to='noobscribe_socials.SocialMedia')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_products', to='noobscribe_socials.Tag')),
            ],
            options={
                'verbose_name': 'Tagged Media',
                'verbose_name_plural': 'Tagged Medias',
            },
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='social_medias', through='noobscribe_socials.TaggedMedia', to='noobscribe_socials.Tag', verbose_name='Tags'),
        ),
    ]
