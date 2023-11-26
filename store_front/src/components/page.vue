<template>
  <div>
    <nav aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
        <li class="page-item ">
        <a class="page-link" @click="previousPage">上一页</a>
        </li>
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item"><a class="page-link" href="#">2</a></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item">
        <a class="page-link" @click="nextPage">下一页</a>
        </li>
    </ul>
    </nav>
  </div>
</template>

<script>
export default {
    props:{
        value: {
                required:false,
                type:Number
            },
    },
    methods: {
        previousPage:function(){
            if (this.value > 1) {
                this.value--;
                this.$emit('input', this.value)
            }
        },
        nextPage:function() {
            this.value++;
            this.$emit('input', this.value)
            console.log(this.value)
        },

    },
}
</script>

<style>

</style>