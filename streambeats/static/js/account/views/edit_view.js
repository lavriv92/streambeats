define(['jquery', 'underscore', 'backbone', 
  '../models/current_user', 'text!templates/account/edit.html'], 
  function($, _, Backbone, CurrentUser, t) {
  
  var AccountEditView = Backbone.View.extend({
    el: $('#ui-view'),
    model: new CurrentUser(),

    events: {
      
    },

    render: function() {
      var compiled = _.template(t, {'user': this.model.attributes});
      this.$el.html(compiled);  
    },

    save: function() {
    
    }
  });

  return AccountEditView;
})
