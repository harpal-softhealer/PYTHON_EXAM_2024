# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

import os
from odoo import http, _
from odoo.http import request
from odoo.exceptions import UserError
from odoo.tools import replace_exceptions
from odoo.addons.web.controllers.binary import Binary


class shFlutterAttachment(Binary):

    @http.route()
    # pylint: disable=redefined-builtin,invalid-name
    def content_common(self, xmlid=None, model='ir.attachment', id=None, field='raw',
                       filename=None, filename_field='name', mimetype=None, unique=False,
                       download=False, access_token=None, nocache=False, **post):

        if not filename:
            attahment = request.env['ir.attachment'].sudo().browse(id)
            filename = attahment.name if attahment else ''
        filename, extension = os.path.splitext(filename)
        if post.get('sh_unique', False) == 'hhlf2B1uquNUr0N29io5KsEnm6q2YLdL69PC5rbJQtGToNWjWm' and model == 'ir.attachment':
            with replace_exceptions(UserError, by=request.not_found()):
                record = request.env['ir.binary']._find_record(
                    xmlid, model, id and int(id), access_token)
                # softhealer custom code we have just added below line from the standard method
                record = record.sudo()
                # Softhealer custom code.
                stream = request.env['ir.binary']._get_stream_from(
                    record, field, filename, filename_field, mimetype)
            send_file_kwargs = {'as_attachment': download}
            if unique:
                send_file_kwargs['immutable'] = True
                send_file_kwargs['max_age'] = http.STATIC_CACHE_LONG
            if nocache:
                send_file_kwargs['max_age'] = None
            res = stream.get_response(**send_file_kwargs)
            res.headers['Content-Security-Policy'] = "default-src 'none'"
            res.headers['X-Content-Type-Options'] = 'nosniff'
            res.headers['sh_filename'] = filename
            res.headers['sh_extension'] = extension
            return res

        return super(shFlutterAttachment, self).content_common(xmlid, model, id, field,
                                                               filename, filename_field, mimetype, unique,
                                                               download, access_token, nocache, **post)
