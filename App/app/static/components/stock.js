const STOCK = {
  template: '\
  <div class="container p-3">\
    <div class="columns">\
      <h1 class="column title is-12">Controle de Estoque</h1>\
    </div>\
    <div class="columns">\
      <div class="column is-full">\
        <input class="input is-medium" type="text" v-model="filter" placeholder="Filtro" />\
      </div>\
    </div>\
    <div class="columns mb-4" v-if="showList">\
      <div class="column is-12">\
        <table class="table">\
          <thead>\
            <tr>\
              <th><abbr title="Produto">Produto</abbr></th>\
              <th><abbr title="Caracteres">Carac.</abbr></th>\
              <th><abbr title="SKU">SKU</abbr></th>\
              <th><abbr title="Código de barras">Cód. Barras</abbr></th>\
              <th><abbr title="NCM">NCM</abbr></th>\
              <th><abbr title="Quantidade em Estoque">Estoque</abbr></th>\
              <th><abbr title="Valor do Estoque">Val. Estoque</abbr></th>\
              <th><abbr title="Custo médio Unitário">Custo Un.</abbr></th>\
              <th><abbr title="Preço de Venda">Val. Venda</abbr></th>\
              <th><abbr title="Marca">Marca</abbr></th>\
              <th><abbr title="Modelo">Mod.</abbr></th>\
              <th><abbr title="Lojas virtuais ativas">Lojas Ativas</abbr></th>\
              <th><abbr title="Unidades vendidas">Vendas</abbr></th>\
              <th><abbr title="Peso Bruto (Kg)">Peso</abbr></th>\
              <th><abbr title="Comprimento (cm)">Comp.</abbr></th>\
              <th><abbr title="Largura (cm)">Larg.</abbr></th>\
              <th><abbr title="Altura (cm)">Alt.</abbr></th>\
              </tr>\
          </thead>\
          <tbody>\
            <tr v-for="(product, index) in apiResult" :key="index">\
              <td>{{product.title}}</td>\
              <td>{{product.characters}}</td>\
              <td>{{product.sku}}</td>\
              <td>{{product.barcode}}</td>\
              <td>{{product.ncm}}</td>\
              <td>{{product.quantityInStock}}</td>\
              <td>{{product.stockValue | formatCurrency }}</td>\
              <td>{{product.averageUnityValue | formatCurrency }}</td>\
              <td>{{product.sellPrice | formatCurrency }}</td>\
              <td>{{product.brand}}</td>\
              <td>{{product.model}}</td>\
              <td>\
                <span v-for="(store, i) in product.activeEcommerces" :key="i">{{store}}, &nbsp;</span>\
              </td>\
              <td>{{product.unitiesSold}}</td>\
              <td>{{product.weight}}</td>\
              <td>{{product.height}}</td>\
              <td>{{product.width}}</td>\
              <td>{{product.depth}}</td>\
            </tr>\
          </tbody>\
        </table>\
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
      filter: '',
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
  filters: {
    formatCurrency: function (value) {
      return new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(value)
    },
  },
  methods: {
    getStock: async function () {
      this.loading = true
      this.apiResult = []
      const result = await axios.get(`/stock/`)
      this.apiResult = result.data
      this.loading = false
    }
  },
  mounted(){
    this.getStock()
  }
}
RUR(() => {
  new Vue({
    el: document.getElementById('app'),
    components: {
      'stock': STOCK,
    },
  })
});