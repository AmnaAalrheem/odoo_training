# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools,_
from datetime import date,datetime
import calendar
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

class StudentProfile(models.Model):
    _name= "student.profile"


    name= fields.Char( string='Name',required=True)
    city_id= fields.Many2one('res.country.state',required=True)
    degree= fields.Float( string='Degree',required=True)
    date_of_birth= fields.Date(string='Date of birth')
    age= fields.Float( string='Age',compute='calculate_age')
    reg_number = fields.Char('Sequence')
    state = fields.Selection([('new','New'),('progress','progress'),('graduated','Graduated')], default='new')



    def action_progress(self):
        for rec in self:
            rec.write({'state':'progress'})
    @api.model
    def create(self, vals):
        
        vals['reg_number'] = self.env['ir.sequence'].next_by_code('Student.student') or _('New')
        result = super(StudentProfile, self).create(vals)
        return result

    def calculate_age(self):
        for rec in self:
            if rec.date_of_birth:
                #date_from = datetime.strptime(date_from, "%Y-%m-%d").date()
                #d1 = int(rec.date_of_birth
                #d2 = datetime.today().year
                rd = relativedelta(datetime.today(),rec.date_of_birth )
                rec.age= rd.years+((rd.months*30+rd.days)/365.25)
            else:
                rec.age=0


    @api.constrains('degree')
    def check_degree(self):
        if self.degree<60:
            raise ValidationError(_('Error ! You cannot register student if his degree less than 60%.')) 



class Subject(models.Model):
    _name= "subject.subject"


    name= fields.Char( string='Name',required=True)
    is_optional = fields.Boolean(string= 'Optional')
    semester_id = fields.Many2one('student.semster',string= 'Semster')


class Subject(models.Model):
    _name= "student.semster"


    name= fields.Char( string='Name',required=True)
    
    subject_ids = fields.One2many('subject.subject','semester_id',string= 'Semster')



    


