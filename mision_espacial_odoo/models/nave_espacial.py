# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class nave_espacial(models.Model):
    
    _name = 'mision.nave_espacial'
    _description = 'nave_espacial info'
    
    name = fields.Char(string ='Titulo', required = True)
    descripcion = fields.Text(string = 'Descripcion')
    
    level = fields.Text(string = 'Tipo')
    
    ancho = fields.Float(string='Ancho', default=0.00)
    
    #Largo por defecto = 0
    largo = fields.Float(string='Largo', default =0.00)
    
    
    
    @api.constrains('ancho','largo')
    def _check_validation_(self):
        for record in self:
            if self.ancho > self.largo:
                raise UserError('Ancho no puede ser mayor a largo en una Nave')
    