/** @jsx React.DOM */

var React = require('react');

var Header = require('./header.jsx');
var Footer = require('./footer.jsx');
var Router = require('./router.jsx');
var Left = require('./left.jsx');

var App = React.createClass({
  render: function() {
    return (
      <div id="wrapper">
        <Header/>
        <div className="container-fluid">
          <div className="row">
            <div className="col-md-2 col-xs-2 sidebar">
              <Left />
            </div>
            <div className="col-md-10 col-xs-10">
              <Router />
            </div>
          </div>
        </div>
        <Footer/>
      </div>
      )
  }
});

module.exports = App;
