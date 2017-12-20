# -*- coding: utf-8 -*-

from odoo import api, models, fields

class StockQuantPackage(models.Model):
    _inherit = "stock.quant.package"


    @api.multi
    def _prepare_info(self, extended=False):
        """ TODO: add docstring

            id  int     
            name    string  

            When extended is True also return:

            quant_ids   [{stock.quants]}    A list of all the quants of the given package.
        """
        self.ensure_one()

        info = {"id": self.id,
                "name": self.name,
               }
        
        if extended:
            info['quants'] = self.quant_ids.get_info()

        return info

    @api.multi
    def get_info(self, extended=False):
        """ TODO: add docstring
        """
        res = []
        for pack in self:
            res.append(pack._prepare_info(extended=extended))

        return res