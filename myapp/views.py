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

@api_view(['GET'])
def get_nodes(request):
    try:
        nodes = Node.objects.all()
        nodes_data = [
            {
                "id": node.node_id,
                "data": {"label": node.label},
                "position": {"x": node.x_position, "y": node.y_position}
            }
            for node in nodes
        ]
        
        return Response(nodes_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_node(request, node_id):
    try:
        node = Node.objects.get(node_id=node_id)
        data = request.data

        node.label = data.get('data', {}).get('label', node.label)
        node.x_position = data.get('position', {}).get('x', node.x_position)
        node.y_position = data.get('position', {}).get('y', node.y_position)

        node.save()

        return Response({"message": "Node updated successfully"}, status=status.HTTP_200_OK)
    
    except Node.DoesNotExist:
        return Response({"error": "Node not found"}, status=status.HTTP_404_NOT_FOUND)
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
    
@api_view(['GET'])
def get_edges(request):
    try:
        edges = Edge.objects.all()
        edges_data = [
            {
                "id": edge.edge_id,
                "source": edge.source.node_id,
                "target": edge.target.node_id
            }
            for edge in edges
        ]
        
        return Response(edges_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_edge(request, edge_id):
    try:
        edge = Edge.objects.get(edge_id=edge_id)
        data = request.data

        source_node = Node.objects.get(node_id=data.get('source'))
        target_node = Node.objects.get(node_id=data.get('target'))

        edge.source = source_node
        edge.target = target_node
        edge.save()

        return Response({"message": "Edge updated successfully"}, status=status.HTTP_200_OK)
    
    except Edge.DoesNotExist:
        return Response({"error": "Edge not found"}, status=status.HTTP_404_NOT_FOUND)
    except Node.DoesNotExist:
        return Response({"error": "Source or target node not found"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
