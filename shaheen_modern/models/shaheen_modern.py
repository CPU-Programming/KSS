from odoo import models, fields, api,_

class ShaheenModern(models.Model):
    _name = 'shaheen.modern'
    _description = 'shaheen.modern'

class ResPartner(models.Model):
    _inherit='res.partner'

class ManuFac(models.Model):
    _inherit='mrp.production'

class purchaseOdre(models.Model):
    _inherit='purchase.order'

class invoice(models.Model):
    _inherit='account.move'

class maintenan(models.Model):
    _inherit='maintenance.request'

    seq_id     =fields.Char(string='Order Referneces',required=True)

class Receipt(models.Model):
    _name='receipt.account'
    _rec_name='sequencess'


    sequencess            =fields.Char('Sequence' , readonly=True)
    date                  =fields.Date('Date', default=fields.Date.today())
    recived_id            =fields.Char('I received from master')
    amount                =fields.Float('Amount')
    amount_id             =fields.Char('المبلغ كتابه')
    cash                  =fields.Char('cash')
    bank                  =fields.Char('Check')
    number_bank           =fields.Integer('Check Number')
    on_bank               =fields.Char('On Bank')
    about_iss             =fields.Text('Is About')
    sing_of_ac            =fields.Char('accountant signature')
    rec_id                =fields.Char('Received By')

    @api.model
    def create(self, vals):
        vals['sequencess'] = self.env['ir.sequence'].next_by_code('receipt.account.sequence')
        return super(Receipt, self).create(vals)

class CashReeipt(models.Model):
    _name='cash.receipt'
    _rec_name='sequences'

    sequences             =fields.Char('Sequence', copy=False, readonly=True)
    date_t                =fields.Date('Date', default=fields.Date.today())
    recived_ids           =fields.Char('I received from master')
    amount_s              =fields.Integer('Amount')
    amount_ids            =fields.Char('المبلغ كتابه')
    cash_sd               =fields.Char('cash')
    bank_sd               =fields.Char('Check')
    numbers_bank          =fields.Integer('Check Number')
    on_banks              =fields.Char('On Bank')
    about_is              =fields.Text('Is About')
    sing_of_cc            =fields.Char('accountant signature')
    rec_ids               =fields.Char('Received By')

    @api.model
    def create(self, vals):
        vals['sequences'] = self.env['ir.sequence'].next_by_code('cash.receipt.seq')
        return super(CashReeipt, self).create(vals)

class TableFollowup(models.Model):
    _name='table.followup'
    _description = 'table.followup'


    date            = fields.Date('Date',  default=fields.Date.today())
    user_id         = fields.Many2one('res.users', string='Ticket Owner')
    table_id        = fields.One2many('table.daily','table_dail',string='Table Daily')



class TableDaily(models.Model):
    _name='table.daily'

    name                  = fields.Char('Name Of The Exporter')
    city                  = fields.Char('Imported State')
    shipping_time         = fields.Integer('Shipping Time')
    sheep_id              = fields.Integer('Sheep')
    goats_id              = fields.Integer('Goat')
    cows_id               = fields.Integer('Cow')
    camel_id              = fields.Integer('Camel')
    method_py             = fields.Selection([('bank','Bank'),('cash','Cash')],'Pay Method')
    payment_date          = fields.Date('Payment Date')
    agent_id              = fields.Char('Agent&Num')
    # agent_num             =fields.Char('agent Num')
    comments              =fields.Text('Comments')
    table_dail            = fields.Many2one('table.followup', string='Table Id')


class MaintenanceOrder(models.Model):
    _name='maintenance.order'

    # state            = fields.Selection([
    #     ('draft','Draft'),
    #     ('done','done'),
    #     ('confirm', 'Confirm')],
    #     string='State', copy=False, default='draft',track_visibity='onchange')


    # # @api.model
    # def action_confirm(self):
    #     print("hello")
    #     # self.write({'state':'posted'})

    # @api.model
    # def cancel_re(self):
    #     self.write({'state':'done'})




    job_num                  =fields.Char('Job NO',required=True)
    responsible_name         =fields.Many2one('res.users',string='responsilbe',required=True,change_default=True)
    date_main                =fields.Date('Date')
    # reference                =fields.Char('Sequence', readonly=True, select=True, copy=False, default='New')
    application_no           = fields.Char('Application No.', default='/')
    mission_id               =fields.Text('Missuon',required=True)
    start_time               =fields.Float('Start Time')
    end_time                 =fields.Float('End Time')
    Final_report             =fields.Text('Final Reports')
    spare_id                 =fields.One2many('spare.part','main_spare',string='Spare')


    @api.model
    def create(self, vals):
        if vals.get('application_no','New') == 'New':
            vals['application_no'] = self.env['ir.sequence'].next_by_code('your.sequence.code') or 'New'
            result = super(MaintenanceOrder, self).create(vals)
            return result


    # on create method
    # @api.model
    # def create(self, vals):
    #     obj = super(MaintenanceOrder, self).create(vals)
    #     if obj.application_no == 'New':
    #         number = self.env['ir.sequence'].get('your.sequence.code') or '/'
    #         obj.write({'application_no': number})
    #         return obj


    # on button click event
    @api.model
    def submit_application(self):
        if self.application_no == '/':
            sequence_id = self.env['ir.sequence'].search([('code', '=', 'your.sequence.code')])
            sequence_pool = self.env['ir.sequence']
            application_no = sequence_pool.sudo().get_id(sequence_id.id)
            self.write({'application_no': application_no})




class sparepart(models.Model):
    _name='spare.part'

    spare_id           =fields.Many2one('maintenance.equipment',string='Spareparts')
    count_id           =fields.Integer('Count')
    comments_sp        =fields.Text('Comments')
    main_spare         =fields.Many2one('maintenance.order',string='Maintenance Parts')



# class PeridoicReports(models.Model):
#     _name='periodic.report'






    # @api.model
    # def create(self, vals):
    #     if vals.get('reference','New') == 'New':
    #         vals['reference'] = self.env['ir.sequence'].next_by_code('sequence.maintenance') or 'New'
    #         result = super(MaintenanceRequest, self).create(vals)
    #         return result


    # @api.model
    # def create(self, vals):
    #     if vals.get('name', 'New') == 'New':
    #         vals['name'] = self.env['ir.sequence'].next_by_code('model.name') or 'New'
    #         result = super(MaintenanceOrder, self).create(vals)
    #         return result








    # @api.model

    # def create(self, vals):
    #     if vals.get('reference' ,'New') =='New':
    #         vals['reference'] = self.env['ir.sequence'].next_by_code('maintenance.order.sequence') or 'New'
    #         res = super(MaintenanceOrder, self).create(vals)
    #         return res
    # # @api.model
    # def create(self, vals):
    #     vals['sequencess'] = self.env['ir.sequence'].next_by_code('receipt.account')
    #     return super(SequenceOrder, self).create(vals)

    # @api.model
    # def create(self, vals):
    #     if vals.get('sequencess' , ('New')) ==('New') :
    #         vals ['sequencess']= self.env['ir.sequence'].next_by_code('receipt.account') or ('New')

    #         result=super(ReceiptAccount, self).create(vals)
    #         return result


    # @api.model
    # def create(self, vals):
    #     if vals.get('sequence_name', _('New')) == _('New'):
    #         vals['sequence_name'] = self.env['ir.sequence'].next_by_code('sequence.maintenance') or _('New')

    #     result = super(MaintenanceRequest, self).create(vals)
    #     return result







# class ProPay(models.Model):
#     _name='pro.pay'

#     method_type =fields.Char('Payment Method')
#     name=fields.Integer('Name')








#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
