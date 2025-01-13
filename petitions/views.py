from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Petition, Vote
from .serializers import PetitionSerializer, VoteSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PetitionViewSet(viewsets.ModelViewSet):
    queryset = Petition.objects.all()
    serializer_class = PetitionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'created_at']


class VoteViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        user = request.user
        petition_id = request.data.get('petition_id')
        try:
            petition = Petition.objects.get(id=petition_id)
        except Petition.DoesNotExist:
            return Response({"error": "Petition not found"},
                            status=status.HTTP_404_NOT_FOUND)

        if Vote.objects.filter(user=user, petition=petition).exists():
            return Response(
                {"error": "You have already voted for this petition."},
                status=status.HTTP_400_BAD_REQUEST)

        Vote.objects.create(user=user, petition=petition)
        petition.votes_count += 1
        petition.save()

        return Response({"message": "Vote added successfully."},
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        user = request.user
        try:
            vote = Vote.objects.get(id=pk, user=user)
        except Vote.DoesNotExist:
            return Response(
                {"error": "Vote not found or you do not have permission to delete it."},
                status=status.HTTP_404_NOT_FOUND)

        petition = vote.petition
        vote.delete()
        petition.votes_count -= 1
        petition.save()

        return Response({"message": "Vote removed successfully."},
                        status=status.HTTP_200_OK)
