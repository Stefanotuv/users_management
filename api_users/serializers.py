from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','name','email','password']
        extra_kwargs = {
            # adding this the ashed password is not returned
            'password':{'write_only':True}
        }

    # this function is required to avoid to save the password
    # in clear for the users register
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance