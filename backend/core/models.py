from django.db import models

# import dependencies for abstract model classes
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

# create a Contact model and inherit abstract model classes
# 'TimeStampedModel' - adds fields for creation and modification timestamps to the model.
# 'ActivatorModel' - adds fields for activation status to the model.
# 'TitleDescriptionModel' - adds fields for title and description to the model.
# 'Model' - an abstract model defined in a separate module that adds some utility methods for querying the model
class Contact(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):

	# The Meta class is used to provide additional options for the model, in this case setting the verbose_name_plural attribute to "Contacts", which will be used in the admin interface to describe multiple instances of the model.
	class Meta:
		verbose_name_plural = "Contacts"

	# add a email field to the model
	email = models.EmailField(verbose_name="Email")

	# this method is defined to return a string representation of the Contact object, which is based on the title field. When a Contact object is printed or displayed in the admin interface, this method will be used to generate the string representation.
	def __str__(self):
		return f'{self.title}'