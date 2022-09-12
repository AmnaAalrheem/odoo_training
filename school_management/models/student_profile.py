# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools,_
    

class StudentProfile(models.Model):
    _name= "student.profile"


    name= fields.Char( string='Name',required=True)
    city_id= fields.Many2one('res.country.state',required=True)
    degree= fields.Float( string='Degree',required=True)
    date_of_birth= fields.Date(string='Date of birth')


