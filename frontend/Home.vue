<template>
  <div class="home">
  
    <div class="cont">
      <draggable :list="items" group="pp"
                animation="150"
                class="cont2">
        <div v-for="item in items" 
            :key="item.i" :id="'id'+String(item.i)" 
            class="drag-me">
          <p>
            {{item.name}}
          </p>   
        </div>
      </draggable>
      <draggable :list="answers" class="cont2" group="pp"
        id="board_2">  
        <div v-for="item in answers" 
            :key="item.i" :id="'id'+String(item.i)" 
            class="drag-me">
          <p>
            {{item.name}}
          </p>   
        </div>
      </draggable>
    </div>

    <div class="add">
      <div v-for="(plus, i) in pluses" :key="plus">
        <button @click="delete_item(i)">-</button>
        <input type="text" :value="plus.i_content">
      </div>
      <div class="new_item">
        
        <b-input-group class="new_input">
          <b-input-group-prepend>
            <b-button variant="outline-info" @click="add_item">new item</b-button>
          </b-input-group-prepend>
          <b-form-input v-model="i_content" type="text"></b-form-input>
          <b-input-group-append>
            <!-- modal 1 -->
            <b-button id="ing" v-if="look_forW(i_content)" v-b-modal.modal-1>variant1</b-button>
            <b-modal id="modal-1" :title="i_content">
              <b-list-group>
                <b-list-group-item v-for="cheese in cheeses" :key="cheese">
                  <div class="cheese">
                    <b-button @click="choose_ing(cheese.name)">{{cheese.name}}</b-button>
                  </div>
                </b-list-group-item>
              </b-list-group>
            </b-modal>
            <!-- modal 2 -->
            <b-button id="ing" v-if="look_forW(i_content)" v-b-modal.modal-1>variant1</b-button>
            <b-modal id="modal-1" :title="i_content">
              <b-list-group>
                <b-list-group-item v-for="cheese in cheeses" :key="cheese">
                  <div class="cheese">
                    <b-button @click="choose_ing(cheese.name)">{{cheese.name}}</b-button>
                  </div>
                </b-list-group-item>
              </b-list-group>
            </b-modal>
          </b-input-group-append>
        </b-input-group>
        
        
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import draggable from 'vuedraggable'
import axios from 'axios'

export default {
  name: 'Home',
  components: {
    draggable,
    // HelloWorld
  },
  data : () =>({
    ing : '',
    i_content : "",
    pluses : [],
    items : [
      {'name': 'amine1', 'i' : 1},
      {'name': 'amine2', 'i' : 2},
      {'name': 'amine3', 'i' : 3},
      {'name': 'amine4', 'i' : 4},
      {'name': 'amine5', 'i' : 5},
    ],
    cheeses : [
      {'name': 'cheese1', 'i' : 1},
      {'name': 'cheese2', 'i' : 2},
      {'name': 'cheese3', 'i' : 3},
      {'name': 'cheese4', 'i' : 4},
      {'name': 'cheese5', 'i' : 5},
    ],
    answers : [],
  }),

  methods: {
    add_item(){
      this.pluses.push({'i_content' : this.i_content})
    },
    delete_item(i){
      this.pluses.splice(i, 1)
      console.log(this.pluses)
    },
    look_forW(i_content){
      if (i_content == 'cheese') {
        return true;
      }
      return false;
    },
    choose_ing(item) {
      this.i_content = item
    }
  },

  mounted () {
    console.log(this.api_url)
    axios.get(this.api_url+'ings', {})
        .then((res) =>{
          console.log(res.data)
            this.cheeses = res.data
        })
        .catch((err) =>{
            console.log("amineeeeee",err)
        })
  },

  
  computed : {

      api_url() {
          return this.$store.state.api_url;
      }
  }
  
}
</script>

<style scoped>

.cont{
  background : pink;
  height : 50vh;
  width : 60%;
  display : grid;
  grid-template-columns : 1fr 1fr;
  }

.cont2 {
  height : 200px;;
  background : grey;
  margin : 2px;
  padding : 2px;
  display : flex;
  flex-direction : column;
  align-items : center;
  }

.drag-me{
  display : flex;
  justify-content : center;
  padding : 2px;
  margin : 2px;
  width : 50%;
  background : yellow;
  cursor : pointer;
}


.new_item {
  display : flex;
  flex-direction : row;
}

.cheese {
  display : flex;
  flex-direction : row;
}

.new_input {
  width : 30%;


}
</style>
