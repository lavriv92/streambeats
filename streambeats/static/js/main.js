requirejs.config({
  paths: {
    jquery: '../libs/jquery/dist/jquery',
    underscore: '../libs/underscore/underscore',
    backbone: '../libs/backbone/backbone',
    text: '../libs/requirejs-text/text',
    templates: '../templates'
  },

  shim: {
    'jquery': {
      depts: [],
      exports: '$'
    },
    'underscore': {
      depts: [],
      exports: '_'
    },
    'backbone': {
      depts: ['jquery', 'underscore'],
      exports: 'Backbone'
    }
  }
});

require(['app'], function(App) {
  App.initialize();
});
