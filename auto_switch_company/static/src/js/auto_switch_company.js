odoo.define('autoswitchcompany.AutoSwitchCompanyMenu', function(require) {
"use strict";

var session = require('web.session');
var core = require('web.core');
var WebClient = require('web.WebClient');
var Model = require('web.Model');

WebClient.include({
	do_switch_company: function(action) {
		var self = this;
		var company_id = null;
		if (action.hasOwnProperty('context')){
			if (action.context.hasOwnProperty('auto_switch_company_id')){
				company_id = action.context.auto_switch_company_id;
			}
		}
		for (var i=0; i<self.systray_menu.widgets.length; i++) {
			var widget = self.systray_menu.widgets[i];
			if (widget.el.className == 'o_switch_company_menu') {
				if (company_id != null && company_id != session.user_companies.current_company[0]){
					session.user_companies.current_company[0] = company_id;
					session.user_companies.current_company[1] = self._get_company_name(company_id);
					new Model('res.users').call('write', [[session.uid], {'company_id': company_id}]).then(function() {
		                self.$('.o_switch_company_menu .oe_topbar_name').text(session.user_companies.current_company[1]);
		                var companies_list = '';
		                _.each(session.user_companies.allowed_companies, function(company) {
		                    var a = '';
		                    if (company[0] === session.user_companies.current_company[0]) {
		                        a = '<i class="fa fa-check o_current_company"></i>';
		                    } else {
		                        a = '<span class="o_company"/>';
		                    }
		                    companies_list += '<li><a href="#" data-menu="company" data-company-id="' + company[0] + '">' + a + company[1] + '</a></li>';
		                });
		                self.$('.o_switch_company_menu .dropdown-menu[role="menu"]').html(companies_list);
		                self.$('.o_sub_menu_logo img').attr("src", '/web/binary/company_logo?company=' + company_id);
		            });
				}
			}
		}
	},

	_get_company_name: function(company_id) {
		var company_name = '';
		for (var i=0; i<session.user_companies.allowed_companies.length; i++) {
			if (session.user_companies.allowed_companies[i][0] == company_id) {
				company_name = session.user_companies.allowed_companies[i][1];
			}
		}
		return company_name;
	},

    show_application: function() {
    	var self = this;
    	return this._super.apply(this, arguments).done(function () {
    		core.bus.on('action', self, self.do_switch_company);
    	});
    }
});
});