// the js for default/search.html

var app = function() {

    var self = {};

    Vue.config.silent = false;  // show all warnings

    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            products: [],
            has_more: false
        },
    });

    return self;
};

var APP = null;

jQuery(function(){APP = app();});