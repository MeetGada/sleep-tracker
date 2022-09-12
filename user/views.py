from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.http import JsonResponse
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

    def perform_update(self, serializer):
        validated_data = self.request.data
        sleepStart = datetime.strptime(validated_data['sleepStart'], '%Y-%m-%dT%H:%M')
        sleepEnd = datetime.strptime(validated_data['sleepEnd'], '%Y-%m-%dT%H:%M')
        duration = sleepEnd - sleepStart
        serializer.save(sleepStart=sleepStart, sleepEnd=sleepEnd, duration=duration)


class logoutUser(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        # deleting the auth token to avoid it's reuse after logging out
        user.auth_token.delete()
        return Response({'msg': 'Logged out successfully!'})


def calculate(request, ss, se):
    sleepStart = datetime.strptime(ss, '%Y-%m-%dT%H:%M')
    sleepEnd = datetime.strptime(se, '%Y-%m-%dT%H:%M')
    duration = sleepEnd - sleepStart
    print(duration)
    return JsonResponse({"duration": str(duration)})


# ****** API Format ******
# {
#     "sleep" : {
#         "date" : "Date",
#         'hrs' : 25,
#         'mins' : 20,
#         'sec' : 50
#     }, "wake" : {
#         "date" : "Date",
#         'hrs' : 25,
#         'mins' : 20,
#         'sec' : 50
#     }
# }
