'use strict';
define(['jquery', 'underscore', 'backbone',
    '../collections/albums', 
    'text!templates/albums.html'], function($, _, Backbone, Albums, t) {
  var AlbumsView = Backbone.View.extend({
    el: $('#ui-view'),
    template: _.template(t),
    collection: new Albums(),
    self: this,

    initialize: function() {
      this.collection.fetch();
      this.collection.bind('reset', this.render, this);
    },

    render: function() {  
      console.log(this.collection.toJSON());
      this.$el.html(this.template);
    }
  });

  return AlbumsView;
});
