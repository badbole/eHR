# -*- coding: utf-8 -*-
from odoo import http

# class Scaff(http.Controller):
#     @http.route('/scaff/scaff/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scaff/scaff/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scaff.listing', {
#             'root': '/scaff/scaff',
#             'objects': http.request.env['scaff.scaff'].search([]),
#         })

#     @http.route('/scaff/scaff/objects/<model("scaff.scaff"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scaff.object', {
#             'object': obj
#         })