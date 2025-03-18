from rest_framework import serializers
from .models import Node,Edge

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['node_id', 'label', 'x_position', 'y_position']

class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = ['edge_id', 'source', 'target']