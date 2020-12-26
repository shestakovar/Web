<template>
    <div class="container">
        <div class="mt-5 login_title">Регистрация</div>
        <div class="mt-1"><img src="../assets/avatar.svg" alt=""></div>
        <div class="mt-3">
            <input class="field" type="text" placeholder="Имя пользователя">
        </div>
        <div class="mt-2">
          <div class="container">
            <span class="col-4">Пол:</span>
            <span class="col-4"><input class="rbut" name="gender" type="radio" value="male"> Мужской</span>
            <span class="col-4"><input clas="rbut" name="gender" type="radio" value="female"> Женский</span>
          </div>
        </div>
        <div class="mt-2">
            <input class="field" type="text" placeholder="Фамилия">
        </div>
        <div class="mt-2">
            <input class="field" type="text" placeholder="Имя">
        </div>
        <div class="mt-3">
            <input class="field" type="password" placeholder="Пароль">
        </div>
        <div class="mt-2">
            <input class="field" type="password" placeholder="Повторите пароль">
        </div>

        <div class="mt-3">
            <router-link to='/'><button class="login">Зарегистрироваться</button></router-link>
        </div>
        <div class="mt-2">
            <router-link to='/login'><button class="registration">Уже зарегистрированы?</button></router-link>
        </div>
    </div>
</template>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
  .login_title {
    font-family: Roboto, sans-serif;
    font-size: 68px;
    font-style: normal;
    font-weight: 200;
    line-height: 110px;
    letter-spacing: 4px;
    text-align: center;
    text-transform: uppercase;
    color: black;
  }
  input {
    border: 2px;
    border-radius: 5px;
    text-align: center;
    font-family: Roboto;
    font-style: normal;
    font-weight: 300;
    font-size: 21px;
    line-height: 34px;
  }
  input.field {
    width: 30%;
    height: 34px;
  }
  rbut {
    height: 24px;
    background-color: #6D6678;
  }
  button {
    height: 34px;
    width: 30%;
    border: 0px;
  }
  button.login {
    border-radius: 5px;
    background-color: #6D6678;
    color: #ffffff;
  }

  button.registration {
    border: 2px solid #6D6678;
    color: #6D6678;
    border-radius: 5px;
    background: none;
  }

  a.forgot_pass {
    color: #898989;
  }
</style>
