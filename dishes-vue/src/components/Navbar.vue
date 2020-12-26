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
            <router-link to="/" class="nav nav-link">Главная<span class="sr-only">(current)</span></router-link>
            <router-link to="/dishes" class="nav nav-link">Рецепты<span class="sr-only">(current)</span></router-link>
            <router-link to="/" class="nav nav-link">Вопрос-ответ<span class="sr-only">(current)</span></router-link>
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

.nav {
    color: ghostwhite;
}
.nav:hover {
    color:rgb(138, 109, 145)
}
</style>