# Generated by Django 4.2.7 on 2023-11-08 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0005_alter_review_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=20)),
                ('payment_mode', models.CharField(choices=[('COD', 'Cod'), ('Online', 'Online')], default='COD', max_length=15)),
                ('payment_status', models.CharField(choices=[('Unpaid', 'Unpaid'), ('Payment Received', 'Payment Received'), ('Refunded', 'Refunded'), ('Chargeback', 'Chargeback'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Unpaid', max_length=50)),
                ('total_amount', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(default='', max_length=150)),
                ('address', models.TextField(max_length=400)),
                ('phone', models.IntegerField(default=0)),
                ('zip_code', models.CharField(default='', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('price', models.FloatField(default=0)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='order.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
            ],
        ),
    ]