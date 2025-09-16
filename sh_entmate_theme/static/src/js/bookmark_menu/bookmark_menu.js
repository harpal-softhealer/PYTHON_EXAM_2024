
/* @odoo-module */

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, useState, onWillStart, onMounted, onWillUnmount, useRef } from "@odoo/owl";

export class BookmarkMenu extends Component {
    static template = "sh_entmate_theme.bookmark_menu";

    setup() {
        this.actionService = useService("action");
        this.state = useState({
            bookmarks: [],
            showPopup: false,
        });
        this.root = useRef("bookmark-menu");

        onWillStart(() => {
            this.loadBookmarks();
        });

        onMounted(() => {
            document.addEventListener("click", this._onOutsideClick.bind(this), true);
        });

        onWillUnmount(() => {
            document.removeEventListener("click", this._onOutsideClick.bind(this), true);
        });
    }

    //--------------------------------------------------------------------------
    // Getters
    //--------------------------------------------------------------------------

    /**
     * @returns {string}
     */
    getCurrentURL() {
        return window.location.href;
    }

    /**
     * @returns {string}
     */
    getCurrentURLName() {
        const currentAction = this.actionService.currentController?.action;
        if (currentAction) {
            return currentAction.display_name || currentAction.name || "Odoo Page";
        }
        return document.title || "Odoo Page";
    }

    /**
     * @returns {boolean}
     */
    isUrlBookmarked() {
        const currentUrl = this.getCurrentURL();
        return this.state.bookmarks.some(b => b.url === currentUrl);
    }

    //--------------------------------------------------------------------------
    // Local Storage Operations
    //--------------------------------------------------------------------------

    loadBookmarks() {
        const bookmarks = JSON.parse(localStorage.getItem("sh_theme_bookmarks") || "[]");
        this.state.bookmarks = bookmarks;
    }

    saveBookmarks() {
        localStorage.setItem("sh_theme_bookmarks", JSON.stringify(this.state.bookmarks));
    }

    //--------------------------------------------------------------------------
    // Event Handlers
    //--------------------------------------------------------------------------

    /**
     * Single click: Toggles the bookmark list visibility.
     * @param {MouseEvent} ev
     */
    _onClick(ev) {
        this.state.showPopup = !this.state.showPopup;
    }

    /**
     * Double click: Adds or removes the current URL from bookmarks.
     * @param {MouseEvent} ev
     */
    _onDblClick(ev) {
        const currentUrl = this.getCurrentURL();
        const currentName = this.getCurrentURLName();
        const existingIndex = this.state.bookmarks.findIndex(b => b.url === currentUrl);

        if (existingIndex > -1) {
            // Remove bookmark
            this.state.bookmarks.splice(existingIndex, 1);
        } else {
            // Add bookmark
            this.state.bookmarks.push({ name: currentName, url: currentUrl });
        }
        this.saveBookmarks();
    }

    /**
     * Handles click on a bookmark item to navigate.
     * @param {Object} bookmark
     */
    _onBookmarkClick(bookmark) {
        window.location.href = bookmark.url;
        this.state.showPopup = false;
    }

    /**
     * Handles click on the delete button for a bookmark.
     * @param {Object} bookmark
     */
    _onDeleteClick(bookmark) {
        const index = this.state.bookmarks.findIndex(b => b.url === bookmark.url);
        if (index > -1) {
            this.state.bookmarks.splice(index, 1);
            this.saveBookmarks();
        }
    }

    /**
     * Closes the popup if a click is detected outside the component.
     * @param {MouseEvent} ev
     */
    _onOutsideClick(ev) {
        if (this.state.showPopup && !this.root.el.contains(ev.target)) {
            this.state.showPopup = false;
        }
    }
}

registry.category("systray").add("sh_entmate_theme.bookmark_menu", {
    Component: BookmarkMenu,
}, { sequence: 30 });
