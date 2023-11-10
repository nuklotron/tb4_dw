import time
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.permissions import IsSuper, IsUser
from users.serializers import UserSerializer
from users.services import is_valid_phone, generate_passcode, send_sms, generate_invite


class LoginUserView(APIView):
    """
    APIView for checks if phone number exists in DB.
    If not, creating new user.
    After check sending SMS with passcode.
    """

    def post(self, request):
        username = request.data.get('phone')
        if not User.objects.filter(phone=username).exists():
            if is_valid_phone(username):
                new_user = User.objects.create(phone=username, invite_code=generate_invite())
                new_user.save()
            else:
                return Response({'Error': 'Wrong phone number'}, status=status.HTTP_404_NOT_FOUND)
        else:
            user = User.objects.get(phone=username)
            passcode = generate_passcode()
            user.passcode = passcode
            user.save()

            print("Login passcode -", passcode)
            # send_sms(username, passcode) # не работал сервис, вывел в принты для симуляции отправки

            time.sleep(2)
            return Response({'Done': 'Code has been sent.'}, status=status.HTTP_200_OK)


class ValidatePasscodeView(APIView):
    """
    Next step before authenticate - validating passcode.
    If passcode correct user obtain his token and getting access for user detail.
    """

    def post(self, request):
        username = request.data.get('phone')
        passcode = request.data.get('passcode')
        print("validate -", passcode)
        user = User.objects.get(phone=username)

        if user.passcode == passcode:
            user.passcode = None
            user.save()
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status=status.HTTP_200_OK)

        else:
            return Response({'Error': 'Invalid passcode.'}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(RetrieveAPIView):
    """
    User details APIView
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuper | IsUser]


class UserUpdateAPIView(UpdateAPIView):
    """
    User update APIView
    User can PUT someone's invite code, can input only once
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuper | IsUser]

    def perform_update(self, serializer):
        new_obj = serializer.save()

        if new_obj.is_invited:
            raise ValidationError({"Error": "You are already use invite code"})
        else:
            new_obj.is_invited = True
            new_obj.save()
