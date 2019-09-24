from django.db import models


class URL(models.Model):
    """
    Necesario para la integración de Bitly
    """
    bitly = models.URLField(editable=False, blank=True)

    def get_absolute_url(self):
        return "https://namespace.mx/%s/%s/" % (self.category.slug, self.slug)
