odoo.define("sh_open_record_in_new_tab.Open_records", function (require) {
  "use strict";

  var ListRenderer = require("web.ListRenderer");
  // Open Record feature Access Variable :-
  const rpc = require("web.rpc");
  var session = require('web.session');
  var core = require('web.core');
  var view_type = null;

  var show_open_record_new_tab_button = false
  rpc.query({
    model: 'res.users',
    method: 'search_read',
    fields: ['sh_enable_open_record_in_new_tab'],
    domain: [['id', '=', session.uid]]
  }, { async: false }).then(function (data) {
    if (data) {
      _.each(data, function (user) {
        if (user.sh_enable_open_record_in_new_tab) {

          show_open_record_new_tab_button = true
        }
      });

    }
  });


  core.bus.on('DOM_updated', null, function () {
    if (show_open_record_new_tab_button && view_type) {
      // Your code to execute after the page loads
      var trsWithColspan6 = $('tr:has(td[colspan])');
      trsWithColspan6.each(function () {
        $(this).append('<td></td>');
      });
    }
    view_type = null;
  });
  const Open_records = ListRenderer.include({
    events: _.extend({}, ListRenderer.prototype.events, {
      "click .open_record_new_tab": "_OpenRecord",
    }),
    /**
     * @override
     */

    _renderRow: function (record) {
      if (this.activeActions) {
        view_type = this.activeActions
      }
      // console.log("\n\n\n\n View Type", view_type);
      var $tr = this._super.apply(this, arguments);
      $tr.find('.open_record_new_tab').attr('data-res_id',record.res_id);
      return $tr;
    },

    _renderSelector: function (tag, disableInput, id) {
      var $mainElement = this._super.apply(this, arguments);
      if (tag == "th") {
        var $additionalTd = $("<th>").text("Open");

        var $combineElement = $mainElement.add($additionalTd);
      } else {
        var $button = $(
          '<button type="button" class="btn btn-primary py-1 px-2 h6 text-white m-0 open_record_new_tab">Click</button>'
        );
        var $additionalTd = $("<td>").append($button);

        var $combineElement = $mainElement.add($additionalTd);
      }
      // console.log("\n\n\n show_open_record_new_tab_button", show_open_record_new_tab_button);
      if (show_open_record_new_tab_button) {
        return $combineElement;
      }
      else {
        return $mainElement;
      }
    },

    _renderFooter: function () {
        if (this.activeActions) {
          view_type = this.activeActions
        }
      var aggregates = {};
      _.each(this.columns, function (column) {
        if ('aggregate' in column) {
          aggregates[column.attrs.name] = column.aggregate;
        }
      });
      var $cells = this._renderAggregateCells(aggregates);
      if (this.hasSelectors) {
        $cells.unshift($('<td>'));
      }
        $cells.unshift($('<td></td>'));
        // console.log("\n\n\n\n View type", view_type);
      
      if (show_open_record_new_tab_button && view_type) {
        return $('<tfoot>').append($('<tr>').append($cells));
      }
      else{
        var $tfoot = this._super.apply(this, arguments);
        return $tfoot;
      }
    },

  //   _renderFooter: function () {
  //     var aggregates = {};
  //     _.each(this.columns, function (column) {
  //         if ('aggregate' in column) {
  //             aggregates[column.attrs.name] = column.aggregate;
  //         }
  //     });
  //     var $cells = this._renderAggregateCells(aggregates);
  //     if (this.hasSelectors) {
  //         $cells.unshift($('<td>'));
  //     }
  //     var $tfoot = this._super.apply(this, arguments);
  //     return $tfoot;
  // },

    _OpenRecord(ev) {
      ev.stopPropagation();
      var res_id = $(ev.currentTarget).attr('data-res_id');
      var url = window.location.href;
      var latest_url = url + "&id=" + res_id;
      let result = latest_url.replace("view_type=list", "view_type=form");
      window.open(result, "_blank");
    },

    _processColumns: function (columnInvisibleFields) {
      if (show_open_record_new_tab_button) {
      this._super(columnInvisibleFields);
      setTimeout(function () {
        // Softhealer Custom Code :-
        var trsWithGroupheader = $('tr:has(th.o_group_name)');
        trsWithGroupheader.each(function () {
          var hasCustomClass = false;

          // Check if any <td> inside the <tr> contains the custom class
          $(this).find("td").each(function () {
            if ($(this).hasClass("sh_custom_class")) {
              hasCustomClass = true;
              return false; // Exit the loop if the custom class is found in a <td>
            }
          });

          // If the custom class is not found, add a new <td> with the custom class
          if (!hasCustomClass) {
            // $(this).append("<td class='sh_custom_class'>New TD with custom class</td>");
            $(this).children().eq(0).after("<td class='sh_custom_class'></td>");
          }
        });
      }, 40);
    }
    else {
      this._super(columnInvisibleFields);
    }
    },
  });
});
