/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import DropdownMenu from "web.DropdownMenu";

const rpc = require("web.rpc");
var session = require('web.session');
var show_open_record_new_tab_button = false
  rpc.query({
    model: 'res.users',
    method: 'search_read',
    fields: ['sh_enable_open_record_in_new_tab'],
    domain: [['id', '=', session.uid]]
  }, { async: false }).then(function (data) {
    console.log("\n\n\n Data", data);
    if (data) {
      _.each(data, function (user) {
        if (user.sh_enable_open_record_in_new_tab) {

          show_open_record_new_tab_button = true
        }
      });

    }
  });


patch(DropdownMenu.prototype, "sh_add_custom_inside_action_dropdown", {
  setup() {
    this.show_open_record_new_tab_button = show_open_record_new_tab_button
  }
});
