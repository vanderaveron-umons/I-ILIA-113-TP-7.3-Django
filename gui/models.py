from django.db import models

class Typeproduit(models.Model):
    idtypeproduit = models.AutoField(db_column='idTypeProduit', primary_key = True)  # C'est la clef primaire de TypeProduit
    nom = models.TextField(db_column='Nom')  

    class Meta:
        managed = False
        db_table = 'typeProduit'

class Produit(models.Model):
    idproduit = models.AutoField(db_column='idProduit', primary_key = True)  # C'est la clef primaire de Produit
    nom = models.TextField(db_column='Nom')  
    prixunitaire = models.IntegerField(db_column='PrixUnitaire')  
    idtypeproduit = models.ForeignKey('Typeproduit', on_delete = models.CASCADE, db_column='idTypeProduit')  # C'est une foreign key vers TypeProduit

    class Meta:
        managed = False
        db_table = 'produit'


class Client(models.Model):
    idclient = models.AutoField(db_column='idClient', primary_key = True)  # C'est la clef primaire de Client
    nom = models.CharField(db_column='Nom', max_length=255)  
    prenom = models.CharField(db_column='Prenom', max_length=255)  
    adresse = models.CharField(db_column='Adresse', max_length=255)  
    codepostal = models.TextField(db_column='CodePostal')  
    ville = models.CharField(db_column='Ville', max_length=255)  
    email = models.CharField(db_column='Email', max_length=255)  

    class Meta:
        managed = False
        db_table = 'client'


class Commande(models.Model):
    idcommande = models.AutoField(db_column='idCommande', primary_key = True)  # C'est la clef primaire de Commande
    datec = models.TextField(db_column='DateC')  
    commentaire = models.TextField(db_column='Commentaire')  
    idclient = models.ForeignKey('Client', on_delete = models.CASCADE, db_column='idClient')  # C'est une foreign key vers Client

    class Meta:
        managed = False
        db_table = 'commande'


class Detailscommande(models.Model):
    idcommande = models.ForeignKey('Commande', on_delete = models.CASCADE, db_column='idCommande', primary_key = True)  # C'est une foreign key vers Commande
    idproduit = models.ForeignKey('Produit', on_delete = models.CASCADE, db_column='idProduit')  # C'est une foreign key vers Produit
    quantite = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detailsCommande'




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



