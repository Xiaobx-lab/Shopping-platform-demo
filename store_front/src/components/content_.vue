<template>
  <div >
    <span class="card" v-for="item in goodsList" v-bind:key = "item.id" style="display:inline-block;width:20%; padding:20px">
        <router-link :to="'/goods/goodsDetail/' + item.id ">
            <img class="card-img-top" :src="item.color_url" alt="Card image cap">
            <div class="card-body">
            <span class="card-title" style="color:#333333">{{item.gname}}</span>
                <div style="display:inline-block">
                    <img src="../assets/coupon1.png" style="height: 10px; margin-top: 4px;margin-left: 0px">
                    <input type="submit" value="加入购物车" style="height: 30px;border: none;">
                </div>
                <div style="display:inline-block;margin-top:5px">
                    <span style="color: #FD3F31">{{item.price}}</span>
                    <span style="color:#333333;text-decoration: line-through;font-size:smaller">{{item.oldprice}}</span>
                </div>
            </div>
            <div class="card-footer">
            <small class="text-muted" >库存{{item.count}}</small>
            </div>
        </router-link>

    </span>
    <chat />
  </div>
</template>

<script>
import chat from '@/components/chat'
export default {
    props:{
        goodsList:{
            required:false,
            type: Array
        },
 
    },
    methods: {

    },
    components:{chat}

}
</script>

<style>

</style>