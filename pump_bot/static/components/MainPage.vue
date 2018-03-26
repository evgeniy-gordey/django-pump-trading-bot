<template>
  <div class="main-page">
    <h1>Django Pump-trading bot 2</h1>
    <!-- <div>
      <label for="amount">Amount</label>
      <input type="number" v-model="amount">
    </div>
    <div>
      <label for="buyRate">Buy Rate</label>
      <input type="number" v-model="buyRate">
    </div>
    <div>
      <label for="sellRate">Sell Rate</label>
      <input type="number" v-model="sellRate">
    </div> -->
    <div>
      <label for="Currency">Currency</label>
      <input type="text" v-model="currency">
    </div>
    <button class="button" @click="buyCurrency">Buy currency</button>
    <h5 v-if="ticker">{{ ticker }}</h5>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MainPage',
  data() {
    return {
      amount: 10,
      buyRate: 0,
      sellRate: 0,
      currency: '',
      ticker: undefined
    }
  },
  methods: {
    async buyCurrency () {
      let res = await axios.post('/api/trade/', {
        amount: this.amount,
        buyRate: this.buyRate,
        sellRate: this.sellRate,
        currency: this.currency
      })
      this.ticker = res.data
    }
  }
}
</script>

<style lang="sass" scoped>
  
h1 
  text-align: center
  
.main-page
  display: flex
  flex-direction: column
  align-items: center
  
</style>
