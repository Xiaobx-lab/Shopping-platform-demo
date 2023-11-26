<template>
  <div>
    <top :top1_href="top1_href"/>
    <search />
    <!--遍历商品-->
    <content_ :goodsList="goodsList" />
    <page  v-model="currentPage" />
    {{currentPage}}
  </div>
</template>

<script>
import top from '@/components/top'
import search from '@/components/search'
import content_ from '@/components/content_'
import page from '@/components/page'
import axios from 'axios';
export default {
    data() {
        return {
            top1_href:"/login",
            goodsList: [],
            currentPage: 1,
            pageSize: 10
        }
    },
    mounted() {
        this.fetchGoodsList();
    },
    methods: {
        fetchGoodsList() {
            axios.get(`/goods/?page=${this.currentPage}&page_size=${this.pageSize}`)  // 发送GET请求到后台的API接口
                .then(response => {
                    this.goodsList = response.data;
                    console.log(response.data)
                })
                .catch(error => {
                    console.error(error);
                });
            }
    },
    watch:{
        currentPage(){
            this.fetchGoodsList();
        }
    },
    components:{top,search,content_,page}
}

</script>

<style>

</style>