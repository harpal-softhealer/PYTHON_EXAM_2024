# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.addons.web.controllers.home import Home as WebHome
from odoo.http import request


class sh_backmate_theme_mobile_Home(WebHome):

    @http.route()
    def web_client(self, s_action=None, **kw):
        if kw.get('sh_backmate_theme_mobile_login', False) and kw.get('db', False) and kw.get('login', False) and kw.get('password', False):
            try:
                uid = request.session.authenticate(
                    kw.get('db'), kw.get('login'), kw.get('password'))
                response = request.redirect(
                    self._login_redirect(uid, redirect=None))
                response.set_cookie(
                    key='sh_backmate_theme_mobile_login_web_view',
                    value='true',
                )
                return response
            except Exception:
                pass

        return super().web_client(s_action, **kw)
