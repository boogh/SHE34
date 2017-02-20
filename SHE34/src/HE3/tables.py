import django_tables2 as tables
from django_tables2.utils import A
from .models import Evaluation

class EvaluationsTables(tables.Table):

    title = tables.Column()
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
        exclude=('id', 'evaluator' , 'ofProject')
        sequence=('title','heurPrincip','place','description' ,'recommendation','positivity','severity','frequency','tags')
