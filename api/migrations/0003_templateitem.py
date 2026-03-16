from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_template', '0002_delete_mlmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Без названия', max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('item_id', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Template Item',
                'verbose_name_plural': 'Template Items',
            },
        ),
    ]
