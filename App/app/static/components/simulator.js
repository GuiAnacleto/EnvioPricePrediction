const SIMULATOR = {
    template: '\
    <div class="container p-3">\
      <div class="columns">\
        <h1 class="column title is-12">Precificação</h1>\
      </div>\
      <div class="columns">\
        <div class="column is-11 is-full-mobile">\
          <input class="input is-medium" type="text" v-model="profitInput" placeholder="Valor do lucro do produto" />\
        </div>\
        <div class="column is-full-mobile">\
          <button class="button is-info is-medium is-fullwidth" @click="searchProfit">\
            <img src="../static/img/ico-search.svg" />\
          </button>\
        </div>\
      </div>\
      <div class="columns" v-if="showList">\
        <h2 class="column is-12 subtitle mt-3">Resultados das APIs</h2>\
      </div>\
      <div class="columns mb-4" v-for="(eCommerce, index) in apiResult" :key="index" v-if="showList">\
        <div class="column is-12">\
          <div class="columns">\
          <div class="column is-2 is-5-mobile">\
            <img :alt="\`${eCommerce.service} logo\`" :src="\`../static/img/${eCommerce.service}.svg\`" height="50" />\
          </div>\
            <div class="column is-10 is-7-mobile">\
              <div class="columns">\
                <div class="column is-6 is-12-mobile">\
                  <div class="input-wrapper">\
                    <label>Valor mínimo de venda</label>\
                    <input class="input" type="text" :value="formatCurrency(eCommerce.amount)" readonly />\
                  </div>\
                </div>\
                <div class="column is-6 is-12-mobile">\
                  <div class="input-wrapper">\
                    <label>Taxa do E-commerce</label>\
                    <input class="input" type="text" :value="\`${eCommerce.tax}%\`" readonly />\
                  </div>\
                </div>\
              </div>\
            </div>\
          </div>\
        </div>\
      </div>\
      <div class="columns" v-if="isLoading">\
        <img class="mx-auto mt-6" alt="Carregando" src="../static/img/loading.svg" width="100" height="100" />\
      </div>\
    </div>\
  ',
    data: function() {
        return {
            profitInput: '',
            apiResult: [],
            loading: false
        }
    },
    computed: {
        showList: function() {
            return (this.apiResult.length > 0 && !this.isLoading)
        },
        isLoading() {
            return this.loading
        }
    },
    methods: {
        formatCurrency: function(value) {
            return new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(value)
        },
        searchProfit: async function() {
            this.loading = true
            this.apiResult = []
                // API MOCK
            const result = await axios.get(`/prices/${this.profitInput}`)
            this.apiResult = result.data
            this.loading = false
        }
    }
}
RUR(() => {
    new Vue({
        el: document.getElementById('app'),
        components: {
            'simulator': SIMULATOR,
        },
    })
});