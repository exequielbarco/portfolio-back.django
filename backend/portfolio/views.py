# # from rest_framework.response import Response
# # from rest_framework.decorators import api_view
# from rest_framework import viewsets, permissions, generics
# from .models import AboutPage
# from .serializers import AboutPageSerializer

# from django.contrib.auth.models import User, Group
# from backend.portfolio.serializers import UserSerializer, GroupSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by("-date_joined")
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class AboutPageViewSet(viewsets.ModelViewSet):
#     queryset = AboutPage.objects.select_related("owner").all()
#     serializer_class = AboutPageSerializer
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         language = self.request.query_params.get("language")
        
#         valid_languages = dict(AboutPage.LANGUAGE_CHOICES).keys()

#         if language and language.lower() in valid_languages:
#             queryset = queryset.filter(language=language)
            
#         if not queryset.exists():
#             return AboutPage.objects.filter(id=1)
        
#         return queryset


# # @api_view(["GET"])
# # def get_aboutpage(request):
# #     aboutpage = AboutPage.objects.all()
# #     serializer = AboutPageSerializer(aboutpage, many=False)
# #     return Response(serializer.data)


# # @api_view("POST")
# # def create_aboutpage(request):
# #     serializer = AboutPage(data=request.data)
# #     if serializer.is_valid():
# #         serializer.save
# #         return Response(serializer.data, status=201)
# #     return Response(serializer.errors, status=400)
