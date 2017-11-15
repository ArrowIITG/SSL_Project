# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 19:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0009_remove_about_us_about_us_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017, max_length=4, verbose_name='year')),
                ('semester', models.CharField(choices=[('E', 'Even Semester'), ('O', 'Odd Semester')], max_length=1)),
                ('Subject_code', models.CharField(max_length=10)),
                ('Subject', models.CharField(max_length=200)),
                ('Partners', models.CharField(help_text="please separate professor's name with commas", max_length=200)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Teach', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]