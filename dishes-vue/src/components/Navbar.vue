<template>
<header>
    <nav class="navbar navbar-expand-lg">
    <div class="container">
        <router-link to="/" class="navbar-brand"><img src="@/assets/logo.png" alt=""></router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
            <router-link to="/" class="nav-item nav-link">Главная<span class="sr-only">(current)</span></router-link>
            <a class="nav-item nav-link">Рецепты</a>
            <a class="nav-item nav-link">Вопрос-ответ</a>
            </div>
        </div>
    </div>

    </nav>
</header>
</template>

<script>
export default {

}
</script>

<style>
.navbar {
    background-color: #361D62;
}
nav-link :active {
    color: white;
}
</style>