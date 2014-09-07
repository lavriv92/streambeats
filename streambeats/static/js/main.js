require.config({
  paths: {
    jquery: '../libs/jquery/dist/jquery',
    underscore: '../libs/underscore/underscore',
    backbone: '../libs/backbone/backbone',
    text: '../libs/requirejs-text/text',
    templates: '../templates'
  }, 

  shim: {
    'jquery': {
      deps: [],
      exports: '$'
    },

    'underscore': {
      deps: [],
      exports: '_'
    },

    'backbone': {
      deps: ['jquery', 'underscore'],
      exports: 'Backbone'
    }
  }
});

require(['app'], function(App) {
  App.initialize();
});
