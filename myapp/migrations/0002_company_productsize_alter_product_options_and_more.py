# Generated by Django 4.2.6 on 2023-10-24 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='ProductSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('url', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', related_query_name='site', to='myapp.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', related_query_name='site', to='myapp.product')),
                ('productsize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', related_query_name='site', to='myapp.productsize')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='myapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='myapp.category'),
        ),
    ]
