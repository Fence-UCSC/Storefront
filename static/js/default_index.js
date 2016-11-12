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

    // Generate the URL for returning the reviews
    function get_reviews_url(start_idx, end_idx) {
        var pp = {
            start_idx: start_idx,
            end_idx: end_idx
        };
        return reviews_url + "&" + $.param(pp);
    }

    // Get the first 4 reviews from the database
    self.get_reviews = function () {
        $.getJSON(get_reviews_url(0, 4), function (data) {
            self.vue.reviews = data.reviews;
            self.vue.has_more = data.has_more;
            self.vue.logged_in = data.logged_in;
            self.vue.current_user = data.current_user;
            enumerate(self.vue.reviews);
        })
    };

    // Get 4 additional reviews from the database
    self.get_more = function () {
        var num_reviews = self.vue.reviews.length;
        $.getJSON(get_reviews_url(num_reviews, num_reviews + 4), function (data) {
            self.vue.has_more = data.has_more;
            self.extend(self.vue.reviews, data.reviews);
            enumerate(self.vue.reviews);
        });
    };

    self.add_review_button = function () {
        // The button to add a review has been pressed.
        self.vue.is_adding_review = !self.vue.is_adding_review;
    };

    self.cancel_add = function () {
        // The button to edit a review has been pressed.
        self.vue.is_adding_review = !self.vue.is_adding_review;
    };

    self.cancel_edit = function () {
        // The button to edit a review has been pressed.
        self.vue.being_edited = null;
    };

    // Add a review to the database and vue model
    self.add_review = function () {
        self.vue.add_review_button();
        $.post(add_review_url,
            {
                reviewed_id: self.vue.reviewed_id,
                review_title : self.vue.form_review_title,
                review_description: self.vue.form_review_description
            },
            function (data) {
                $.web2py.enableElement($("#add_review_submit"));
                self.vue.reviews.unshift(data.review);
                enumerate(self.vue.reviews);
                self.get_reviews();
                console.log(self.vue.stars);
            });
        self.vue.form_review_title = "";
        self.cancel_edit();

    };

    self.update_stars = function(stars) {
        self.vue.stars = stars;
    };

    // Select the review that is being edited
    self.select_review = function(review_idx) {
        self.vue.is_editing = true;
        self.vue.being_edited = review_idx;
        self.vue.current_review = self.vue.reviews[review_idx];
        self.vue.form_edit_text = self.vue.current_review.review_title;
    };

    // Edit a review
    self.edit_review = function(review_idx) {
        $.post(edit_review_url,
            {
                review_id: self.vue.reviews[review_idx].id,
                edit_text: self.vue.form_edit_text,
            },
            function (data) {
                self.vue.reviews[review_idx].review_title = self.vue.form_edit_text;
                self.get_reviews();
            });
        self.vue.form_review_title = "";
        self.cancel_edit();
        self.vue.is_editing = false;


    };

    // Delete a review
    self.delete_review = function(review_idx) {
        $.review(del_review_url,
            {
                review_id: self.vue.reviews[review_idx].id
            },
            function () {
                self.vue.reviews.splice(review_idx, 1);
                enumerate(self.vue.reviews);
                self.get_reviews();
            }
        )
    };


    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            is_adding_review: false,
            is_editing: false,
            reviews: [],
            current_review: null,
            stars: 1,
            being_edited: null,
            logged_in: false,
            current_user: null,
            has_more: false,
            form_review_title: null,
            form_review_description: null,
            form_edit_text: null,
            form_created_on: null,
        },
        methods: {
            get_more: self.get_more,
            add_review_button: self.add_review_button,
            cancel_add: self.cancel_add,
            cancel_edit: self.cancel_edit,
            add_review: self.add_review,
            select_review: self.select_review,
            edit_review: self.edit_review,
            delete_review: self.delete_review,
        }

    });

    self.get_reviews();
    $("#vue-div").show();

Vue.component('star-rating', {

  props: {
    'name': String,
    'value': null,
    'id': String,
    'disabled': Boolean,
    'required': Boolean
  },

  template: '<div class="star-rating">\
        <label class="star-rating__star" v-for="rating in ratings" \
        :class="{\'is-selected\': ((value >= rating) && value != null), \'is-disabled\': disabled}" \
        v-on:click="set(rating)" v-on:mouseover="star_over(rating)" v-on:mouseout="star_out">\
        <input class="star-rating star-rating__checkbox" type="radio" :value="rating" :name="name" \
        v-model="value" :disabled="disabled">★</label></div>',

  /*
   * Initial state of the component's data.
   */
  data: function() {
    return {
      temp_value: null,
      ratings: [1, 2, 3, 4, 5]
    };
  },

  methods: {
    /*
     * Behaviour of the stars on mouseover.
     */
    star_over: function(index) {
      //  console.log(self.vue.stars);
      var self = this;

      if (!this.disabled) {
        this.temp_value = this.value;
        return this.value = index;
      }

    },

    /*
     * Behaviour of the stars on mouseout.
     */
    star_out: function() {
      var self = this;
      if (!this.disabled) {
        return this.value = this.temp_value;
      }
    },

    /*
     * Set the rating of the score
     */
    set: function(value) {
      var self = this;
      if (!this.disabled) {
          console.log("VALUE" + value);
        this.$emit('update_stars', value);
      	// Make some call to a Laravel API using Vue.Resource
        this.temp_value = value;
        return this.value = value;
      }
    }
  }

});

var APP = null;


// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
