<template>
  <div>
<div class="register">
    <div class="header">
        <a href="#"><img src="../assets/logo2.png"  width="130px"/></a>
        <h2 style="margin-top:20px">用户注册</h2>
    </div>
    <div style="margin-top: 55px;">
        <div class="content">
        <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm" method="POST">
            <el-form-item label="用户名" prop="username">
                <el-input type="text" v-model="ruleForm.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass">
                <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPass">
                <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="验证码" prop="verify">
                <el-input type="text" v-model="ruleForm.verify" autocomplete="off"></el-input>
                <img src="/user/loadCode/" alt="" style="width: 40%">
            </el-form-item>
            <el-form-item>
                <el-button style="background-image: linear-gradient(90deg,#f90,#ff5000);color: white;font-size: 15px;" @click="submitForm('ruleForm')">提交</el-button>
                <el-button style="background-image: linear-gradient(90deg,#f90,#ff5000);color: white;font-size: 15px;" @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
        </el-form>

        </div>

        <div >
            <input id="cb" class="c" type="checkbox"/>
            <span class="text">已阅读并同意以下协议淘宝平台服务协议、隐私权政策、法律声明、支付宝及客户端服务协议</span> 
        </div>
       
        <hr style="border-top: 0px;border-left: 0px;border-right: 0px;color: #D6D6D6">
        <div style="color: gray; " class="a">
            <a href="#" class="a"> 阿里巴巴集团&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 阿里巴巴国际站&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 阿里巴巴中国站&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 全球速卖通&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 淘宝网&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 天猫&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 聚划算&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 阿里巴巴妈妈&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 阿里云计算&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 云OS&nbsp;&nbsp;|&nbsp;</a>
            <a href="#" class="a"> 支付宝&nbsp;&nbsp;|&nbsp;</a>
            <hr style="border-top: 0px;border-left: 0px;border-right: 0px;color: #D6D6D6">
            <a href="#" class="a"> 关于淘宝&nbsp;&nbsp;&nbsp;</a>
            <a href="#" class="a"> 合作伙伴&nbsp;&nbsp;&nbsp;</a>
            <a href="#" class="a"> 营销中心&nbsp;&nbsp;&nbsp;</a>
            <a href="#" class="a"> 联系客服&nbsp;&nbsp;&nbsp;</a>
            <a href="#" class="a"> 开放平台&nbsp;&nbsp;&nbsp;</a>
            <a href="#" class="a"> 诚征英才&nbsp;&nbsp;&nbsp;</a>
            <a href="#" class="a"> 联系我们&nbsp;&nbsp;&nbsp;</a>
            <a href="#" class="a"> 网站地图&nbsp;&nbsp;&nbsp;</a>
            <a href="#" class="a"> 法律声明及隐私&nbsp;&nbsp;&nbsp;</a>
        </div>
    </div>

</div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.ruleForm.checkPass !== '') {
            this.$refs.ruleForm.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      return {
        ruleForm: {
            username:'',
            pass: '',
            checkPass: '',
            verify:'',
        },
        code:'',
        flag: false,
        rules: {
          username: [
            { required: true, message:'请输入用户名',trigger:'blur'},
            { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
          ],
          pass: [
            { required: true, message:'请输入密码',trigger:'blur'},
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ],
          verify: [
            {required: true, message:'请输入验证码',trigger:'blur' }
          ]
        }
      };
    },
    methods: {
      // async submitForm(formName){
      //   await this.$refs[formName].validate(async (valid) => {
      //     if (valid) {
      //       await this.getCode();
      //       console.log(this.code);
      //       if (this.code != this.ruleForm.verify) {
      //         alert("验证码不正确，请重新输入")
      //       }else{
      //       //表单提交，向后台发送数据
      //         axios.post('/user/register/', {
      //             username: this.ruleForm.username,
      //             password: this.ruleForm.pass
      //         }).then(response => {
      //             this.flag = response.data.flag
      //             if (this.flag) {
      //                 alert("恭喜您，注册成功！")
      //                 this.$router.push('/');
      //                 this.getSessionData()
      //             }else{
      //                 alert("用户名已经存在，请重新尝试！")
      //             }
      //         }).catch(error => {
      //             console.error(error);
      //         });
      //       }
        
      //     } else {
      //           console.log('error submit!!');
      //           return false;
      //       }
      //   });
      // },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.getCode(() => {
            console.log(this.code);
            if (this.code != this.ruleForm.verify) {
              alert("验证码不正确，请重新输入");
            } else {
              // 表单提交，向后台发送数据
              axios
                .post("/user/register/", {
                  username: this.ruleForm.username,
                  password: this.ruleForm.pass,
                })
                .then((response) => {
                  this.flag = response.data.flag;
                  if (this.flag) {
                    alert("恭喜您，注册成功！");
                    // this.$router.push("/");
                    this.getSessionData();
                  } else {
                    alert("用户名已经存在，请重新尝试！");
                  }
                })
                .catch((error) => {
                  console.error(error);
                });
            }
          });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },

      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      // 获取session数据
      getSessionData(){
        axios.get('/user/session-data')
        .then(response => {
            const sessionData = response.data.user;
            console.log(sessionData);
        })
        .catch(error => {
            console.error(error);
            // 处理请求错误
        });
      },
      // getCode(){
      //   axios.get('/user/checkCode/')
      //   .then(response => {
      //     const code = response.data.code;
      //       // console.log('code',typeof code)
      //       this.code =code
      //   })
      //   .catch(error => {
      //       console.error(error);
      //       // 处理请求错误
      //   });

      // }
      getCode(callback) {
        axios.get("/user/checkCode/")
          .then((response) => {
            this.code = response.data.code;
            if (typeof callback === "function") {
              callback();
            }
          })
          .catch((error) => {
            console.error(error);
          });
      }
    }
  }

</script>

<style type="text/css">
    .register{
        width: 990px;
        margin: 0 auto;
        color: #3c3c3c;
        font: 400 12px/1.6 arial,'Hiragino Sans GB',宋体,sans-serif;
    }
    .header{
        position: relative;
        height: 43px;
        padding: 20px 0;
    }
    .header h2{
        display: inline-block;
        zoom: 1;
        *display: inline;
        height: 43px;
        line-height: 10px;
        font-size: 22px;
        font-family: "\5FAE\8F6F\96C5\9ED1","\534E\6587\7EC6\9ED1","\9ED1\4F53",arial;
        font-weight: 400;
        vertical-align: middle;
    }
    .content{
        width: 600px;
        margin: 0 auto;
        margin-top: 30px;
        position: relative;
        text-align: center;
        margin-top: 30px;
    }
    .content input{
        /* margin-top: 20px; */
        padding-left: 10px;
        padding-right: 10px;
        margin-top: 10px;
        height: 34px;
        width: 250px;
        min-height: 34px;
        border: 1px solid #d6d6d6;
        border-radius: 3px;
        margin-left: 70px;
    }
    .content lable{
        position: absolute;
        height: 36px;
        line-height: 36px;
        color: #3C3C3C;
        font-size: 16px;
        width: 120px;
        overflow: hidden;
        left: 60px;
        text-align: right;
        margin-top: 12px;
    }

    #span{
        margin-left: 0px;
        color: gainsboro;
        background-color: #f40;
        margin-left: 480px;
        font-size: 25px;
    }

    .c{
        
        margin-top: 10px;
    }
    .text{
        
        margin-top: -22px;
        width: 250px;
        color: #f40;
    }
    .a :hover{
        color: #FF5000;
    }
    .a{
        color: gray;
        text-decoration: none;
        font-size: 15px;
    }
</style>