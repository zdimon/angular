from django.db import models
import pytils

class Page(models.Model):
    title = models.CharField(max_length=30, blank = True, default='', verbose_name = 'Name', db_index = True)
    content = models.TextField(max_length=30, blank = True, null = True)
    name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
    def __unicode__(self):
        return self.title
    def save(self, **kwargs):
        if not self.id:
            self.name_slug = pytils.translit.slugify(self.title)
        return super(Page, self).save(**kwargs)
