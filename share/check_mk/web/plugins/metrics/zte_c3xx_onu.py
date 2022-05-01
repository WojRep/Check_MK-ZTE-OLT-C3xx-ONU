#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-



metric_info['zte_c3xx_onu_onurx'] = {
    'title': _('ONU Rx'),
    'help': _('ONU Rx signal from OLT'),
    'unit': 'dbm',
    'color': '16/a',
}

metric_info['zte_c3xx_onu_oltrx'] = {
    'title': _('OLT Rx'),
    'help': _('OLT Rx signal from ONU'),
    'unit': 'dbm',
    'color': '33/a',
}

metric_info['zte_c3xx_onu_onutx'] = {
    'title': _('ONU Tx'),
    'help': _('ONU Tx signal to OLT'),
    'unit': 'dbm',
    'color': '#fff3e9',
}

metric_info['zte_c3xx_onu_onuphasestatus'] = {
    'title': _('ONU Phase Status'),
    'help': _('ONU Phase Status'),
    'unit': '',
    'color': '#fff3e9',
}



check_metrics['check_mk-zte_c3xx_onu'] = {
    'onurx': {'name': 'zte_c3xx_onu_onurx', },
    'oltrx': {'name': 'zte_c3xx_onu_oltrx', },
    'onutx': {'name': 'zte_c3xx_onu_onutx', },
    'onuphasestatus': {'name': 'zte_c3xx_onu_onuphasestatus', },
}


perfometer_info.append({
    'type': 'dual',
    'perfometers': [
    {
        'type': 'logarithmic',
        'metric': 'zte_c3xx_onu_onurx',
        'half_value': 4,
        'exponent': 2,
        'color': '#c7ecff',
        },
    {
        'type': 'logarithmic',
        'metric': 'zte_c3xx_onu_oltrx',
        'half_value': 4,
        'exponent': 2,
        'color': '#d8d7ff',
        },
    ],
})

graph_info.append({
    'title': _('Rx Optical Signal'),
    'metrics': [
        ('zte_c3xx_onu_onurx', 'area'),
        ('zte_c3xx_onu_oltrx', '-area'),
    ],
    'range': (-40,40),
})

#graph_info['zte_c3xx_onu'] = {
#    'title': _('Rx Optical Signal'),
#    'metrics': [
#       ('zte_c3xx_onu_onurx', 'line'),
#       ('zte_c3xx_onu_oltrx', 'line'),
#    ],
#    'range': (-40,5),
#}