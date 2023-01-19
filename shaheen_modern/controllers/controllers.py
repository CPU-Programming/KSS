# -*- coding: utf-8 -*-
# from odoo import http


# class Kss(http.Controller):
#     @http.route('/kss/kss/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kss/kss/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kss.listing', {
#             'root': '/kss/kss',
#             'objects': http.request.env['kss.kss'].search([]),
#         })

#     @http.route('/kss/kss/objects/<model("kss.kss"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kss.object', {
#             'object': obj
#         })
