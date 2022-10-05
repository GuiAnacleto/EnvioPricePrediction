const SIMULATOR = {
  template: '\
  <div class="container p-3">\
    <div class="columns">\
      <h1 class="column title is-12">Precificação</h1>\
    </div>\
    <div class="columns">\
      <div class="column is-4 is-full-mobile">\
        <input class="input is-medium" type="text" v-model="sku" placeholder="SKU do Produto" />\
      </div>\
      <div class="column is-2 is-full-mobile">\
        <input class="input is-medium" type="text" v-model="goverment_taxes" placeholder="Imposto" />\
      </div>\
      <div class="column is-4 is-full-mobile">\
        <input class="input is-medium" type="text" v-model="profitInput" placeholder="Valor a cobrar" />\
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
        <div class="columns is-desktop is-flex is-flex-wrap-wrap">\
          <div class="column is-2 is-two-fifths-mobile is-flex is-justify-content-center is-align-content-center">\
            <img class="logo my-auto" :alt="\`${eCommerce.service} logo\`" :src="\`../static/img/${eCommerce.service}.svg\`" height="50" />\
          </div>\
          <div class="column is-10 is-three-fifths-mobile">\
            <div class="columns">\
              <div class="column is-3 is-full-mobile">\
                <div class="input-wrapper">\
                  <label>Taxa do E-commerce</label>\
                  <input class="input" type="text" :value="formatCurrency(eCommerce.tax)" readonly />\
                </div>\
              </div>\
              <div class="column is-3 is-full-mobile">\
                <div class="input-wrapper">\
                  <label>Frete</label>\
                  <input class="input" type="text" :value="formatCurrency(eCommerce.shipping)" readonly />\
                </div>\
              </div>\
              <div class="column is-3 is-full-mobile">\
                <div class="input-wrapper">\
                  <label>Impostos</label>\
                  <input class="input" type="text" :value="formatCurrency(eCommerce.goverment_taxes)" readonly />\
                </div>\
              </div>\
              <div class="column is-3 is-full-mobile">\
                <div class="input-wrapper">\
                  <label>Valor a Receber</label>\
                  <input class="input" type="text" :value="formatCurrency(eCommerce.amount)" readonly />\
                </div>\
              </div>\
            </div>\
          </div>\
        </div>\
      </div>\
    </div>\
    <div class="columns" v-if="isLoading">\
      <div class="column is-flex is-justify-content-center is-align-content-center">\
        <img class="mx-auto mt-6" alt="Carregando" src="../static/img/loading.svg" width="100" height="100" />\
      </div>\
    </div>\
  </div>\
',
  data: function () {
    return {
      profitInput: '',
      apiResult: [],
      loading: false
    }
  },
  computed: {
    showList: function () {
      return (this.apiResult.length > 0 && !this.isLoading)
    },
    isLoading() {
      return this.loading
    }
  },
  methods: {
    formatCurrency: function (value) {
      return new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(value)
    },
    searchProfit: async function () {
      this.loading = true
      this.apiResult = []
      // API MOCK
      const result = await axios.get(`/prices/${this.sku}/${this.goverment_taxes}/${this.profitInput}`)
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