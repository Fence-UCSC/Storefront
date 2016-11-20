// This is the js for the default/index.html view.


var app = function() {

    var self = {};

    Vue.config.silent = false; // show all warnings

    // Extends an array
    self.extend = function(a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };

    // Enumerates an array.
    var enumerate = function(v) {
        var k=0;
        return v.map(function(e) {e._idx = k++;});
    };


    self.cancel_add = function () {
        // The button to edit a review has been pressed.
        self.vue.is_posting = !self.vue.is_posting;
        $("#contactOn").slideDown();
        console.log(self.vue.is_posting);
    };


    self.contact_seller = function () {
        self.vue.is_posting = true;
        $.post(contact_seller_url,
            {
                reviewed_id: self.vue.reviewed_id,
                review_title : self.vue.form_review_title,
                review_description: self.vue.form_review_description,
                vote: self.vue.stars
            },
            function (data) {
                self.vue.is_posting = false;
                self.vue.is_successful = true;
            });
    };


    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            is_posting: false,
            is_successful: false,
        },
        methods: {
            contact_seller: self.contact_seller,
            cancel_add: self.cancel_add
        }
    });


    $("#vue-div").show();

 };


var APP = null;


// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});/**
 * Created by tommaso on 20/11/16.
 */

$("#interest").click(function(){
    $("#contactOn").slideUp();
});