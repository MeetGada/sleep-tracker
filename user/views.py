from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import uSleep
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class resgisterUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class storeSleep(ListCreateAPIView):
    queryset = uSleep.objects.all()
    # serializer_class = sleepSerializer
    serializer_class = newSleepSerializer
    permission_classes = [IsAuthenticated]

class getSleep(RetrieveUpdateDestroyAPIView):
    queryset = uSleep.objects.all()
    # serializer_class = sendSleepSerializer
    serializer_class = newSleepSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user)
        return uSleep.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        blogList = uSleep.objects.filter(user=self.request.user)
        serializer = newSleepSerializer(blogList, many=True)
        return Response(serializer.data)

class logoutUser(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        # deleting the auth token to avoid it's reuse after logging out
        user.auth_token.delete()
        return Response({'msg': 'Logged out successfully!'})


# ******* API FORMAT *******
# {
#     "id": 9,
#     "sleepStart": "2022-10-10 10:20:50",
#     "sleepEnd": "2022-10-11 21:10:25",
#     "duration": "800888",
#     "user": "Pool Loop",
#     "currentDate": "808808"
# }