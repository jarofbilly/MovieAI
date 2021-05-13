/******/ (function(modules) { // webpackBootstrap
/******/ 	// install a JSONP callback for chunk loading
/******/ 	function webpackJsonpCallback(data) {
/******/ 		var chunkIds = data[0];
/******/ 		var moreModules = data[1];
/******/ 		var executeModules = data[2];
/******/
/******/ 		// add "moreModules" to the modules object,
/******/ 		// then flag all "chunkIds" as loaded and fire callback
/******/ 		var moduleId, chunkId, i = 0, resolves = [];
/******/ 		for(;i < chunkIds.length; i++) {
/******/ 			chunkId = chunkIds[i];
/******/ 			if(Object.prototype.hasOwnProperty.call(installedChunks, chunkId) && installedChunks[chunkId]) {
/******/ 				resolves.push(installedChunks[chunkId][0]);
/******/ 			}
/******/ 			installedChunks[chunkId] = 0;
/******/ 		}
/******/ 		for(moduleId in moreModules) {
/******/ 			if(Object.prototype.hasOwnProperty.call(moreModules, moduleId)) {
/******/ 				modules[moduleId] = moreModules[moduleId];
/******/ 			}
/******/ 		}
/******/ 		if(parentJsonpFunction) parentJsonpFunction(data);
/******/
/******/ 		while(resolves.length) {
/******/ 			resolves.shift()();
/******/ 		}
/******/
/******/ 		// add entry modules from loaded chunk to deferred list
/******/ 		deferredModules.push.apply(deferredModules, executeModules || []);
/******/
/******/ 		// run deferred modules when all chunks ready
/******/ 		return checkDeferredModules();
/******/ 	};
/******/ 	function checkDeferredModules() {
/******/ 		var result;
/******/ 		for(var i = 0; i < deferredModules.length; i++) {
/******/ 			var deferredModule = deferredModules[i];
/******/ 			var fulfilled = true;
/******/ 			for(var j = 1; j < deferredModule.length; j++) {
/******/ 				var depId = deferredModule[j];
/******/ 				if(installedChunks[depId] !== 0) fulfilled = false;
/******/ 			}
/******/ 			if(fulfilled) {
/******/ 				deferredModules.splice(i--, 1);
/******/ 				result = __webpack_require__(__webpack_require__.s = deferredModule[0]);
/******/ 			}
/******/ 		}
/******/
/******/ 		return result;
/******/ 	}
/******/
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// object to store loaded and loading chunks
/******/ 	// undefined = chunk not loaded, null = chunk preloaded/prefetched
/******/ 	// Promise = chunk loading, 0 = chunk loaded
/******/ 	var installedChunks = {
/******/ 		"app": 0
/******/ 	};
/******/
/******/ 	var deferredModules = [];
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/";
/******/
/******/ 	var jsonpArray = window["webpackJsonp"] = window["webpackJsonp"] || [];
/******/ 	var oldJsonpFunction = jsonpArray.push.bind(jsonpArray);
/******/ 	jsonpArray.push = webpackJsonpCallback;
/******/ 	jsonpArray = jsonpArray.slice();
/******/ 	for(var i = 0; i < jsonpArray.length; i++) webpackJsonpCallback(jsonpArray[i]);
/******/ 	var parentJsonpFunction = oldJsonpFunction;
/******/
/******/
/******/ 	// add entry module to deferred list
/******/ 	deferredModules.push([0,"chunk-vendors"]);
/******/ 	// run deferred modules when ready
/******/ 	return checkDeferredModules();
/******/ })
/************************************************************************/
/******/ ({

/***/ 0:
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__("56d7");


/***/ }),

/***/ "56d7":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
// ESM COMPAT FLAG
__webpack_require__.r(__webpack_exports__);

// EXTERNAL MODULE: ./node_modules/vue/dist/vue.runtime.esm.js
var vue_runtime_esm = __webpack_require__("2b0e");

// CONCATENATED MODULE: ./src/App.js
/* harmony default export */ var App = ({
  name: 'App',
  data: () => ({
    movie: '',
    showingForm: true,
    showingResults: false,
    results: {
      topRated: [],
      similar: []
    }
  }),
  methods: {
    reset() {
      this.results = {
        topRated: [],
        similar: []
      };
      this.movie = '';
      this.togglePanels();
    },

    togglePanels() {
      this.showingForm = !this.showingForm;
      this.showingResults = !this.showingResults;
    },

    imbdSearch(e) {
      let text = e.target.innerText;
      window.open(`https://www.imdb.com/find?q=${text}`, '_blank');
    },

    getRecommendations() {
      fetch(`${window.location.origin}/search/${this.movie}`, {
        method: 'GET'
      }).then(response => {
        return response.json();
      }).then(data => {
        if ("topRated" in data) {
          this.results.topRated = data.topRated;
          this.results.similar = data.similar;
          this.togglePanels();
        } else {
          this.movie = '';
          alert("Movie not found! Enter another.");
        }
      }).catch(() => {
        throw new Error('Recommendation service failed.');
      });
    }

  },

  render() {
    const h = arguments[0];
    return h("div", {
      "class": "container h-100"
    }, [h("div", {
      "class": "d-flex justify-content-center align-items-center h-100"
    }, [h("b-card", {
      "attrs": {
        "text-variant": "white",
        "bg-variant": "transparent"
      },
      "class": "justify-content-center text-center border-0",
      "style": "width: 35rem;"
    }, [this.showingForm && h("div", [h("b-card-text", {
      "class": "mb-4 mb-md-5",
      "style": "font-size: 4rem; line-height: 0.55;"
    }, ["MovieAI"]), h("p", ["Welcome to MovieAI, a service which gives you movie recommendations based on one that you input. Please input a movie you have watched that you enjoyed into the field below and click 'submit'."]), h("div", [h("b-form-group", {
      "class": "mb-1 mb-md-4",
      "attrs": {
        "id": "input-group-1",
        "label": "Movie",
        "label-for": "movie"
      }
    }, [h("b-form-input", {
      "attrs": {
        "id": "input-1",
        "type": "text",
        "placeholder": "Enter a movie name",
        "size": "lg",
        "required": true
      },
      "model": {
        value: this.movie,
        callback: $$v => {
          this.movie = $$v;
        }
      }
    })]), h("b-button", {
      "attrs": {
        "type": "button",
        "size": "lg",
        "variant": "primary"
      },
      "class": "col-12 mt-2",
      "on": {
        "click": this.getRecommendations
      }
    }, ["Submit"])])]), this.showingResults && h("div", [h("b-card-text", {
      "class": "mb-4",
      "style": "font-size: 4rem; line-height: 0.55;"
    }, ["Results"]), h("p", ["Click on the results to search them on IMDB."]), this.results.similar.length > 0 && h("div", [h("b-card-text", {
      "class": "mt-4",
      "style": "font-size: 1.5rem; line-height: 0.55;"
    }, ["Similar movies"]), this.results.similar.map(result => {
      return h("b-button", {
        "attrs": {
          "size": "md",
          "variant": "secondary"
        },
        "class": "col-12 mb-2",
        "on": {
          "click": this.imbdSearch
        }
      }, [result]);
    })]), h("b-card-text", {
      "class": "mt-4",
      "style": "font-size: 1.5rem; line-height: 0.55;"
    }, ["Top movies in this genre"]), this.results.topRated.map(result => {
      return h("b-button", {
        "attrs": {
          "size": "md",
          "variant": "secondary"
        },
        "class": "col-12 mb-2",
        "on": {
          "click": this.imbdSearch
        }
      }, [result]);
    }), h("b-button", {
      "attrs": {
        "size": "lg",
        "variant": "primary",
        "href": "/"
      },
      "class": "col-12 mt-4"
    }, ["Start again"])])])])]);
  }

});
// EXTERNAL MODULE: ./node_modules/bootstrap-vue/esm/index.js + 295 modules
var esm = __webpack_require__("5f5b");

// EXTERNAL MODULE: ./node_modules/bootstrap-vue/dist/bootstrap-vue.css
var bootstrap_vue = __webpack_require__("2dd8");

// CONCATENATED MODULE: ./src/main.js




vue_runtime_esm["default"].use(esm["a" /* BootstrapVue */]);
vue_runtime_esm["default"].config.productionTip = false;
new vue_runtime_esm["default"]({
  render: h => h(App)
}).$mount('#app');

/***/ })

/******/ });
//# sourceMappingURL=app.a29e8a6b.js.map