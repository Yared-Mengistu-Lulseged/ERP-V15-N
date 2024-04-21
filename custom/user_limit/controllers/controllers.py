# -*- coding: utf-8 -*-
# from odoo import http


# class UserLimit(http.Controller):
#     @http.route('/user_limit/user_limit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/user_limit/user_limit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('user_limit.listing', {
#             'root': '/user_limit/user_limit',
#             'objects': http.request.env['user_limit.user_limit'].search([]),
#         })

#     @http.route('/user_limit/user_limit/objects/<model("user_limit.user_limit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('user_limit.object', {
#             'object': obj
#         })
