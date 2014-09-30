var gulp = require('gulp');
var browserify = require('browserify');
var reactify = require('reactify');
var stream = require('vinyl-source-stream');

var paths = {
  index_js: ['./frontend/main.jsx']
};

gulp.task('js', function() {
  browserify(paths.index_js)
    .transform('reactify')
    .bundle()
    .pipe(stream('app.build.js'))
    .pipe(gulp.dest('./static/js/'));
});


gulp.task('default', ['js']);
