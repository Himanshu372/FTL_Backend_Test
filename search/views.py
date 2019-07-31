from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from search.models import corpusData
from search.serializers import corpusDataSerializer
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
import json



class corpusDataView(viewsets.ModelViewSet):
    queryset = corpusData.objects.all()
    serializer_class = corpusDataSerializer
    parser_classes = (FileUploadParser, )

    def list(self, request, *args, **kwargs):
        '''

        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        word = request.GET.get('word')
        filtered_queryset = self.queryset.filter(token__contains = word).values()
        for each in filtered_queryset:
            if each['token'] == word:
                each['primary_rank'] = 0
            elif each['token'].startswith(word):
                each['primary_rank'] = 1
            else:
                each['primary_rank'] = 2
        filtered_queryset = sorted(filtered_queryset, key = lambda x : (x['primary_rank'], len(x['token'])))
        serialized_data = corpusDataSerializer(filtered_queryset, many = True)
        print(serialized_data)
        return Response(serialized_data.data, status = 204)



    # def put(self, request, filename = 'word_search.tsv' , format = None):
    #     '''
    #
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     '''
    #     file_obj = request.data['file']
    #     for line in file_obj:
    #         token = line.decode('utf-8').split()[0]
    #         token_count = line.decode('utf-8').split()[1]
    #         if self.queryset.filter(token = token).exists():
    #             pass
    #         else:
    #             db_obj = corpusData(token = token, token_count = token_count)
    #             db_obj.save()
    #     return Response('File processed', status = 204)







