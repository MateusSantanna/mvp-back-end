from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from bson import ObjectId
from .mongo import events_collection


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def list_events(request):

    if request.method == 'GET':

        events = []

        for event in events_collection.find():

            events.append({
                "id": str(event["_id"]),
                "titulo": event["titulo"],
                "data": event["data"],
                "hora": event["hora"],
                "local": event["local"],
                "tipo_atividade": event["tipo_atividade"],
                "imagem": event["imagem"],
                "descricao": event["descricao"]
            })

        return Response(events)

    if request.method == 'POST':

        data = request.data

        new_event = {
            "titulo": data.get("titulo"),
            "data": data.get("data"),
            "hora": data.get("hora"),
            "local": data.get("local"),
            "tipo_atividade": data.get("tipo_atividade"),
            "imagem": data.get("imagem"),
            "descricao": data.get("descricao")
        }

        result = events_collection.insert_one(new_event)

        return Response({
            "message": "Evento criado com sucesso",
            "id": str(result.inserted_id)
        })
    

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def event_detail(request, id):

    if request.method == 'GET':

        event = events_collection.find_one({"_id": ObjectId(id)})

        if not event:
            return Response({"erro": "Evento não encontrado"}, status=404)

        return Response({
            "id": str(event["_id"]),
            "titulo": event["titulo"],
            "data": event["data"],
            "hora": event["hora"],
            "local": event["local"],
            "tipo_atividade": event["tipo_atividade"],
            "imagem": event["imagem"],
            "descricao": event["descricao"]
        })


    if request.method == 'PUT':

        data = request.data

        events_collection.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "titulo": data.get("titulo"),
                    "data": data.get("data"),
                    "hora": data.get("hora"),
                    "local": data.get("local"),
                    "tipo_atividade": data.get("tipo_atividade"),
                    "imagem": data.get("imagem"),
                    "descricao": data.get("descricao")
                }
            }
        )

        return Response({"message": "Evento atualizado com sucesso"})


    if request.method == 'DELETE':

        events_collection.delete_one({"_id": ObjectId(id)})

        return Response({"message": "Evento removido com sucesso"})