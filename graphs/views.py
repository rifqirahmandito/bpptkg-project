from django.views.generic import TemplateView
from obspy import read

# class for echart.html
class DataChartViewEChart(TemplateView):

    template_name = 'graphs/echart.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        st = read('/home/rifqi/Downloads/stream.msd')

        def arrayFunc(stream, idx):

            mainArray = []
            for i in range(len(stream[idx])):
                xyArray = []
                xyArray.append(stream[idx].times('timestamp')[i])
                xyArray.append(stream[idx].data[i])
                mainArray.append(xyArray)
            return(mainArray)

        tr2 = arrayFunc(st, 1)

        context['tr2'] = tr2

        return context