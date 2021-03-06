# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Industrial Dual Analog In Bricklet communication config

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 249,
    'name': ('IndustrialDualAnalogIn', 'industrial_dual_analog_in', 'Industrial Dual Analog In', 'Industrial Dual Analog In Bricklet'),
    'manufacturer': 'Tinkerforge',
    'description': 'TODO',
    'released': False,
    'packets': []
}

com['api'] = {
'en':
"""
TODO

Two channels can be connected to the Bricklet. Functions that are related
directly to a channel have a ``channel`` parameter to specify one of the two
channels. Valid values for the ``channel`` parameter are 0 and 1.
""",
'de':
"""
TODO

Es können zwei Sensoren an das Bricklet angeschlossen werden. Funktionen die
sich direkt auf einen der Sensoren beziehen haben einen ``channel`` Parameter,
um den Sensor anzugeben. Gültige Werte für den ``channel`` Parameter sind 0
und 1.
"""
}

com['packets'].append({
'type': 'function',
'name': ('GetVoltage', 'get_voltage'), 
'elements': [('channel', 'uint8', 1, 'in'),
             ('voltage', 'int32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO

If you want to get the voltage periodically, it is recommended to use the
callback :func:`Voltage` and set the period with 
:func:`SetVoltageCallbackPeriod`.
""",
'de':
"""
TODO

Wenn die Stromstärke periodisch abgefragt werden soll, wird empfohlen
den Callback :func:`Voltage` zu nutzen und die Periode mit 
:func:`SetVoltageCallbackPeriod` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('SetVoltageCallbackPeriod', 'set_voltage_callback_period'), 
'elements': [('channel', 'uint8', 1, 'in'),
             ('period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :func:`Voltage` callback is triggered
periodically for the given channel. A value of 0 turns the callback off.

:func:`Voltage` is only triggered if the voltage has changed since the
last triggering.

The default value is 0.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :func:`Voltage` Callback für den
übergebenen Sensor ausgelöst wird.
Ein Wert von 0 deaktiviert den Callback.

:func:`Voltage` wird nur ausgelöst wenn sich die Stromstärke seit der
letzten Auslösung geändert hat.

Der Standardwert ist 0. 
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('GetVoltageCallbackPeriod', 'get_voltage_callback_period'), 
'elements': [('channel', 'uint8', 1, 'in'),
             ('period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`SetVoltageCallbackPeriod`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`SetVoltageCallbackPeriod`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('SetVoltageCallbackThreshold', 'set_voltage_callback_threshold'), 
'elements': [('channel', 'uint8', 1, 'in'),
             ('option', 'char', 1, 'in', ('ThresholdOption', 'threshold_option', [('Off', 'off', 'x'),
                                                                                  ('Outside', 'outside', 'o'),
                                                                                  ('Inside', 'inside', 'i'),
                                                                                  ('Smaller', 'smaller', '<'),
                                                                                  ('Greater', 'greater', '>')])), 
             ('min', 'int32', 1, 'in'),
             ('max', 'int32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the thresholds for the :func:`VoltageReached` callback for the given
channel.

The following options are possible:

.. csv-table::
 :header: "Option", "Description"
 :widths: 10, 100

 "'x'",    "Callback is turned off"
 "'o'",    "Callback is triggered when the voltage is *outside* the min and max values"
 "'i'",    "Callback is triggered when the voltage is *inside* the min and max values"
 "'<'",    "Callback is triggered when the voltage is smaller than the min value (max is ignored)"
 "'>'",    "Callback is triggered when the voltage is greater than the min value (max is ignored)"

The default value is ('x', 0, 0).
""",
'de':
"""
Setzt den Schwellwert des :func:`VoltageReached` Callbacks für den übergebenen
Sensor.

Die folgenden Optionen sind möglich:

.. csv-table::
 :header: "Option", "Beschreibung"
 :widths: 10, 100
 
 "'x'",    "Callback ist inaktiv"
 "'o'",    "Callback wird ausgelöst wenn die Stromstärke *außerhalb* des min und max Wertes ist"
 "'i'",    "Callback wird ausgelöst wenn die Stromstärke *innerhalb* des min und max Wertes ist"
 "'<'",    "Callback wird ausgelöst wenn die Stromstärke kleiner als der min Wert ist (max wird ignoriert)"
 "'>'",    "Callback wird ausgelöst wenn die Stromstärke größer als der min Wert ist (max wird ignoriert)"
 
Der Standardwert ist ('x', 0, 0).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('GetVoltageCallbackThreshold', 'get_voltage_callback_threshold'), 
'elements': [('channel', 'uint8', 1, 'in'),
             ('option', 'char', 1, 'out', ('ThresholdOption', 'threshold_option', [('Off', 'off', 'x'),
                                                                                   ('Outside', 'outside', 'o'),
                                                                                   ('Inside', 'inside', 'i'),
                                                                                   ('Smaller', 'smaller', '<'),
                                                                                   ('Greater', 'greater', '>')])), 
             ('min', 'int32', 1, 'out'),
             ('max', 'int32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the threshold as set by :func:`SetVoltageCallbackThreshold`.
""",
'de':
"""
Gibt den Schwellwert zurück, wie von :func:`SetVoltageCallbackThreshold`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('SetDebouncePeriod', 'set_debounce_period'), 
'elements': [('debounce', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the threshold callback

* :func:`VoltageReached`

is triggered, if the threshold

* :func:`SetVoltageCallbackThreshold`

keeps being reached.

The default value is 100.
""",
'de':
"""
Setzt die Periode in ms mit welcher der Schwellwert Callback

* :func:`VoltageReached`
 
ausgelöst werden, wenn der Schwellwert

* :func:`SetVoltageCallbackThreshold`
 
weiterhin erreicht bleibt.

Der Standardwert ist 100.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('GetDebouncePeriod', 'get_debounce_period'), 
'elements': [('debounce', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the debounce period as set by :func:`SetDebouncePeriod`.
""",
'de':
"""
Gibt die Entprellperiode zurück, wie von :func:`SetDebouncePeriod`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('SetSampleRate', 'set_sample_rate'), 
'elements': [('rate', 'uint8', 1, 'in', ('SampleRate', 'sample_rate', [('976SPS', '976_sps', 0),
                                                                       ('488SPS', '488_sps', 1),
                                                                       ('244SPS', '244_sps', 2),
                                                                       ('122SPS', '122_sps', 3),
                                                                       ('61SPS', '61_sps', 4),
                                                                       ('4SPS', '4_sps', 5),
                                                                       ('2SPS', '2_sps', 6),
                                                                       ('1SPS', '1_sps', 7)]))],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('GetSampleRate', 'get_sample_rate'), 
'elements': [('rate', 'uint8', 1, 'out', ('SampleRate', 'sample_rate', [('976SPS', '976_sps', 0),
                                                                        ('488SPS', '488_sps', 1),
                                                                        ('244SPS', '244_sps', 2),
                                                                        ('122SPS', '122_sps', 3),
                                                                        ('61SPS', '61_sps', 4),
                                                                        ('4SPS', '4_sps', 5),
                                                                        ('2SPS', '2_sps', 6),
                                                                        ('1SPS', '1_sps', 7)]))],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the sample rate as set by :func:`SetSampleRate`.
""",
'de':
"""
Gibt die Abtastrate zurück, wie von :func:`SetSampleRate`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('SetCalibration', 'set_calibration'), 
'elements': [('offset', 'int32', 2, 'in'),
             ('gain', 'int32', 2, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('GetCalibration', 'get_calibration'), 
'elements': [('offset', 'int32', 2, 'out'),
             ('gain', 'int32', 2, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': ('GetADCValues', 'get_adc_values'), 
'elements': [('value', 'int32', 2, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': ('Voltage', 'voltage'), 
'elements': [('channel', 'uint8', 1, 'out'),
             ('voltage', 'int32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`SetVoltageCallbackPeriod`. The :word:`parameter` is the voltage of the
channel.

:func:`Voltage` is only triggered if the voltage has changed since the
last triggering.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit :func:`SetVoltageCallbackPeriod`,
ausgelöst. Der :word:`parameter` ist die Stromstärke des Sensors.

:func:`Voltage` wird nur ausgelöst wenn sich die Stromstärke seit der
letzten Auslösung geändert hat.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': ('VoltageReached', 'voltage_reached'), 
'elements': [('channel', 'uint8', 1, 'out'),
             ('voltage', 'int32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered when the threshold as set by
:func:`SetVoltageCallbackThreshold` is reached.
The :word:`parameter` is the voltage of the channel.

If the threshold keeps being reached, the callback is triggered periodically
with the period as set by :func:`SetDebouncePeriod`.
""",
'de':
"""
Dieser Callback wird ausgelöst wenn der Schwellwert, wie von 
:func:`SetVoltageCallbackThreshold` gesetzt, erreicht wird.
Der :word:`parameter` ist die Stromstärke des Sensors.

Wenn der Schwellwert erreicht bleibt, wird der Callback mit der Periode, wie
mit :func:`SetDebouncePeriod` gesetzt, ausgelöst.
"""
}]
})
