from django.db import models
from django.utils.translation import ugettext_lazy as _
from meotec.base import EntityModel


class Server(EntityModel):
    hostname = models.CharField(_('Hostname'), max_length=255)

    class EntityMeta:
        possible_parents = (EntityModel,)
        possible_children = ('base_manager.models.Site',)


class Site(EntityModel):
    domain = models.CharField(_('Domain name'), max_length=255)
    repository = models.CharField(_('Repository'), max_length=255)

    class EntityMeta:
        possible_parents = (Server,)