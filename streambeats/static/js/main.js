requirejs.config({
  paths: {
    jquery: '../libs/jquery/dist/jquery',
    underscore: '../libs/underscore/underscore',
    backbone: '../libs/backbone/backbone',
    text: '../libs/requirejs-text/text',
    templates: '../templates'
  }
});

require(['app'], function(App) {
  App.initialize();
});
