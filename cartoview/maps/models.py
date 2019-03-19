from django.db import models
from cartoview.layers.validators import validate_projection
from django.contrib.postgres.fields import ArrayField, JSONField
from django.core.validators import MaxValueValidator, MinValueValidator
from cartoview.layers.models import Layer


class Map(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    bounding_box = ArrayField(models.DecimalField(
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True), size=4, null=True, blank=True)
    projection = models.CharField(
        max_length=30,
        blank=False,
        null=False, validators=[validate_projection, ], default="EPSG:3857")
    center = models.CharField(
        max_length=150, null=False, blank=False, default="[0,0]")
    constrain_rotation = models.BooleanField(default=True)
    enable_rotation = models.BooleanField(default=True)
    max_zoom = models.IntegerField(default=28, validators=[
        MaxValueValidator(28),
        MinValueValidator(0)
    ])
    min_zoom = models.IntegerField(default=0, validators=[
        MaxValueValidator(28),
        MinValueValidator(0)
    ])
    zoom_factor = models.IntegerField(default=2, validators=[
        MaxValueValidator(28),
        MinValueValidator(1)
    ])
    zoom = models.IntegerField(default=6, validators=[
        MaxValueValidator(28),
        MinValueValidator(1)
    ])
    rotation = models.IntegerField(null=False, blank=False, default=0)
    layers = models.ManyToManyField(Layer)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    render_options = JSONField(default=dict, null=False, blank=True)

    class Meta:
        ordering = ('title', '-created_at', '-updated_at')
