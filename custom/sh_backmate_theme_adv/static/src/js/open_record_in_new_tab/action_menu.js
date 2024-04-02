/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import ActionMenus from "web.ActionMenus";

patch(ActionMenus.prototype, "sh_add_custom_inside_action", {
  /**
   * @override
   */

  _onItemSelected(ev) {
    if (ev.originalComponent.props.hotkeyTitle) {
      let record_activeIds = this.props.activeIds;
      for (var j in record_activeIds) {
        var url = window.location.href;
        var latest_url = url + "&id=" + record_activeIds[j];
        let result = latest_url.replace("view_type=list", "view_type=form");
        window.open(result, "_blank");
      }
    } else {
      this._super(ev);
    }
  },
});
