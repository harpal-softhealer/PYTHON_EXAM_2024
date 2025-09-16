/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { session } from "@web/session";

patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
        // For regular form views (not in a dialog), if the session flag is set,
        // force the initial mode to readonly.
        if (!this.props.isDialog && session.sh_disable_auto_edit_model) {
            this.model.config.mode = 'readonly';
        }
    },
});