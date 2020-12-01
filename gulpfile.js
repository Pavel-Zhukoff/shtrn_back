const {src,dest,series, watch} = require('gulp');
const sass = require('gulp-sass');
const csso = require('gulp-csso');
const autoprefixer = require('gulp-autoprefixer');
const concat = require('gulp-concat');
const uglify = require('gulp-uglify');
const include = require('gulp-file-include');
const babel = require('gulp-babel');
const cleanCSS = require('gulp-clean-css');
const imagemin = require('gulp-imagemin');
const del = require('del')
const assets = {
    css: [
        'app/static/website/src/css/reset.css',
        'app/static/website/src/css/variables.css',
        'app/static/website/src/css/keyframes.css',
        'app/static/website/src/css/mixins.css',
        'app/static/website/src/css/fonts.css',
        'app/static/website/src/css/modals.css',
        'app/static/website/src/css/main.css',
    ],
    js: [
       'app/static/website/src/js/schedule.js',
    ],
    images: [
        'app/static/website/src/img/**/*.{jpg,jpeg,png,svg}',
    ],
    fonts: [
        'app/static/website/src/fonts/**/*.*'
    ]
}

function scss() {
     return src(assets.css)
        .pipe(sass())
        .pipe(autoprefixer({

        }))
        .pipe(csso())
        .pipe(concat('app.min.css'))
         .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(dest('app/static/website/dist/css/'))
}
function js() {
    return src(assets.js)
        .pipe(babel({
            presets: ['@babel/preset-env']
        }))
        .pipe(uglify())
        .pipe(concat('app.min.js'))
        .pipe(dest('app/static/website/dist/js/'))
}
function images() {
    return src(assets.images)
        .pipe(imagemin())
        .pipe(dest('app/static/website/dist/img/'))
}
function fonts() {
    return src(assets.fonts)
        .pipe(dest('app/static/website/dist/fonts/'))
}
function clear() {
    return del('app/static/website/dist')
}
function serve() {
    console.log('Dev serve watcher has been started')
    watch('app/static/website/src/css/',series(scss)).on('change',series(scss))
    watch('app/static/website/src/js/',series(js)).on('change',series(js))
    watch('app/static/website/src/fonts/',series(fonts)).on('change',series(fonts))
    watch('app/static/website/src/img/',series(images)).on('change',series(images))
}
exports.scss = scss
exports.js = js
exports.images = images
exports.fonts = fonts
exports.clear = clear
exports.serve = serve
exports.build = series(scss,images,js,fonts)