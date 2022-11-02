<template>
  <div>
    <el-button @click="onCreateGame"> Create game </el-button>
    <p>Game: {{ gameUuid }}</p>
    <div class="players">
      <div class="player-card" v-for="player in countPlayers" :key="player">
        <p class="player-card-name"> Player {{ player }} </p>
        <div class="button-wrapper">
          <el-button class="player-get-cards-button" @click="getPlayerCard(player)"> Get cards </el-button>
        </div>
        <div v-for="(cards, player_id) in playersCards" :key="player_id">
          <div v-for="(card, id) in cards" :key="id">
            <div class="player-card-text">
              <p> ID : {{ card.id }} </p>
              <p> Name : {{ card.name }} </p>
              <p> Color : {{ card.color }} </p>
            </div>
          </div>
        </div>
      </div>
      <div class="dealer-card">
        <p class="player-card-name"> Dialer </p>
        <div class="button-wrapper">
          <el-button class="player-get-cards-button" @click="getDealerCard()"> Get cards </el-button>
        </div>
        <div class="dealer-card-page" v-for="(card, id) in dealerCards" :key="id">
          <div class="dealer-card-text">
            <p> ID : {{ card.id }} </p>
            <p> Name : {{ card.name }} </p>
            <p> Color : {{ card.color }} </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data() {
    return {
      gameUuid: '',
      cardsId: [],
      playersCards: [],
      dealerCards: [],
      countPlayers: 4,
    }
  },
  methods: {
    async onCreateGame() {
      const {data} = await this.axios.get('/api/create-game')
      this.gameUuid = data.uuid
    },
    async getPlayerCard(player_id) {
      console.log(player_id)
      const {data} = await this.axios.get(`/api/get-card?uuid=${this.gameUuid}`)
      const playerCard = {
        'player_id': player_id,
      }
      this.playersCards.push(data)
    },
    async getDealerCard() {
      const {data} = await this.axios.get(`/api/get-card?uuid=${this.gameUuid}`)
      this.dealerCards.push(data)
    }
  },
}
</script>

<style>
  .players {
    position: absolute;
    width: 100%;
    margin: 1%;
  }
  .player-card {
    display: inline-block;
    border: 1px solid cadetblue;
    border-radius: 5px;
    margin: 2px;
    min-width: 24%;
    min-height: 400px;
  }
  .player-card-name {
    text-align: center;
  }
  .button-wrapper {
    text-align: center;
  }
  .player-card-text {
    text-align: left;
    margin-left: 10px;
    border-bottom: 1px solid black;
  }

  .dealer-card {
    border: 1px solid cadetblue;
    border-radius: 5px;
    margin: 2px;
    width: 100%;
    min-height: 400px;
  }
  .dealer-card-page {
    display: inline-block;
    height: 100%;
    width: 15%;
    border: 1px solid cadetblue;
    border-radius: 5px;
    margin: 10px;
  }
  .dealer-card-text {
    text-align: center;
  }
</style>
