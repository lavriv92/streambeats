define(['jquery','backbone'], function($, Backbone) {
  var LeftPanel = Backbone.View.extend({
    el: $('#left'),
        
    events: {
      'click .hide': 'hidePanel',
      'click .show': 'showPanel',
    },

    hidePanel: function() {
      $(this.$el).fadeIn();
    },

    showPanel: function() {
      $(this.$el).fadeOut();
    }
  });

  return LeftPanel;
});
