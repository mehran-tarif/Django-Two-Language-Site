from django.db import models
from django.utils import timezone
from translated_fields import TranslatedField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Article(models.Model):
	title = TranslatedField( models.CharField(_('title'), max_length=200) )
	image = models.ImageField(_('image'), upload_to="images")
	publish = models.DateTimeField(_('publish'), default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.BooleanField(_('status'), default=False)

	class Meta:
		ordering = ['-publish']
		verbose_name = _("Article")
		verbose_name_plural = _("Articles")

	def __str__(self):
		return self.title


class SlideShow(models.Model):
	article = models.OneToOneField(Article, on_delete=models.CASCADE, verbose_name=_('Article'))
	status = models.BooleanField(_('status'), default=False)

	class Meta:
		ordering = ['-article__publish']
		verbose_name = _("Slide Show")
		verbose_name_plural = _("Slide Shows")

	def __str__(self):
		return self.article.title