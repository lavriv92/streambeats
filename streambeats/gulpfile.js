var gulp = require('gulp');
var browserify = require('browserify');
var reactify = require('reactify');
var stream = require('vinyl-source-stream');
var less = require('gulp-less');
var path = require('path');
var watch = require('gulp-watch');

var paths = {
  index_js: ['./frontend/components/main.jsx'],
  index_less: ['./frontend/stylesheets/*.less']
};

gulp.task('js', function() {
  browserify(paths.index_js)
    .transform('reactify')
    .bundle()
    .pipe(stream('app.build.js'))
    .pipe(gulp.dest('./static/js/'));
});

gulp.task('compile-less', function() {
  gulp.src(paths.index_less)
    .pipe(less({
      paths: [path.join(__dirname, 'less', 'includes')]
    }))
    .pipe(gulp.dest('./static/css/'))
});

gulp.task('watch', function() {
  gulp.watch(['./frontend/**/*.jsx'], ['js']);
  gulp.watch('./frontend/**/*.less', ['compile-less']);
});

gulp.task('default', ['watch']);
