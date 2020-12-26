<template>
  <div class="mt-5 container">
    <div class="dish_title row">
      <div class="title_text text-left col-10">Хачапури по-аджарски</div>
      <div class="title_img text-right col-2">
        <a href="#"><img src="@/assets/fav.svg" alt=""></a>
      </div>
    </div>
  </div>
  <div class="container mt-5">
    <div class="row mb-5">
      <div class="col-7">
        <img src="@/assets/dish1.png" alt="">
      </div>
      <div class="ingredients col-5">
        <ul class="list-group">
          <li class="ingredients_title list-group-item align-items-center">
            Ингредиенты
          </li>
          <li class="ingredients_a list-group-item d-flex justify-content-between align-items-center">
            Молоко (теплое)
            <span class="">125 мл</span>
          </li>
          <li class="ingredients_b list-group-item d-flex justify-content-between align-items-center">
            Вода (теплая)
            <span class="">125 мл</span>
          </li>
          <li class="ingredients_a list-group-item d-flex justify-content-between align-items-center">
            Яйца (куриные)
            <span class="">1 шт</span>
          </li>
          <li class="ingredients_b list-group-item d-flex justify-content-between align-items-center">
            Масло растительное
            <span class="">2 ст.л</span>
          </li>
          <li class="ingredients_a list-group-item d-flex justify-content-between align-items-center">
            Мука
            <span class="">400 г</span>
          </li>
          
          
        </ul>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="stage_title mb-4">
      <h3>Этапы приготовления</h3>
    </div>
    sadas
  </div>
</template>

<script>
export default {

}
</script>

<style>
  .dish_title {
    background-color: #534B60;
    height: 75px;
  }
  .title_text {
    color: ghostwhite;
    font-family: Roboto;
    font-size: 42px;
    font-style: normal;
    font-weight: 400;
    line-height: 68px;
    letter-spacing: 0px;
    text-align: center;
  }
  .title_img {
    margin-top: 12px;
  }
  .ingredients_title {
    background-color: #75717C;
    color: #fff;
  }
  .ingredients_b {
    background-color: #75717C;
    color: #fff; 
  }
  .ingredients_a {
    background-color: #534B60;
    color: #fff; 
  }
  
</style>