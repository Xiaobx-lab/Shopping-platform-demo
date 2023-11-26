<template>
<div>
    <div class="row" style="background: #F5F5F5;">
        <ul class="nav" >
            <li class="nav-item">
                <a class="nav-link active" style="color: #FD3F31" >首页</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#" style="color: #FD3F31">会员中心</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#" style="color: #FD3F31">联系客服</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#" style="color: #FD3F31">我的淘宝</a>
            </li>
        </ul>
        <div style="padding-left:750px">
            <ul class="nav justify-content-end">
                <li class="nav-item">
                    <a class="nav-link active" href="#"><router-link style="color: #FD3F31" :to="'/register'"> 免费注册</router-link></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" ><router-link style="color: #FD3F31" :to="'/login'">请登录</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" style="color: #FD3F31" @click="quitUser" >退出</a>
                </li>
            </ul>       
        </div>


    </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
    props:{
        top1_href:{
            required:false,
            type:String,
            default:''
      }
    },
    methods: {
        quitUser(){
            axios.get('/user/session-data-clear')
            .then(response => {
                const sessionData = response.data.del_flag;
                console.log(sessionData);
            })
            .catch(error => {
                console.error(error);
                // 处理请求错误
            });
        }
    },
}
</script>

<style>
.row{
    margin-left: 0px;
    padding: 5px;
}
.nav{
    font-size: smaller;
}
</style>