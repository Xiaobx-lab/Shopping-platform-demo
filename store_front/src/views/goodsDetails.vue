<template>
  <div>
    <top :top1_href="'/login'"/>
    <search />
    <div class="container">
        <div class="row justify-content-center product-details">
            <div class="col-md-6">
                <img :src="goodsDetails.color_url" style="width:70%" alt="Product Image" >
            </div>
            <div class="col-md-6 ">
                <div style="border: 0px solid grey; padding:10px; padding-bottom: 60px; background:#F5F5F5 ">
                    <h2 class="product-title">{{goodsDetails.gname}}</h2>
                    <p class="product-description">{{goodsDetails.gdesc}}</p>
                    <div style="display: inline-block">
                        <span class="product-price" >¥{{goodsDetails.price}}</span>
                        <span class="product-old-price">{{goodsDetails.oldprice}}</span>
                    </div>

                    <div class="product-attributes" >
                        <span class="attribute-label" style="font-weight:bold;margin-right:30px">颜色</span>
                        <a href="#" v-for="color_url in goodsDetails.color_urls" v-bind:key="color_url">
                            <img :src="color_url" style="width:9%;padding:2px;padding-top:10px " alt="Product Image"   >
                        </a>
                    </div>
                    <div>
                        <span class="attribute-label" style="font-weight:bold;margin-right:65px">尺码</span>
                        <span v-for="size in goodsDetails.sizes" v-bind:key="size" class="size-info">{{size}}</span>
                    </div>
                    <button class=" btn add-to-cart-button" style="background-color:darkorange;margin-top:50px">加入购物车</button>
                </div>

            </div>
        </div>
        <!--模特实拍图头上的导航栏-->
        <ul class="nav nav-tabs" style="margin-top:10px;margin-bottom:10px">
        <li class="nav-item">
            <a class="nav-link active" href="#" style="color:red">商品详情</a>
        </li>
        <li class="nav-item">
            <a class="nav-link dark"  href="#" style="color:black">物流与售后</a>
        </li>
        <li class="nav-item">
            <a class="nav-link dark" href="#" style="color:black">消费保障</a>
        </li>
        <li class="nav-item">
            <a class="nav-link disabled" href="#" style="color:black">手机购买</a>
        </li>
        </ul>
        <!--模特实拍图等展示-->
        <div class="show-model">
            <div v-for="(gdurlList,gdname ) in goodsDetails.detailsList" v-bind:key="gdname">
          
                <p style="color:grey;">{{gdname}}</p>
                

 
                
                <span v-for="gdurl in gdurlList" :key="gdurl">
                    <img :src="gdurl" alt="gdurl">        
                </span>
            </div>    
        </div>
    </div>
    <guessYouLike />
    <content_ :goodsList=" goodsDetails.recommend_list" style="margin-top:20px"/>
  </div>
</template>

<script>
import axios from 'axios';
import top from '@/components/top'
import search from '@/components/search'
import guessYouLike from '@/components/guessYouLike'
import content_ from '@/components/content_'
export default {
    data() {
        return {
            goodsID: 1 ,
            goodsDetails:[],
        }
    },
    mounted() {
        this.goodsID = this.$route.params.id; // 使用 this.$route.params.id 来获取路由参数
        this.fetchGoodsList();
    },
    methods: {
        fetchGoodsList(){
            axios.get('/goods/api/goodsDetail', {
                params: {
                    id: this.goodsID
                }
            }).then(response => {
                    this.goodsDetails = response.data;
                    console.log(response.data)
                })
                .catch(error => {
                    console.error(error);
                });
        }
    },
    components:{top,search,guessYouLike,content_}
}
</script>


<style>
    body {
      background-color: #f8f9fa;
    }

    .product-details {
      margin-top: 50px;
    }
    
    .size-info{
        font-size: small;
        border-color:darkgrey;
        border-style: solid;
        border-width: 0.1px;
        padding: 6px;
        margin: 2px;
    }

    .product-title {
      font-size: 24px;
      margin-bottom: 20px;
      font: bolder;
    }

    .product-description {
      color: #6c757d;
      margin-bottom: 30px;
      font-size: smaller;
    }

    .product-price {
      font-size: 30px;
      font-weight: bold;
      margin-bottom: 10px;
      color: crimson;
    }
    .product-old-price {
      font-size: 15px;
      text-decoration: line-through;
      margin-bottom: 10px;
    }

    .product-attributes {
      margin-bottom: 20px;
    }


    .add-to-cart-button {
      padding: 10px 30px;
      background-color: crimson;
      font-size: 10px;
      color:black;
    }
</style>