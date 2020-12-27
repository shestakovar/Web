<template>
    <div class="container">
        <div class="user_data mt-5">
           <div class="user_data_title">
               Личные данные
           </div>
           <div class="avatar">
               <img src="@/assets/avatar.svg" alt="">
           </div>
           <div class="data col-6 align-center mt-4 ml-auto mr-auto">
               <table class="user_data_table table">
                <tbody>
                    <tr>
                    <td class="text-left">Имя пользователя:</td>
                    <td>{user_login}</td>
                    </tr>
                    <tr>
                    <td class="text-left">Фамилия:</td>
                    <td>{user_surname}</td>
                    </tr>
                    <tr>
                    <td class="text-left">Имя:</td>
                    <td>{user_name}</td>
                    </tr>
                    <tr>
                    <td class="text-left">Пол:</td>
                    <td>{user_gender}</td>
                    </tr>
                </tbody>
                </table>
           </div>
           <div class="col-12 mb-4">
                <button class="primary">Редактировать профиль</button>
           </div>
        </div>
        <div class="user_data mt-5">
            <div class="user_reciepts_title">
              Мои рецепты
            <div class="data col-7 ml-auto mr-auto">
                <table class="table table-striped">
                <thead>
                    <tr>
                    <th scope="col">Название блюда</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>{user_reciept/id}</td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/edit.svg" alt=""></a></td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/delete.svg" alt=""></a></td>
                    </tr>
                    <tr>
                    <td>{user_reciept/id}</td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/edit.svg" alt=""></a></td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/delete.svg" alt=""></a></td>
                    </tr>
                    <tr>
                    <td>{user_reciept/id}</td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/edit.svg" alt=""></a></td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/delete.svg" alt=""></a></td>
                    </tr>
                </tbody>
                </table>
              </div>
            </div>
            <div class="col-12 mb-4">
                <button class="primary">Добавить рецепт</button>
           </div>
        </div>
        <div class="user_data mt-5">
            <div class="user_reciepts_title">
              Мои вопросы
            <div class="data col-7 ml-auto mr-auto">
                <table class="table table-striped">
                <thead>
                    <tr>
                    <th scope="col">Заголовок вопроса</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>{user_question/id}</td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/edit.svg" alt=""></a></td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/delete.svg" alt=""></a></td>
                    </tr>
                    <tr>
                    <td>{user_question/id}</td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/edit.svg" alt=""></a></td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/delete.svg" alt=""></a></td>
                    </tr>
                    <tr>
                    <td>{user_question/id}</td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/edit.svg" alt=""></a></td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/delete.svg" alt=""></a></td>
                    </tr>
                </tbody>
                </table>
              </div>
            </div>
            <div class="col-12 mb-4">
                <button class="primary">Задать вопрос</button>
           </div>
        </div>
        <div class="user_data mt-5 mb-5">
        <div class="user_reciepts_title">
              Избранные рецепты
            <div class="data col-7 ml-auto mr-auto">
                <table class="table table-striped">
                <thead>
                    <tr>
                    <th scope="col">Заголовок вопроса</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>{user_fav/id}</td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/edit.svg" alt=""></a></td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/delete.svg" alt=""></a></td>
                    </tr>
                    <tr>
                    <td>{user_fav/id}</td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/edit.svg" alt=""></a></td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/delete.svg" alt=""></a></td>
                    </tr>
                    <tr>
                    <td>{user_fav/id}</td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/edit.svg" alt=""></a></td>
                    <td><a style="" href=""><img style="width: 25px;" src="@/assets/delete.svg" alt=""></a></td>
                    </tr>
                </tbody>
                </table>
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
    .user_data {
        border: 2px solid #6d6678;
    }
    .table{
        border: 5px solid #FFF3D8;
        border-radius: 5px;
        background-color: #FFF3D8;
    }
    button {
        height: 34px;
        width: 30%;
        border: 0px;
    }
    button.primary {
        border-radius: 5px;
        background-color: #6D6678;
        color: #ffffff;
    }
</style>