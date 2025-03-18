from django.urls import path
from .views import save_nodes,save_edges

urlpatterns = [
    path('save-nodes/', save_nodes, name='save_nodes'),
    path('save-edges/', save_edges, name='save_edges'),
]
