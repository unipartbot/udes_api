# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request

from .main import UdesApi


class PickingPriorities(UdesApi):

    @http.route('/api/stock-picking-priorities/',
                type='json', methods=['GET'], auth='user')
    def get_priority_groups(self):
        """
        Return a JSON list with a single object, containing the
        priorities of the 'Picking' priority group, by following
        the format of this example:

            [
                {
                    'name': 'Picking',
                    'priorities': [
                        {'id': '2', 'name': 'Urgent'},
                        {'id': '1', 'name': 'Normal'}
                    ]
                },
                {
                    ...
                },
                ...
            ]
        """
        Picking = request.env['stock.picking']
        return Picking.get_priorities()
