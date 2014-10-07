/** @jsx React.DOM */

var React = require('react');

var Header = require('./header.jsx');
var Footer = require('./footer.jsx');
var Router = require('./router.jsx');

var Link = require('./link.jsx');

module.exports = React.createClass({
  render: function() {
    return (
      <div id="wrapper">
        <Header/>
        <div className="row">
          <div className="container">
            <a href="/music/albums">Albums</a>
            <a href="/music/artists">Artists</a>
            <Router />
          </div>
        </div>
        <Footer/>
      </div>
      )
  }
});
