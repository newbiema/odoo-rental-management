from odoo import models, fields


class RentalOrder(models.Model):
    _name = 'rental.order'
    _description = 'Rental Order'

    name = fields.Char(string='Rental Name', required=True)
    partner_id = fields.Many2one( 'res.partner', string='Customer')
    rental_date = fields.Date(string='Rental Date')
    duration = fields.Integer(string='Duration')
    price = fields.Float(string='Price')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
    ], string='Status', default='draft')