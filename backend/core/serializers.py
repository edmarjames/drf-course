from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class ContactSerializer(serializers.ModelSerializer):

	# 'name' is a CharField that is mapped to the 'title' field of the Contact model.
	name = CharField(source="title", required=True)
	# 'message' is also a CharField that is mapped to the 'description' field of the Contact model.
	message = CharField(source="description", required=True)
	# 'email' is an EmailField that is required and mapped to the email field of the Contact model.
	email = EmailField(required=True)
	

	# The Meta class is used to specify that the model attribute of the ContactSerializer is the Contact model imported from another module.
	class Meta:
		model = models.Contact

		# fields attribute is a tuple of fields to be included in the serialized output, which in this case are the name, email, and message fields.
		fields = (
			'name',
			'email',
			'message'
		)