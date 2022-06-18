# Generated by Django 4.0.5 on 2022-06-11 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=2048)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=2048)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=2048)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(max_length=256)),
                ('annual_ctc', models.IntegerField(default=0)),
                ('currency', models.CharField(default='INR', max_length=16)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('relevant_experience_in_months', models.IntegerField()),
                ('overall_experience_in_months', models.IntegerField()),
                ('graduation', models.CharField(max_length=256)),
                ('graduation_institute', models.CharField(max_length=1024)),
                ('post_graduation', models.CharField(max_length=256)),
                ('post_graduation_institute', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company')),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.domain')),
                ('industry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.industry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MicroSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=2048)),
                ('weight', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=2048)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill_MicroSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('weight', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('microskill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.microskill')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='micro_skills',
            field=models.ManyToManyField(through='app.Skill_MicroSkills', to='app.microskill'),
        ),
        migrations.CreateModel(
            name='MicroSkill_Prerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('microskill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.microskill')),
                ('pre_microskill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_skill', to='app.microskill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='microskill',
            name='pre_requisite',
            field=models.ManyToManyField(through='app.MicroSkill_Prerequisite', to='app.microskill'),
        ),
        migrations.AddField(
            model_name='microskill',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.skill'),
        ),
        migrations.CreateModel(
            name='JobSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('skill_type', models.CharField(max_length=256)),
                ('weight', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.job')),
                ('skill_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(through='app.JobSkills', to='app.skill'),
        ),
    ]
