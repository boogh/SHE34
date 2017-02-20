import django_tables2 as tables
from django_tables2.utils import A
from .models import Evaluation
from django.utils.html import format_html
import itertools

class EvaluationsTablesForEvaluator(tables.Table):

    # evaluator =tables.Column()
    row_number = tables.Column(empty_values=() , verbose_name= '#')
    title = tables.LinkColumn('profiles:dashboard:evaluation-update', args=[A('pk')])
    heurPrincip = tables.Column()
    place = tables.Column()
    tags = tables.Column()
    description = tables.Column()
    recommendation = tables.Column()
    positivity = tables.Column()
    severity = tables.Column()
    frequency = tables.Column()
    # checkbox = tables.CheckBoxColumn(args='pk' )


    class Meta:
        template ='django_tables2/bootstrap.html'
        model = Evaluation
        # attrs = {'class':  'paleblue'}
        attrs ={'class' : 'table table-responsive', "width":"100%"}
        exclude=('id' ,'evaluator', 'ofProject')
        sequence=('row_number','title','heurPrincip','place','description' ,'recommendation','positivity','severity','frequency','tags')

    def __init__(self, *args, **kwargs):
        super(EvaluationsTablesForEvaluator, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return next(self.counter)

class EvaluationsTablesForManager(tables.Table):



    # evaluator = UserCol()
    ...
    row_number = tables.Column(empty_values=() , verbose_name= '#')
    evaluator = tables.Column()
    title = tables.LinkColumn('profiles:dashboard:evaluation-update', args=[A('pk')])
    heurPrincip = tables.Column()
    place = tables.Column()
    tags = tables.Column()
    description = tables.Column()
    recommendation = tables.Column()
    positivity = tables.Column()
    severity = tables.Column()
    frequency = tables.Column()
    # checkbox = tables.CheckBoxColumn(args='pk' )


    class Meta:
        template ='django_tables2/bootstrap.html'
        model = Evaluation
        # attrs = {'class':  'paleblue'}
        attrs ={'class' : 'table table-responsive', "width":"100%"}
        exclude=('id' , 'ofProject')
        sequence=('row_number','evaluator','title','heurPrincip','place','description' ,'recommendation','positivity','severity','frequency','tags')

    def __init__(self, *args, **kwargs):
        super(EvaluationsTablesForManager, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return next(self.counter)

    def render_evaluator(self , value):
        return  value.name


