<template>
<div class="container">
    <div class="info mt-3 p-2">
        <p>Вопросы и ответы по кулинарии и домашнему хозяйству.</p>
        <p>Задать вопрос или найти ответ по интересующей теме. Ответить, посоветовать, дать свою рекомендацию, или узнать мнение большинства. Здесь вы можете задать вопрос пользователям сайта, а также поделиться своим опытом, отвечая на вопросы других.</p>
   </div>
   <div class="mt-3">
            <router-link to='#'><button class="login">Задать вопрос</button></router-link>
   </div>
   <div class="questions mt-5">
       <div class="row" style="border: 2px solid #6D6678;">
            <div class="col-4 p-2" style="border-right:2px solid #6D6678;">
                <img src="@/assets/avatar.svg" alt="">
                <div class="mt-2">{User.surname} {User.name}</div>
            </div>
            <div class="col-8">
                <div class="question_title">
                    <h2>{User.question.title}</h2>
                </div>
                <div class="question_text text-left">
                    Здравствуйте, дорогие пользователи сайта! Хотел приготовить макароны, уже купил их, но столкнулся с проблемой - не знаю, как долго нужно варить эти макароны. Бренд макарон - barilla. На коробке написано 8 минут, но не знаю насколько можно доверять производителю. Заранее спасибо!
                </div>
                <div class="text-right">
                    {user.question.date}
                </div>
            </div>
       </div>
   </div>
</div>
</template>

<script>
export default {

}
</script>

<style>
    .info {
        background-color: #FFF3D8;
        border-radius: 5px;
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
    .question {
        border: 2px, solid,;
    }
</style>