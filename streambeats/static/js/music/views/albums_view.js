'use strict';
define(['jquery', 'underscore', 'backbone', '../collections/albums', 
    'text!templates/albums.html'], 
function($, _, Backbone, Albums, t) {
  var AlbumsView = Backbone.View.extend({
    el: $('#ui-view'),
    template: _.template(t),
    collection: new Albums(),
    self: this,

    initialize: function() {
      this.collection.fetch();
      this.collection.bind('all', this.render, this);
    },

    render: function() {  
      this.$el.html(this.template({'albums': this.collection.toJSON()}));
      return this;
    }
  });

  return AlbumsView;
});
