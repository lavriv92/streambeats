/** @jsx React.DOM */

var React = require('react');
var Albums = require('../../collections/albums.jsx');


module.exports = React.createClass({

  collection: new Albums(),

  getInitialState: function() {
    return {
      albums: []  
    };
  },  
  
  componentDidMount: function() {
    var self = this;
    this.collection.on('sync', function(data) {  
      self.setState({albums: self.collection.toJSON()});
    });
    this.collection.fetch();

  },  

  render: function() {
    var AlbumsNodes = this.state.albums.map(function(album) {
      return <h3>{album.name}</h3>
    });

    return (
        <div>
          <h2>Albums</h2>
          <div>{AlbumsNodes}</div>
        </div>
        )
  }
});
