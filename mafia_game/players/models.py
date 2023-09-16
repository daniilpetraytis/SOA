from django.db import models
from serializable.models import Serializable


class Player(Serializable):
    serialized_attributes = (
        'id',
        'nickname',
        'sex',
        'email'
    )

    nickname = models.CharField(max_length=100,
                                null=False,
                                blank=False)

    avatar = models.ImageField(upload_to='images/')

    sex = models.CharField(max_length=10,
                           null=False,
                           blank=False)
    
    email = models.EmailField(max_length = 254)
