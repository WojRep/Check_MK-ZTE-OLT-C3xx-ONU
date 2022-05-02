#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_check_parameters(
    subgroup_networking,
    'zte_c3xx_onu',
    _('ZTE OLT C3xx - ONU params'),
    Transform(
        Dictionary(
            title=_('ZTE OLT C3xx - ONU params'),
            elements=[
                ('olt_rx', Tuple(
                    title=_('OLT Rx signal from ONU'),
                    elements=[
                        Float(title=_('Warning at'), unit='dBm',
                              default_value='-25.0', ),
                        Float(title=_('Critical at'), unit='dBm',
                              default_value='-27.0', ),
                    ])),
                ('onu_rx', Tuple(
                    title=_('ONU Rx signal from OLT'),
                    elements=[
                        Float(title=_('Warning at'), unit='dBm',
                              default_value='-25.0', ),
                        Float(title=_('Critical at'), unit='dBm',
                              default_value='-27.0', ),
                    ])),
                ('onu_tx', Tuple(
                    title=_('ONU Tx power to OLT'),
                    elements=[
                        Float(title=_('Warning at'), unit='dBm',
                              default_value='6.0', ),
                        Float(title=_('Critical at'), unit='dBm',
                              default_value='7.0', ),
                    ])),
            ],
        ),
    ),
    TextAscii(
        title=_("ZTE OLT C3xx - ONU params"),
    ),
    match_type='dict',
)