import accounts.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=11)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('product_list', models.JSONField(default=accounts.models.User.default_product_list)),
                ('finance_type', models.CharField(choices=[('saver', '저축형'), ('investor', '투자형'), ('spender', '소비형'), ('planner', '안정형')], default='planner', max_length=20)),
                ('gender', models.CharField(choices=[('male', '남성'), ('female', '여성')], default='male', max_length=10)),
                ('marriage', models.CharField(choices=[('single', '미혼'), ('married', '기혼')], default='single', max_length=10)),
                ('income_prospect', models.CharField(choices=[('stable_increase', '안정적 증가'), ('unstable', '불안정'), ('decreasing', '감소')], default='stable_increase', max_length=20)),
                ('asset_level', models.CharField(choices=[('below_10m', '1천만 원 이하'), ('10m_to_50m', '1천만~5천만 원'), ('50m_to_100m', '5천만~1억 원'), ('100m_to_500m', '1억~5억 원'), ('500m_to_1b', '5억~10억 원'), ('above_1b', '10억 원 이상')], default='below_10m', max_length=20)),
                ('income_level', models.CharField(choices=[('below_30m', '3천만 원 이하'), ('30m_to_50m', '3천만~5천만 원'), ('50m_to_70m', '5천만~7천만 원'), ('70m_to_100m', '7천만~1억 원'), ('100m_to_300m', '1억~3억 원'), ('above_300m', '3억 원 이상')], default='below_30m', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
