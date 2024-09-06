from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from django.contrib.auth.models import User
from .models import UserSocialData
from .serializers import UserSocialDataSerializer

# Define supported platforms
PLATFORMS = ["google", 'facebook', 'instagram', 'linkedin', 'youtube', 'trustpilot', 'yelp']

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def connect_social(request, platform):
    if platform not in PLATFORMS:
        return Response({"error": "Unsupported platform."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Assume we have the access token in the request data
        access_token = request.data.get('access_token')

        if not access_token:
            return Response({"error": "Access token is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Simulate fetching user data from the platform
        # In reality, you would use the platform's API to fetch user data with the access token
        user_data = {
            "username": "fetched_username",
            "email": "fetched_email@example.com",
            "profile_picture": "fetched_profile_picture_url"
        }

        # Save the data in your database
        user_social_data, created = UserSocialData.objects.get_or_create(
            user=request.user, platform=platform)
        user_social_data.data = user_data
        user_social_data.access_token = access_token
        user_social_data.save()

        serializer = UserSocialDataSerializer(user_social_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except OAuth2Error as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def disconnect_social(request, platform):
    if platform not in PLATFORMS:
        return Response({"error": "Unsupported platform."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_social_data = UserSocialData.objects.get(user=request.user, platform=platform)
        user_social_data.delete()
        return Response({"success": f"{platform} account disconnected successfully."}, status=status.HTTP_200_OK)
    except UserSocialData.DoesNotExist:
        return Response({"error": f"No connected {platform} account found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_connected_socials(request):
    user_social_data = UserSocialData.objects.filter(user=request.user)
    serializer = UserSocialDataSerializer(user_social_data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
