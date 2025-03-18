from django.db import models

# Create your models here.
class Node(models.Model):
    node_id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)  
    x_position = models.FloatField() 
    y_position = models.FloatField() 

    def __str__(self):
        return self.label
    
class Edge(models.Model):
    edge_id = models.AutoField(primary_key=True) # Stores the edge 'id'
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='source_edges')
    target = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='target_edges')

    def __str__(self):
        return f"{self.source.node_id} -> {self.target.node_id}"