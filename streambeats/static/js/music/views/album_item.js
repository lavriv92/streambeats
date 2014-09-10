define(['jquery', 'underscore', 'backbone', 
    'text!templates/album_item.html'], 
function($, _, Backbone, t) {
  var AlbumItem = Backbone.View.extend({
    el:  $('#ui-view'),
    template: _.template(t),

    initialize: function() {
      this.model.bind('all', this.render, this);
      return this;
    },

    render: function() {
      this.$el.html(this.template({'album': this.model.toJSON()}));
    },
  });

  return AlbumItem;
});
