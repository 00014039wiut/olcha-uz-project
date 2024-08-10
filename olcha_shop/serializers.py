import imghdr

from rest_framework import serializers

from olcha_shop.models import Category, Product, Comment, Image, Attribute, Group, Key, Value

from rest_framework import serializers
from django.core.files.base import ContentFile
import base64
import uuid
import imghdr


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.
    """

    def to_internal_value(self, data):
        # Check if this is a base64 string
        if isinstance(data, str):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Fix padding
            missing_padding = len(data) % 4
            if missing_padding:
                data += '=' * (4 - missing_padding)

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except (TypeError, ValueError) as e:
                self.fail('invalid_image', error=str(e))

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = f"{file_name}.{file_extension}"

            data = ContentFile(decoded_file, name=complete_file_name)

        return super().to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        if extension == "jpeg":
            extension = "jpg"
        if extension is None:
            raise serializers.ValidationError('Invalid image file type.')
        return extension


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = Category
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField('get_discounted_price')
    primary_image = serializers.SerializerMethodField('get_primary_image')
    images = ImageSerializer(many=True, read_only=True, source='products')

    attributes = serializers.SerializerMethodField('get_attributes')

    def get_attributes(self, obj):
        attributes = obj.attributes.all().values('key__key_name', 'value__value_name')
        attr_dict = {}
        for attribute in attributes:
            key = attribute['key__key_name']
            value = attribute['value__value_name']
            attr_dict[key] = value

        print(attributes)
        return attr_dict

    def get_discounted_price(self, obj):
        return obj.price - obj.price * obj.discount / 100

    class Meta:
        model = Product
        fields = '__all__'

    def get_primary_image(self, obj):
        primary_image = obj.products.filter(is_primary=True).first()
        if primary_image:
            return ImageSerializer(primary_image).data
        return None


class GroupSerializer(serializers.ModelSerializer):
    category_title = serializers.SerializerMethodField('get_category_title')
    category_slug = serializers.SerializerMethodField('get_category_slug')

    def get_category_title(self, obj):
        return obj.category.title

    def get_category_slug(self, obj):
        return obj.category.slug

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'rating', 'content', 'date', 'file', 'product']


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        exclude = ('id',)


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        exclude = ('id', )


class AttributeSerializer(serializers.ModelSerializer):
    key = serializers.SerializerMethodField('get_key')
    value = serializers.SerializerMethodField('get_value')
    product = serializers.SerializerMethodField('get_product')
    def get_key(self, obj):
        return obj.key.key_name
    def get_value(self, obj):
        return obj.value.value_name
    def get_product(self, obj):
        return obj.product.name
    class Meta:
        model = Attribute
        fields = ['id', 'key', 'value', 'product']
