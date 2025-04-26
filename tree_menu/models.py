from django.db import models
from django.urls import NoReverseMatch, reverse


class MenuItem(models.Model):
    name = models.CharField('name', max_length=100)
    parent = models.ForeignKey(
        'self',
        verbose_name='parent',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
    )
    url = models.CharField(
        'url',
        max_length=255,
        blank=True,
        help_text = 'URL или URL pattern',
    )
    menu_name = models.CharField(
        'menu name',
        max_length=100,
        help_text='Меню, к которому принадлежит этот пункт',
    )
    order = models.PositiveIntegerField('order', default=0)

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_url(self):
        if not self.url:
            return None

        try:
            return reverse(self.url)
        except NoReverseMatch:
            if not self.url.startswith('/'):
                return '/' + self.url
            return self.url

    def is_active(self, current_path):
        item_url = self.get_url()
        if not item_url:
            return False

        return (
            current_path == item_url or current_path.startswith(item_url + '/')
        )
