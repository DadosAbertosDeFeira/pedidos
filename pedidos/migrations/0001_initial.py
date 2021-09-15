# Generated by Django 3.2.6 on 2021-09-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_protocolo', models.CharField(blank=True, max_length=25, verbose_name='Número de Protocolo')),
                ('data_envio', models.DateField(db_index=True, verbose_name='Data de envio')),
                ('data_resposta', models.DateField(blank=True, db_index=True, null=True, verbose_name='Data de resposta')),
                ('orgao', models.CharField(blank=True, max_length=50, verbose_name='Órgão')),
                ('esfera', models.CharField(choices=[('municipal', 'MUNICIPAL'), ('estadual', 'ESTADUAL'), ('federal', 'FEDERAL')], max_length=20, verbose_name='Esfera')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título do Pedido')),
                ('meio_de_contato', models.CharField(max_length=200, verbose_name='Meio de Contato')),
                ('status', models.CharField(blank=True, choices=[('sem_resposta', 'SEM RESPOSTA'), ('respondido_parcialmente', 'RESPONDIDO PARCIALMENTE'), ('respondido', 'RESPONDIDO'), ('respondido_apos_recurso', 'RESPONDIDO APÓS RECURSO'), ('em_recurso', 'EM RECURSO'), ('em_andamento', 'EM ANDAMENTO'), ('respondido_com_atraso', 'RESPONDIDO COM ATRASO'), ('pedido_nao_processado', 'PEDIDO NÃO PROCESSADO')], max_length=50, verbose_name='Status do Pedido')),
                ('historico', models.TextField(blank=True, null=True, verbose_name='Historico')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('resposta', models.TextField(blank=True, null=True, verbose_name='Resposta')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
