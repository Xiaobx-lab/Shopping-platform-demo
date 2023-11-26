<template>
  <div>
    <div class="lo">
    <div class="top">
        <div class="top-a">
            <a href="#" ><img src="../assets/logo2.png" width="130px"></a>
        </div>
    </div>
    <div class="login">
        <div class="background"></div>
        <div class="login-layout">
            <div class="login-box-warp">
                <div class="login-box">
                    <div style="margin-bottom: 0px;width: 100%">
                        <div class="login-content">
                            <div class="login-content-top">
                                <a class="login-content-a">密码登录</a>
                                <a class="login-content-a">短信登录</a>
                            </div>
                            <div class="login-content-form">
                                <el-form  ref="form" :model="user">
                                    <input class="input" type="text" v-model="user.username" autocomplete="off" placeholder="请输入您的账号">
                                    <input class="input" type="password" v-model="user.password"  autocomplete="off" placeholder="请输入登录密码" style="margin-top: 20px">
                                   <input class="dl" type="submit" value="登录" @click = "onSubmit" style="margin-left: 20px">
                                </el-form>
                            </div>
                            <div style="margin-top: 20px;margin-left: 150px">
                                <a href="#" ><router-link :to="'/register'" style="color: gray;text-decoration: none;"> 我要注册</router-link></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            user:{
                username:'',
                password:''
            }
        }
    },
    methods: {
        onSubmit(){
            axios.post('/user/login/', {
                username: this.user.username,
                password: this.user.password
            }).then(response => {
                //如果登陆成功，获取token值，否则重新输入
                console.log('登陆成功，返回的数据',response.data)
                const flag = response.data.login_flag
                if (flag == "True") {
                    // 存储Token，例如使用localStorage
                    localStorage.setItem('token', response.data.token.access);
                    // 设置Axios的全局默认请求头
                        axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`;
                        console.log(axios.defaults.headers.common['Authorization'])
                        // 发送受保护的API请求
                        axios.get('/user/testProtected/')
                        .then(response => {
                            // 处理受保护API请求的响应数据
                            console.log(response.data)
                        })
                        .catch(error => {
                            // 处理受保护API请求失败的情况
                            console.log(error)
                        });
                }else{
                    alert("用户名或密码错误，请重新输入")
                }
            })
        },


    },
}
</script>

<style>
    .lo{
        margin: 0;
        margin-left: -8px;
        margin-right: -8px;
        padding: 0;
    }
    .top{
        padding: 20px 0;
        height: 44px;
    }
    .top-a{
        width: 1200px;
        margin: 0 auto;
        overflow: hidden;
    }
    .login{
        width: 100%;
        position: relative;
    }
    .background{
        background-image: url("../assets/login_background.jpg");
        position: absolute;
        z-index: 1;
        top: 0;
        left: 0;
        background-size: cover;
        background-repeat: no-repeat;
        background-position: 50%;
        width: 100%;
        height: 600px;
    }
    .login-layout{
        width: 1200px;
        margin: 40px;
        overflow: hidden;
        position: relative;
        height: 600px;
        z-index: 2;
    }
    .login-box-warp{
        position: absolute;
        top: 120px;
        right: 60px;
        width: 350px;
    }
    .login-box{
        min-height: 300px;
        padding: 25px 25px 23px;
        color: #6c6c6c;
        background: #fff;
        background-color: rgb(255, 255, 255);
        position: relative;
        margin: 0 auto;
    }
    .login-box-warp .login-box{
        background-color: hsla(0,0%,100%,0.7);
        position: relative;
    }
    .login-content{
        width: 100%;
        margin: 0 auto;
        padding-top: 2px;
    }
    .login-content-top{
        text-align: left;
        margin-bottom: 20px;
        margin-top: 4px;
    }
    .login-content-a{
        height: 18px;
        line-height: 5px;
        font-size: 16px;
        color: #3c3c3c;
        margin: 9px 10px 0 0;
        font-weight: 700;
    }
    .input{
        color: gray;
        width: 295px;
        height: 42px;
        padding-left: 10px;
        border: none;
    }
    .dl{
        background: #f40;
        width: 300px;
        height: 42px;
        padding-left: 10px;
        margin-top: 20px;
        border: none;
        color: white;
        font-size: 20px;
        ;
    }
</style>