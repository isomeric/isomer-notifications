#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Isomer - The distributed application framework
# ==============================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

"""

Schema: Notification
====================

Contains
--------

Notification: A configurable notification

"""

from isomer.schemata.defaultform import editbuttons
from isomer.schemata.base import base_object
from isomer.misc import i18n as _

NotificationSchema = base_object('notification',
                                 roles_read=['admin'],
                                 roles_write=['admin'],
                                 roles_create=['admin'],
                                 roles_list=['admin']
                                 )

NotificationSchema['properties'].update({
    'text': {
        'type': 'string', 'format': 'html', 'title': _('Text'),
        'description': _('Notification text')
    },
    'time': {
        'type': 'string',
        'format': 'datetimepicker',
        'title': _('Time'),
        'description': _('When this notification was issued')
    },
    'priority': {
        'type': 'integer',
        'default': 5,
        'title': _('Priority')
    },
    'acknowledged': {
        'type': 'boolean', 'title': _('Acknowledged'),
    },
    'acknowledged_time': {
        'type': 'string',
        'format': 'datetimepicker',
        'title': _('Acknowledged when'),
        'description': _('When this notification was acknowledged')
    },
    'acknowledgement': {
        'type': 'object',
        'properties': {
            'required': {
                'type': 'boolean', 'title': _('Acknowledgement required'),
                'default': False
            },
            'by': {
                'type': 'string',
                'format': 'datetimepicker',
                'title': _('Acknowledgment due by'),
                'description': _('Latest time, this notification has to be acknowledged')
            },
            'failover': {
                'type': 'string',
                'enum': ['ignore', 'repeat', 'emit', 'escalate']
            },
            'escalations': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'method': {
                            'type': 'string'
                        },
                        'text': {
                            'type': 'string', 'title': _('New text')
                        },
                        'next_failover': {
                            'type': 'string',
                            'enum': ['ignore', 'repeat', 'emit', 'escalate']
                        },
                        'timespan': {
                            'type': 'integer', 'title': _('Timespan for repeated escalation')
                        }
                    }
                }
            }
        }
    }
})

NotificationForm = [
    '*',
    editbuttons
]

Notification = {'schema': NotificationSchema, 'form': NotificationForm}
