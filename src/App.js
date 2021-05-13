export default {
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
      this.results = {topRated: [], similar: []};
      this.movie = '';
      this.togglePanels();
    },
    togglePanels() {
      this.showingForm = !this.showingForm;
      this.showingResults = !this.showingResults;
    },
    imbdSearch(e) {
      let text = e.target.innerText;

      window.open(
        `https://www.imdb.com/find?q=${text}`,
        '_blank'
      );
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
        }
        else {
          this.movie = '';
          alert("Movie not found! Enter another.");
        }
      }).catch(() => {
          throw new Error('Recommendation service failed.');
      })
    }
  },
  render() {
    return (
      <div class="container h-100">
        <div class="d-flex justify-content-center align-items-center h-100">
          <b-card
            text-variant="white"
            bg-variant="transparent"
            class="justify-content-center text-center border-0"
            style="width: 35rem;"
          >
          {
            this.showingForm &&
            <div>
              <b-card-text class="mb-4 mb-md-5" style="font-size: 4rem; line-height: 0.55;">MovieAI</b-card-text>

              <p>Welcome to MovieAI, a service which gives you movie recommendations based on one that you input.
                Please input a movie you have watched that you enjoyed into the field below and click 'submit'.
              </p>

              <div>
                <b-form-group
                  class="mb-1 mb-md-4"
                  id="input-group-1"
                  label="Movie"
                  label-for="movie"
                >
                  <b-form-input
                    v-model={this.movie}
                    id="input-1"
                    type="text"
                    placeholder="Enter a movie name"
                    size="lg"
                    required
                  />
                </b-form-group>

                <b-button type="button" size="lg" class="col-12 mt-2" variant="primary" onClick={this.getRecommendations}>Submit</b-button>
              </div>
            </div>
          }

          {
            this.showingResults &&
            <div>
              <b-card-text class="mb-4" style="font-size: 4rem; line-height: 0.55;">Results</b-card-text>
              <p>Click on the results to search them on IMDB.</p>
              
              {
                (this.results.similar.length > 0) &&
                <div>
                  <b-card-text class="mt-4" style="font-size: 1.5rem; line-height: 0.55;">Similar movies</b-card-text>
                  {
                    this.results.similar.map((result) => {
                      return (
                        <b-button size="md" class="col-12 mb-2" variant="secondary" onClick={this.imbdSearch}>{result}</b-button>
                      )
                    })
                  }
                </div>
              }

              <b-card-text class="mt-4" style="font-size: 1.5rem; line-height: 0.55;">Top movies in this genre</b-card-text>
              {
                this.results.topRated.map((result) => {
                  return (
                    <b-button size="md" class="col-12 mb-2" variant="secondary" onClick={this.imbdSearch}>{result}</b-button>
                  )
                })
              }

              <b-button size="lg" class="col-12 mt-4" variant="primary" href="/">Start again</b-button>
            </div>
          }
          </b-card>
        </div>
      </div>
    )
  }
}