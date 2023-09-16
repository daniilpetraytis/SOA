from django.db import models


def _cut_level(requested, key):
    result = list()
    for req in requested:
        if req.startswith("%s__" % key):
            result.append(req.split('__', 1)[1])
        if req.startswith("-%s__" % key):
            result.append("-" + req.split('__', 1)[1])
    return result


def query_filter(available, requested):
    available = set(available)
    include = set()
    exclude = set()
    for req in requested:
        if "__" not in req:
            if req.startswith('-'):
                exclude.add(req[1:])
            else:
                include.add(req)
        else:
            if not req.startswith('-'):
                include.add(req.split('__', 1)[0])
    if len(include) == 0:
        filtered = available
    else:
        filtered = available.intersection(include)
    filtered = {req: _cut_level(requested, req) for req in filtered.difference(exclude)}
    return filtered


class SerializableQuerySet(models.QuerySet):
    def serialize(self, *args):
        return [obj.serialize(*args) for obj in self]


class SerializableManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return SerializableQuerySet(self.model, using=self._db)

    def serialize(self, *args):
        return self.get_queryset().serialize(*args)


class Serializable(models.Model):
    class Meta:
        abstract = True

    objects = SerializableManager()
    serialized_attributes = []

    def _serialize_attributes(self, serializable, *requested, parsed=None):
        if parsed is None:
            ser_attributes = query_filter(serializable, requested)
        else:
            ser_attributes = parsed
        ser_data = {}
        for attr in ser_attributes:
            value = getattr(self, attr)
            if hasattr(value, 'serialize'):
                ser_data[attr] = value.serialize(*ser_attributes[attr])
            else:
                ser_data[attr] = value
        return ser_data

    def _serialize(self, *args, parsed=None):
        return self._serialize_attributes(self.serialized_attributes, *args, parsed=parsed)

    def serialize(self, *args):
        return self._serialize(*args)
