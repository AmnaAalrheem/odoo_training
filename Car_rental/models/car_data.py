# -*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models,tools,_
from datetime import datetime 
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from odoo.exceptions import UserError , ValidationError

class CarData(models.Model):
    _name= "car.data"
    name_of_car= fields.Char(string="Name",required=True)
    car_id= fields.Char(string='Car ID',required=True)
    color= fields.Char(string='Color',required=True)
    price= fields.Float(string='Price',required=True)
    license_date=fields.Date(string='License Date',required=True)
    insurance_amount=fields.Float(string='Insurance Amount',required=True)


class CustomerData(models.Model):
    _name= "customer.data"
    _rec_name="name_of_customer"
    name_of_customer=fields.Char(string="Name",required=True)
    #customer_id= fields.Float(string="Customr ID",required=True)
    phone= fields.Char(string="Phone NO",required=True)
    Identification_Number= fields.Char(string="Identification NO",required=True)
    license_number=fields.Char(string="License  NO",required=True)
    contract_details= fields.One2many("tenancy.agreement","rent_contract_id",string="Contract Details",)
    reg_number=fields.Char('Sequence')
    state = fields.Selection([('new','New'),('create agreement','Create Agreement'),('done','Done')], default='new')



    def action_Create_Agreement(self):
        for rec in self:
            rec.write({'state':'create agreement'})
    @api.model
    def create(self, vals):
        
        vals['reg_number'] = self.env['ir.sequence'].next_by_code('Customer.customer') or _('New')
        result = super(CustomerData, self).create(vals)
        return result


class TenancyAgreement(models.Model):
    _name= "tenancy.agreement"
    rent_contract_id= fields.Many2one("customer.data",string="Rent Contract ID")
    rent_contract_date= fields.Date(string="Rent Contract Date",required=True)
    from_date= fields.Date(string="From Date",required=True)
    to_date= fields.Date(string="To Date",required=True)
   # customer_id=fields.Many2one("customer.data",string="Customr ID")
    number_of_days= fields.Integer(string="Number Of Days",compute="calc_days")
    
    @api.depends('to_date','from_date')
    def calc_days(self):
        for rec in self:
            if rec.from_date != False and rec.to_date != False : 
                date_start = rec.from_date
                date_end = rec.to_date
                #date_start_d = datetime.strptime(date_start,DATE_FORMAT)
               # date_end_d = datetime.strptime(date_end,DATE_FORMAT)
                rec.number_of_days = ((date_end - date_start).days +1)
            else :
                rec.number_of_days = 0

       
       
   
    rent_per_day= fields.Float(string="Rent Per Day",required=True)
    @api.constrains('rent_per_day')
    def check_rent_per_day(self):
        if self.rent_per_day<=0:
            raise ValidationError(_('Error! you cannot continue.'))

    Total= fields.Float(string="Total",compute="Multi")
    @api.depends('rent_per_day','number_of_days')
    def Multi (self):
        for num in self:
            days = num.number_of_days
            rent = num.rent_per_day
            num.Total=(rent * days)
   
   
            
       
            

    