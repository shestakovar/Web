<template>
<header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <div class="collapse navbar-collapse">
                <router-link to="/"><img src="@/assets/logo.png" alt=""></router-link>
                <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                <router-link 
                    to="/"
                    tag="li"
                    active-class="active">
                    <li class="nav-item nav-link">
                        Главная
                    </li>
                </router-link>
                <router-link 
                    to="/dishes"
                    tag="li"
                    active-class="active">
                    <li class="nav-item nav-link">
                        Рецепты
                    </li>
                </router-link>
                <router-link 
                    to="/questions"
                    tag="li"
                    active-class="active">
                    <li class="nav-item nav-link">
                        Вопрос-ответ
                    </li>
                </router-link>
                </ul>
                <div class="form-inline my-2 my-lg-0">
                <router-link 
                    to="/user"
                    tag="li"
                    active-class="">
                <li class="btn btn-link" style="background-color: #75717C; color:white;">{User_name}</li>
                </router-link>
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
    color:rgb(201, 175, 207)
}
</style>