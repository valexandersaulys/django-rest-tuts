from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# Create a User serializer as an endpoint for our API
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


# Pull up a model serializers to simplify our code
class SnippetSerializer(serializers.ModelSerializer):
    '''Make sure to associate snippets with the users who create them'''
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html' )

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title',
            'code', 'linenos', 'language', 'style', 'owner')

"""
# Manual way of doing serializers
class SnippetSerializer(serializers.Serializer):
    '''We specify our serializers, which are like fields
        in a form class.'''
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        '''
        Create and return a new 'Snippet' model instance given validated data
        '''
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''
        Update & return an existing 'Snippet' `instance` given
        `validated_data`
        '''
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
"""
