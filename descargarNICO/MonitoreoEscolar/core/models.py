from django.db import models
from django.contrib.auth.models import AbstractUser


class Administrador(models.Model):
    rut_administrador = models.IntegerField(primary_key=True)
    dv_administrador = models.CharField(max_length=1)
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25, blank=True, null=True)
    appaterno = models.CharField(max_length=25)
    apmaterno = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'administrador'


class Alumno(models.Model):
    rut_alumno = models.IntegerField(primary_key=True)
    dv_alumno = models.CharField(max_length=1)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=25, blank=True, null=True)
    appaterno = models.CharField(max_length=25)
    apmaterno = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'alumno'


class AnnoCurso(models.Model):
    rut_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    rut_profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'anno_curso'
        unique_together = (('rut_alumno', 'id_curso', 'rut_profesor'),)


class Anotacion(models.Model):
    id_anotacion = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    rut_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    tipo_anotacion = models.ForeignKey('TipoAnotacion', on_delete=models.CASCADE)
    rut_profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'anotacion'


class Apoderado(models.Model):
    rut_apoderado = models.IntegerField(primary_key=True)
    dv_apoderado = models.CharField(max_length=1)
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25, blank=True, null=True)
    appaterno = models.CharField(max_length=25)
    apmaterno = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'apoderado'


class ApoderadoAlumno(models.Model):
    rut_apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE)
    alumno_rut_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    class Meta:
        db_table = 'apoderado_alumno'
        unique_together = (('rut_apoderado', 'alumno_rut_alumno'),)


class Asignatura(models.Model):
    id_asignatura = models.CharField(max_length=10)
    nombre_asignatura = models.CharField(max_length=25)

    class Meta:
        db_table = 'asignatura'
        unique_together = (('id_asignatura', 'nombre_asignatura'),)


class AsignaturaCurso(models.Model):
    curso_id_curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nombre_asignatura = models.CharField(max_length=25)
    id_nota = models.ForeignKey('Nota', on_delete=models.CASCADE)

    class Meta:
        db_table = 'asignatura_curso'
        unique_together = (('id_asignatura', 'nombre_asignatura', 'curso_id_curso'),)


class AsignaturaProfesor(models.Model):
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nombre_asignatura = models.CharField(max_length=25)
    profesor_rut_profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'asignatura_profesor'
        unique_together = (('id_asignatura', 'nombre_asignatura', 'profesor_rut_profesor'),)


class Asistencia(models.Model):
    id_asistencia = models.CharField(max_length=25, primary_key=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=20)
    alumno_rut_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    class Meta:
        db_table = 'asistencia'


class Curso(models.Model):
    id_curso = models.CharField(max_length=25, primary_key=True)
    seccion = models.CharField(max_length=25)
    anno_generacion = models.IntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        db_table = 'curso'

    def __str__(self):
        return self.seccion      


class Nota(models.Model):
    id_nota = models.CharField(max_length=15, primary_key=True)
    calificacion = models.FloatField()
    alumno_rut_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota_1 = models.FloatField()
    nota_2 = models.FloatField()
    nota_3 = models.FloatField()
    nota_4 = models.FloatField()
    promedio = models.IntegerField()
    nota_5 = models.FloatField(blank=True, null=True)
    nota_6 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'nota'


class Profesor(models.Model):
    rut_profesor = models.IntegerField(primary_key=True)
    dv_profesor = models.CharField(max_length=1)
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25, blank=True, null=True)
    appaterno = models.CharField(max_length=25)
    apmaterno = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'profesor'


class TipoAnotacion(models.Model):
    id_anotacion = models.AutoField(primary_key=True)
    positiva = models.CharField(max_length=1, blank=True, null=True)
    negativa = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'tipo_anotacion'

class Usuario(AbstractUser):
    rut_usuario = models.CharField(max_length=25, unique=True, primary_key=True)
    dv_usuario = models.CharField(max_length=1)

    # Meta
    class Meta:
        db_table = 'usuario'

    # Representación del usuario por RUT
    def __str__(self):
        return f"{self.rut_usuario}-{self.dv_usuario}"

    # Evitar conflicto de nombre para los grupos y permisos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Cambia el nombre inverso
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='usuario',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_set',  # Cambia el nombre inverso
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuario',
    )

    