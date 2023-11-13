from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,Http404
from django.views.generic import FormView,ListView

from ShowGraph.forms import FormUploadFile
from ShowGraph.models import Files,Product

from plotly.offline import plot
from plotly.graph_objs import Scatter

class UploadFile(FormView):
    template_name = 'load_file.html'
    form_class = FormUploadFile
    success_url = 'showgraph:load'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('account:login'))

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if id := form.load(self.request.user):
            return HttpResponseRedirect(reverse('showgraph:plot',args=[id]))
        return HttpResponseRedirect(reverse(self.get_success_url() ))

class HistoryList(ListView):
    template_name = 'history.html'
    model = Files
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('account:login'))

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
            queryset = super().get_queryset()
            queryset = queryset.filter(user=self.request.user)
            return queryset
        
def index(request,files_id):
    
    if(request.user.is_anonymous):
        return HttpResponseRedirect(reverse('account:login'))
    
    file = Files.objects.all().filter(user=request.user,pk=files_id)
    data = Product.objects.filter(files_id=file[0].pk)
    
    client = []
    tps = []
    latency = []
    stddev = []
    
    for el in data:
        client.append(el.client)
        tps.append(el.tps)
        latency.append(el.latency)
        stddev.append(el.stddev)
        
    plot_div = []
    plot_div.append(plot([Scatter(x=client, y=tps,
                        mode='lines', name='tps',
                        opacity=0.8, marker_color='green')],
            output_type='div'))
    plot_div.append(plot([Scatter(x=client, y=latency,
                        mode='lines', name='latency',
                        opacity=0.8, marker_color='green')],
            output_type='div'))
    plot_div.append(plot([Scatter(x=client, y=stddev,
                        mode='lines', name='stddev',
                        opacity=0.8, marker_color='green')],
            output_type='div'))
    return render(request, "view.html", context={'plots_div': plot_div})
