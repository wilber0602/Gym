from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    id_rol = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.SET_NULL)
    id_coach = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    # Evitar conflictos con auth.User
    groups = models.ManyToManyField(
        Group,
        related_name="usuario_groups",
        blank=True,
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuario_user_permissions",
        blank=True,
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username


class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion_dias = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Membresia(models.Model):
    id_membresia = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_plan = models.ForeignKey(Plan, on_delete=models.RESTRICT)
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('vencida', 'Vencida'),
    ]
    estado = models.CharField(max_length=7, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"Membresía {self.id_membresia} - {self.estado}"


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=50)

    def __str__(self):
        return f"Pago {self.id_pago} - {self.monto}"


class Ejercicio(models.Model):
    id_ejercicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    calorias_por_unidad = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    grupo_muscular = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    id_rutina = models.AutoField(primary_key=True)
    id_coach = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Rutina_Ejercicio(models.Model):
    id_rutina_ejercicio = models.AutoField(primary_key=True)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.RESTRICT)
    series = models.IntegerField()
    repeticiones = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.id_rutina.nombre} - {self.id_ejercicio.nombre}"

class Rutina_Dia_Ejercicio(models.Model):
    DIAS_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
    ]

    id_rutina_dia_ejercicio = models.AutoField(primary_key=True)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    dia = models.CharField(max_length=9, choices=DIAS_CHOICES)
    id_ejercicio = models.ForeignKey(
        Ejercicio, on_delete=models.SET_NULL, null=True, blank=True
    )
    nombre_ejercicio = models.CharField(max_length=100, blank=True, null=True)
    series = models.IntegerField(blank=True, null=True)
    repeticiones = models.IntegerField(blank=True, null=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    orden = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id_rutina.nombre} - {self.dia} - {self.nombre_ejercicio or (self.id_ejercicio.nombre if self.id_ejercicio else '')}"


class Registro_Entrenamiento(models.Model):
    id_registro = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.RESTRICT)
    fecha = models.DateField()
    series_realizadas = models.IntegerField(blank=True, null=True)
    repeticiones_realizadas = models.IntegerField(blank=True, null=True)
    peso_usado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Registro {self.id_registro} - {self.id_usuario.nombre} - {self.fecha}"
