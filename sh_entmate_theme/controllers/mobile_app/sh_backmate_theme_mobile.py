# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

import json
import logging
import requests

from odoo import http
from odoo.http import request, root

_logger = logging.getLogger(__name__)


class sh_backmate_theme_mobile(http.Controller):

    @http.route('/sh_backmate_theme_mobile/session/logout', type='http', auth="none")
    def sh_backmate_theme_mobile_session_logout(self, redirect='/web'):
        module_name = 'sh_backmate_theme'
        theme = request.env['ir.module.module'].sudo().search([
            ('name', 'in', ['sh_backmate_theme',
                           'sh_backmate_theme_adv', 'sh_entmate_theme']),
            ('state', '=', 'installed')
        ], limit=1).sudo()
        if theme:
            module_name = theme.name

        request.session.logout(keep_db=True)
        response = request.render(
            module_name + '.sh_backmate_theme_mobile_switch_user_template', {})
        return response

    @http.route('/sh_backmate_theme_mobile/session/check_session_expired', type='json', auth="none")
    def sh_backmate_theme_mobile_session_check_session_expired(self, session_id=None):
        if not session_id:
            return {
                'error': "1",
                "result": "'session_id` is required"
            }

        session = root.session_store.get(session_id)
        if not session:
            return {
                'error': "1",
                "result": "'session_id` is expired"
            }

        return {
            'error': "0",
            "result": "'session_id` is active"
        }

    @http.route('/api/session/authenticate', type='json', auth="none")
    def mh_authenticate(self, db, login, password, base_location=None):
        url_root = request.httprequest.url_root
        AUTH_URL = f"{url_root}web/session/authenticate/"
        headers = {'Content-type': 'application/json'}
        data = {
            "jsonrpc": "2.0",
            "params": {
                "login": login,
                "password": password,
                "db": db
            }
        }

        res = requests.post(
            AUTH_URL,
            data=json.dumps(data),
            headers=headers
        )

        try:
            session_id = res.cookies["session_id"]
            user = json.loads(res.text) or {}
            user["result"]["session_id"] = session_id
            user["result"]["status"] = 1
        except Exception:
            return {
                "status": 0,
            }
        return user["result"]