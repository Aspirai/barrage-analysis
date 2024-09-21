#序列化容器
from rest_framework import serializers

from ai.models import Barrage

# serializer 类需要继承 serializers.Serializer，
# 然后实现父类的 update，create 方法
class BarrageSerializer(serializers.ModelSerializer):
    # 声明需要被序列化和反序列化的字段，同 model 的字段，
    # 字段名注意需要同 model 字段同名
    rood_id = serializers.IntegerField
    name = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=1024)
    nature_of_words = serializers.CharField(max_length=255)

    class Meta:
        model = Barrage
        fields = '__all__'

from ai.models import Admin
class AdminSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length=64)
    pass_word = serializers.CharField(max_length=64)
    user_email = serializers.CharField(max_length=255)

    class Meta:
        model = Admin
        fields = '__all__'

from ai.models import Room
class RoomSerializer(serializers.ModelSerializer):
    rood_id = serializers.IntegerField

    class Meta:
        model = Room
        fields = '__all__'
