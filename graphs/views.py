from django.views.generic import TemplateView
from obspy import read

# class for echart.html
class DataChartViewEChart(TemplateView):

    template_name = 'graphs/echart.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        st = read('/home/rifqi/Downloads/stream.msd')

        def arrayFunc(stream, idx, nPoints):

            mainArray = []
            for i in range(nPoints):
                xyArray = []
                xyArray.append(stream[idx].times('timestamp')[i])
                xyArray.append(stream[idx].data[i])
                mainArray.append(xyArray)
            return(mainArray)

        endpoint = 250

        tr1 = arrayFunc(st, 0, endpoint)
        tr2 = arrayFunc(st, 1, endpoint)
        tr3 = arrayFunc(st, 2, endpoint)
        tr4 = arrayFunc(st, 3, endpoint)
        tr5 = arrayFunc(st, 4, endpoint)

        context['tr1'] = tr1
        context['tr2'] = tr2
        context['tr3'] = tr3
        context['tr4'] = tr4
        context['tr5'] = tr5

        return context