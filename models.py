# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Client(models.Model):
    idclient = models.AutoField(db_column='idClient')  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=255)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=255)  # Field name made lowercase.
    codepostal = models.TextField(db_column='CodePostal')  # Field name made lowercase. This field type is a guess.
    ville = models.CharField(db_column='Ville', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class Commande(models.Model):
    idcommande = models.AutoField(db_column='idCommande')  # Field name made lowercase.
    datec = models.TextField(db_column='DateC')  # Field name made lowercase.
    commentaire = models.TextField(db_column='Commentaire')  # Field name made lowercase.
    idclient = models.IntegerField(db_column='idClient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commande'


class Detailscommande(models.Model):
    idcommande = models.AutoField(db_column='idCommande')  # Field name made lowercase.
    idproduit = models.IntegerField(db_column='idProduit')  # Field name made lowercase.
    quantite = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detailsCommande'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Produit(models.Model):
    idproduit = models.AutoField(db_column='idProduit')  # Field name made lowercase.
    nom = models.TextField(db_column='Nom')  # Field name made lowercase.
    prixunitaire = models.IntegerField(db_column='PrixUnitaire')  # Field name made lowercase.
    idtypeproduit = models.IntegerField(db_column='idTypeProduit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produit'


class Typeproduit(models.Model):
    idtypeproduit = models.AutoField(db_column='idTypeProduit')  # Field name made lowercase.
    nom = models.TextField(db_column='Nom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typeProduit'
