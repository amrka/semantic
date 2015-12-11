/*jslint node: true */

'use strict';
var gulp = require('gulp');
var coffee = require('gulp-coffee');
var gutil = require('gutil');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var less = require('gulp-less');
var minifyCSS = require('gulp-minify-css');
var concat = require('gulp-concat');
var flatten = require('gulp-flatten');
var streamqueue = require('streamqueue');

gulp.task('coffee_to_js',  function() {
	return streamqueue ({ objectMode: true},
		//By including __init__ last, every other class has initialized already.
    gulp.src(['./coffee/!(__init__)*.coffee']),
    gulp.src(['./coffee/*/*.coffee']),
    gulp.src(['./coffee/__init__.coffee'])
	)
  	   	.pipe(flatten())
		.pipe(concat('all.coffee'))
		.pipe(coffee())
      	//.pipe(uglify())
        .pipe(rename({
        	extname: '.min.js'
        }))
        .pipe(gulp.dest('./js')
    );
});

gulp.task('less_to_css', function() {
  return gulp.src(['./less/*.less'])
      .pipe(less())
      .pipe(gulp.dest('./css/'));
});

gulp.task('minify_css', function() {
  return gulp.src('./css/*.css')
      .pipe(concat('all.css'))
      .pipe(minifyCSS())
       .pipe(rename({
         extname: '.min.css'
       }))
       .pipe(gulp.dest('./css/'))
});

gulp.task('default', ['less_to_css'], function() {
  gulp.start('coffee_to_js', 'minify_css');
});