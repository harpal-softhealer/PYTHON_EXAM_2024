/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ListController } from "@web/views/list/list_controller";
import { useEffect } from "@odoo/owl";

const EXPAND_COLLAPSE_STATE_KEY = "sh_entmate_theme_list_view_expand_state";

patch(ListController.prototype, {
    setup() {
        super.setup(...arguments);

        useEffect(
            () => {
                const groups = this.model.root.groups;
                if (groups && groups.length > 0) {
                    const savedState = localStorage.getItem(EXPAND_COLLAPSE_STATE_KEY);
                    if (savedState === "expanded") {
                        this.model.expandAll();
                    } else if (savedState === "collapsed") {
                        this.model.collapseAll();
                    }
                }
            },
            () => [this.model.root.groups]
        );
    },

    /**
     * Expands all groups and saves the state.
     */
    onExpandAllGroups() {
        this.model.expandAll();
        localStorage.setItem(EXPAND_COLLAPSE_STATE_KEY, "expanded");
    },

    /**
     * Collapses all groups and saves the state.
     */
    onCollapseAllGroups() {
        this.model.collapseAll();
        localStorage.setItem(EXPAND_COLLAPSE_STATE_KEY, "collapsed");
    },
});
