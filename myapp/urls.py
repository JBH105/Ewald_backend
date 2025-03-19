from django.urls import path
from .views import save_nodes,save_edges,get_nodes,get_edges,update_node,update_edge

urlpatterns = [
    path('save-nodes/', save_nodes, name='save_nodes'),
    path('get-nodes/', get_nodes, name='get_nodes'),
    path('update-node/<int:node_id>/', update_node, name='update_node'),
    path('save-edges/', save_edges, name='save_edges'),
    path('get-edges/', get_edges, name='get_edges'),
    path('update-edge/<str:edge_id>/', update_edge, name='update_edge'),
]
