<template>
<div v-if="dishes && dishes.length > 0" class="mt-5 recipes_new">
  <router-link :to="{ name: 'Dish', params: { id: dishes[0].id }}" style="text-decoration: none;">
      <div class="mb-3 container" style="border: 1px solid black">
        <div class="row" style="background-color: #FFF3D8;">
          <div class="col-4 embed-responsive embed-responsive-4by3">
            <img class="p-3 embed-responsive-item" :src="dishes[0].img" alt="">
          </div>
          <div class="recipes_new_title col-8">
            {{dishes[0].name}}
            <p class="card-text">
              Хачапури по-аджарски сразу из печи - ароматные, с растопленным сыром сулу- гуни и нежным хрустящим краешком. Отломите кусочек, окуните его в сыр, сдобренный маслом и куриным яйцом, а потом попробуйте отказаться от следующего кусочка. Поверьте, это сделать невозможно.
            </p>
          </div>
        </div>
      </div>
  </router-link>
  <div class="recipes_new_title">
    <span><img style="transform: scale(0.7,0.7)" src="@/assets/decor_1.png" alt=""></span>
    <span>Новые рецепты</span>
    <span><img style="transform: scale(-0.7,0.7)" src="@/assets/decor_1.png" alt=""></span>
  </div>
  <div class="container mt-4">
    <div class="row">
      <router-link v-for="(post, index) of dishes" :key="index" :to="{ name: 'Dish', params: { id: post.id }}" class="pulse col-4 embed-responsive embed-responsive-4by3">
        <img :src="post.img" alt="" class="embed-responsive-item p-3">
      </router-link>
    </div>
    <router-link to='/dishes'><button class="mb-5 mt-4 all_dishes">Показать все рецепты</button></router-link>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  components: {
  },
  data: () => ({
    dishes: []
  }),

  created() {
  axios.get("http://localhost/api/v1/dishes/")
  .then(response => {
    this.dishes = response.data
  })
}
}
</script>

<style>
  button {
    height: 34px;
    width: 30%;
    border: 0px;
  }
  button.all_dishes {
    border-radius: 5px;
    background-color: #6D6678;
    color: #ffffff;
    text-transform: uppercase;
  }
  @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
  .recipes_new_title {
    font-family: Roboto;
    font-size: 42px;
    font-weight: 400;
    line-height: 68px;
    letter-spacing: 0px;
    text-align: center;
    color: #361D62;
  }
  .card-text {
    font-family: Roboto;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: 29px;
    letter-spacing: 0em;
    text-align: left;
  }
  img {
    object-fit: cover;
  }

  .pulse:hover {
    -webkit-animation-name: pulse;
    animation-name: pulse;
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-fill-mode: both;
    animation-fill-mode: both;
  }
  @-webkit-keyframes pulse {
  0% {
  -webkit-transform: scale3d(1, 1, 1);
  transform: scale3d(1, 1, 1);
  }
  50% {
  -webkit-transform: scale3d(1.05, 1.05, 1.05);
  transform: scale3d(1.05, 1.05, 1.05);
  }
  100% {
  -webkit-transform: scale3d(1, 1, 1);
  transform: scale3d(1, 1, 1);
  }
  }
  @keyframes pulse {
  0% {
  -webkit-transform: scale3d(1, 1, 1);
  transform: scale3d(1, 1, 1);
  }
  50% {
  -webkit-transform: scale3d(1.05, 1.05, 1.05);
  transform: scale3d(1.05, 1.05, 1.05);
  }
  100% {
  -webkit-transform: scale3d(1, 1, 1);
  transform: scale3d(1, 1, 1);
  }
  } 

</style>
