<template>
<div>
  <div class="container mt-5">
    <div class="finder">
      <div class="row">
        <div class="col-8">
          <div class="filter_types m-4">
            <div class="text-left ml-2">Типы блюд:</div>
            <span class="mr-5"
              ><input type="checkbox" name="types" value="first_dish" /> Первые
              блюда</span
            >
            <span class="mr-5"
              ><input type="checkbox" name="types" value="second_dish" /> Вторые
              блюда</span
            >
            <span class="mr-5"
              ><input type="checkbox" name="types" value="snacks" />
              Закуски</span
            >
            <span class="mr-5"
              ><input type="checkbox" name="types" value="bakery" />
              Выпечка</span
            >
            <br />
            <span class="mr-4"
              ><input type="checkbox" name="types" value="preparation" />
              Заготовки</span
            >
            <span class="mr-4"
              ><input type="checkbox" name="types" value="sauces" /> Соусы</span
            >
            <span class="mr-4"
              ><input type="checkbox" name="types" value="drinks" />
              Напитки</span
            >
            <span class="mr-4"
              ><input type="checkbox" name="types" value="seasonings" />
              Приправы</span
            >
            <span class="mr-4"
              ><input type="checkbox" name="types" value="sweet" />
              Сладости</span
            >
          </div>
          <div class="filter_ingredients m-4">
            <div class="text-left ml-2">Поиск по ингредиентам:</div>
            <div class="mt-2">
              <span>
                <select name="ingr_1" class="ingr mr-4">
                  <option selected="selected" disabled>Ингредиент №1</option>
                  <option v-for="(post, index) of ingredients" :key="index" :value="post.id">{{post.name}}</option>
                </select>
              </span>
              <span>
                <input
                  class="num mr-4"
                  type="text"
                  name=""
                  id=""
                  placeholder="Количество"
                />
              </span>
              <span>
                <select name="unit" class="ingr">
                  <option selected="selected" disabled>Ед. измерения</option>
                  <option value="1">Ст. ложчка</option>
                  <option value="2">Ч. ложка</option>
                  <option value="3">Стакан</option>
                  <option value="4">Г.</option>
                  <option value="5">Кг.</option>
                  <option value="6">Шт.</option>
                </select>
              </span>
            </div>
            <div class="mt-2">
              <span>
                <select name="ingr_1" class="ingr mr-4">
                  <option selected="selected" disabled>Ингредиент №2</option>
                  <option v-for="(post, index) of ingredients" :key="index" :value="post.id">{{post.name}}</option>
                </select>
              </span>
              <span>
                <input
                  class="num mr-4"
                  type="text"
                  name=""
                  id=""
                  placeholder="Количество"
                />
              </span>
              <span>
                <select name="unit" class="ingr">
                  <option selected="selected" disabled>Ед. измерения</option>
                  <option value="1">Ст. ложчка</option>
                  <option value="2">Ч. ложка</option>
                  <option value="3">Стакан</option>
                  <option value="4">Г.</option>
                  <option value="5">Кг.</option>
                  <option value="6">Шт.</option>
                </select>
              </span>
            </div>
            <div class="mt-2">
              <span>
                <select name="ingr_1" class="ingr mr-4">
                  <option selected="selected" disabled>Ингредиент №3</option>
                  <option v-for="(post, index) of ingredients" :key="index" :value="post.id">{{post.name}}</option>
                </select>
              </span>
              <span>
                <input
                  class="num mr-4"
                  type="text"
                  name=""
                  id=""
                  placeholder="Количество"
                />
              </span>
              <span>
                <select name="unit" class="ingr">
                  <option selected="selected" disabled>Ед. измерения</option>
                  <option value="1">Ст. ложчка</option>
                  <option value="2">Ч. ложка</option>
                  <option value="3">Стакан</option>
                  <option value="4">Г.</option>
                  <option value="5">Кг.</option>
                  <option value="6">Шт.</option>
                </select>
              </span>
            </div>
            <div class="mt-2 mb-2">
              <button class="registration" style="width: 63%">
                Добавить ингредиент
              </button>
            </div>
          </div>
        </div>
        <div class="col-4 mt-4 mb-4" style="border-left: 2px solid #6D6678">
          <div class="sort">
            <div class="text-left">Сортировать по:</div>
            <div class="text-left ml-4">
              <input class="mt-3" type="radio" name="sort" value="abc" />
              Алфавиту<br />
              <input class="mt-3" type="radio" name="sort" value="likes" />
              Популярности<br />
              <input class="mt-3" type="radio" name="sort" value="comments" />
              Обсуждаемости<br />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-for="(post, index) of dishes" :key="index" class="mt-5 container" style="border: 1px solid black">
    <router-link :to="{ name: 'Dish', params: { id: post.id }}">
    <div class="row" style="background-color: #FFF3D8;">
      <div class="col-4">
        <img class="p-3" :src="post.img" alt="" />
      </div>
      <div class="recipes_new_title col-8">
        {{post.name}}
        <p class="card-text">
          Хачапури по-аджарски сразу из печи - ароматные, с растопленным сыром
          сулу- гуни и нежным хрустящим краешком. Отломите кусочек, окуните его
          в сыр, сдобренный маслом и куриным яйцом, а потом попробуйте
          отказаться от следующего кусочка. Поверьте, это сделать невозможно.
        </p>
      </div>
    </div>
    </router-link>

  </div>
  </div>
</template>

<style>
.finder {
  border-radius: 15px;
  background-color: #fff3d8;
}
.filter_types {
  border: 2px solid #6d6678;
}
.filter_ingredients {
  border: 2px solid #6d6678;
}
.ingr {
  height: 34px;
  border-radius: 5px;
  border: 0px solid #6d6678;
  color: #6d6678;
}
.num {
  height: 34px;
  border-radius: 5px;
  border: 0px solid #6d6678;
  width: 100px;
  color: #6d6678;
}

button {
  height: 34px;
  width: 30%;
  border: 0px;
}
button.login {
  border-radius: 5px;
  background-color: #6d6678;
  color: #ffffff;
}

button.registration {
  border: 2px solid #6d6678;
  color: #6d6678;
  border-radius: 5px;
  background: none;
  text-transform: uppercase;
  font-size: 20px;
}
a:hover {
  text-decoration: none;
}
img {
  max-width: 100%;
}
</style>

<script>
import axios from 'axios'

export default {
  data: () => ({
    dishes: [],
    ingredients: []
  }),

created() {
  axios.get("http://localhost/api/v1/dishes/")
  .then(response => {
    this.dishes = response.data
    console.log(this.dishes)
  })
  axios.get("http://localhost/api/v1/ingredients/")
  .then(response => {
    this.ingredients = response.data
    console.log(this.dishes)
  })
}
}
</script>