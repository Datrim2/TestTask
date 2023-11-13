from django import forms
from ShowGraph.models import Files,Product

import csv
import codecs
from decimal import Decimal
import functools

class FormUploadFile(forms.Form):
    
    file = forms.FileField(label='Файл:')
    
    def load(self,user):
        file = csv.reader(codecs.iterdecode(self.cleaned_data.get('file').open(), 'utf-8-sig'),delimiter=';')
        header = next(file)
        
        if header==['client', 'tps', 'latency', 'stddev']:
            files = Files.objects.create(user=user,doc_name=self.cleaned_data.get('file').name,
                                        status=0)
            
            bulk_list = []
            
            for el in file:
                bulk_list.append(Product(files=files,
                                        client=Decimal(el[0].replace(",",".")),
                                        tps=Decimal(el[1].replace(",",".")),
                                        latency=Decimal(el[2].replace(",",".")),
                                        stddev=Decimal(el[3].replace(",",".")),))
            
            files.save()
            
            Product.objects.bulk_create(bulk_list)
            return files.id
        else:
            return False