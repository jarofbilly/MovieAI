"use strict";

new Vue({
  el: '#VueApp',
  data: function data() {
    return {
      test: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      facts: []
    };
  },
  methods: {
    getData: function getData() {
      var _this = this;

      var url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=5';
      fetch(url).then(function (response) {
        return response.json();
      }).then(function (json) {
        _this.facts = json;
        console.log(json);
      });
    }
  },
  mounted: function mounted() {
    this.getData();
  },
  render: function render() {
    var h = arguments[0];
    return h("div", [this.facts.map(function (item) {
      return h("h1", [item.text]);
    })]);
  }
});