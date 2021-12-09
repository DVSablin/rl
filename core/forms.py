from crispy_forms.bootstrap import FormActions
from django.forms import Form, ModelForm, DateInput
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML, Div


class DateInput(DateInput):
    input_type = 'date'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        widgets = {'date': DateInput(), 'arrival_date': DateInput()}
        exclude = ['order_status', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "orderFormId"
        self.helper.form_action = 'test_url'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            HTML("<h6> Контактная информация </h6>"),
            Row(
                Column('name'),
                Column('phone'),
                Column('email'),
            ),
            HTML("<h6> Маршрут </h6>"),
            Row(
                Column('departure'),
                Column('arrival'),
            ),
            HTML("<h6> Габариты груза </h6>"),
            Row(
                Column('weight'),
                Column('height'),
                Column('length'),
                Column('capacity'),

            ),
            HTML("<h6>Предпочитаемые даты отправки и выгрузки</h6>"),
            Row(
                Column('date'),
                Column('arrival_date'),
            ),
            HTML("<h6>Дополнительная информация по заявке</h6>"),
            Row(
                Column('extra_info'),
            ),
            Div(css_class="form-group g-recaptcha", data_sitekey="6LfEgY0dAAAAAIigFIvG6bCo5tyvtHd1EsO-BMvB"
            ),
            FormActions(
                Submit('submit', 'Отправить заявку'),
            ),

        )