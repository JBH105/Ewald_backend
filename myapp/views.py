from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Node,Edge
from .serializers import NodeSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
def save_nodes(request):
    try:
        nodes_data = request.data  # Expecting an array of nodes

        for node in nodes_data:
            node_obj, created = Node.objects.update_or_create(
                node_id=node['id'],
                defaults={
                    'label': node['data']['label'],
                    'x_position': node['position']['x'],
                    'y_position': node['position']['y']
                }
            )

        return Response({"message": "Nodes saved successfully"}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def save_edges(request):
    try:
        edges_data = request.data  
        for edge in edges_data:
            source_node = Node.objects.get(node_id=edge['source'])
            target_node = Node.objects.get(node_id=edge['target'])

            edge_obj, created = Edge.objects.update_or_create(
                edge_id=edge['id'],
                defaults={'source': source_node, 'target': target_node}
            )

        return Response({"message": "Edges saved successfully"}, status=status.HTTP_201_CREATED)

    except Node.DoesNotExist:
        return Response({"error": "Source or target node not found"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)