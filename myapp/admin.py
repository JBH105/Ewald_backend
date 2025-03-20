from django.contrib import admin
from .models import Node,Edge,NodeEdgeData

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('node_id', 'label', 'x_position', 'y_position')  # Show all fields in list view
    search_fields = ('node_id', 'label')  # Enable search by node_id and label
    list_filter = ('label',)  # Add filter by label

@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ('edge_id', 'source', 'target')
    search_fields = ('edge_id', 'source__node_id', 'target__node_id')
    autocomplete_fields = ['source', 'target']

@admin.register(NodeEdgeData)
class NodeEdgeDataAdmin(admin.ModelAdmin):
    list_display = ['id','data']
    