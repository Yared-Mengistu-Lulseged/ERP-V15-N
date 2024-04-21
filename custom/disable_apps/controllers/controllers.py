# -*- coding: utf-8 -*-
# from odoo import http


# class DisableApps(http.Controller):
#     @http.route('/disable_apps/disable_apps', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/disable_apps/disable_apps/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('disable_apps.listing', {
#             'root': '/disable_apps/disable_apps',
#             'objects': http.request.env['disable_apps.disable_apps'].search([]),
#         })

#     @http.route('/disable_apps/disable_apps/objects/<model("disable_apps.disable_apps"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('disable_apps.object', {
#             'object': obj
#         })
