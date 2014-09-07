'use strict';
define(['jquery', 'underscore', 'backbone',
  '../models/current_user',
  'text!templates/index.html'
], function($, _, Backbone, User, temp) {
  var IndexView = Backbone.View.extend({
    el: $("#ui-view"),

    template: _.template(temp),

    events: {
      'click button': 'clickMain'
    },

    render: function() {
      this.$el.html(this.template); 
    }
  });

  return IndexView;
});
